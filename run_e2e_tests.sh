#!/usr/bin/env bash

set -e  # Exit on error
set -o pipefail  # Exit if any command in a pipeline fails
set -u  # Treat unset variables as errors

# Define paths
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
E2E_DIR="$ROOT_DIR/e2e_tests"
TESTS_DIR="$E2E_DIR/test/spec"
APPLICATIONS_DIR="$E2E_DIR/applications"
VERSION=$(grep '__version__' ./src/version.py | awk -F'=' '{print $2}' | tr -d ' "' | xargs)

# Paths for the built applications
APP1_NAME="iriswallet-${VERSION}-x86_64.AppImage"
APP2_NAME="iriswallet_app_1-${VERSION}-x86_64.AppImage"

APP1_PATH="$APPLICATIONS_DIR/$APP1_NAME"
APP2_PATH="$APPLICATIONS_DIR/$APP2_NAME"

# Paths for constants file
CONSTANT_FILE="./src/utils/constant.py"
BACKUP_FILE="./src/utils/constant_backup.py"

# Command-line arguments
TEST_FILE=""       # Test file to run (if specified)
RUN_ALL=false      # Default: Do not run all tests
FORCE_BUILD=false  # Default: Do not force rebuild
WALLET_MODES=()    # Wallet modes to run tests for (default: both)

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --force-build)
            FORCE_BUILD=true
            shift
            ;;
        --all)
            RUN_ALL=true
            shift
            ;;
        --wallet-mode)
            if [[ -n "$2" ]]; then
                WALLET_MODES+=("$2")  # Add provided wallet mode
                shift 2
            else
                echo "Error: --wallet-mode requires a value (embedded or connect)."
                exit 1
            fi
            ;;
        *)
            TEST_FILE=$1  # Assume first non-flag argument is the test file
            shift
            ;;
    esac
done

# If no wallet mode is provided, default to both modes
if [[ ${#WALLET_MODES[@]} -eq 0 ]]; then
    WALLET_MODES=("embedded" "connect")
fi

# Ensure constants are restored if the script exits unexpectedly
trap restore_constants EXIT

# Function to temporarily modify constants before build
modify_constants() {
    echo "Modifying constants for testing..."

    # Backup the original file only if it hasn't been backed up
    if [[ ! -f "$BACKUP_FILE" ]]; then
        cp "$CONSTANT_FILE" "$BACKUP_FILE"
    fi

    sed -i -E "
        s|BITCOIND_RPC_HOST_REGTEST = 'regtest-bitcoind.rgbtools.org'|BITCOIND_RPC_HOST_REGTEST = 'localhost'|;
        s|BITCOIND_RPC_PORT_REGTEST = 80|BITCOIND_RPC_PORT_REGTEST = 18443|;
        s|INDEXER_URL_REGTEST = 'electrum.rgbtools.org:50041'|INDEXER_URL_REGTEST = '127.0.0.1:50001'|;
        s|PROXY_ENDPOINT_REGTEST = 'rpcs://proxy.iriswallet.com/0.2/json-rpc'|PROXY_ENDPOINT_REGTEST = 'rpc://127.0.0.1:3000/json-rpc'|;
    " "$CONSTANT_FILE"

    echo "Constants modified."
}

# Function to restore original constants after build
restore_constants() {
    if [[ -f "$BACKUP_FILE" ]]; then
        echo "Restoring original constants..."
        mv -f "$BACKUP_FILE" "$CONSTANT_FILE"
        echo "Original constants restored."
    fi
}

# Function to move an application after it is built
move_application() {
    local app_name=$1
    local app_path="$ROOT_DIR/$app_name"

    echo "Moving $app_name to $APPLICATIONS_DIR..."
    mkdir -p "$APPLICATIONS_DIR"

    if [[ -f "$app_path" ]]; then
        mv -f "$app_path" "$APPLICATIONS_DIR/"
        echo "$app_name moved successfully."
    else
        echo "Error: $app_name not found at $app_path"
        exit 1
    fi
}

# Function to build applications (only if --force-build is passed)
build_applications() {
    echo "Building applications..."

    cd "$ROOT_DIR" || exit 1

    # Modify constants before build
    modify_constants

    # Build first application
    echo "Building first application..."
    build-iris-wallet --network regtest --distribution appimage &
    wait $!
    move_application "$APP1_NAME"

    # Build second application
    echo "Building second application..."
    build-iris-wallet --network regtest --distribution appimage --app-name app_1 &
    wait $!
    move_application "$APP2_NAME"

    echo "Build completed successfully."
}

# **If --force-build is passed, build and exit**
if [[ "$FORCE_BUILD" == true ]]; then
    build_applications
    exit 0
fi

# Function to run E2E tests with wallet mode
run_e2e_tests() {
    local wallet_mode=$1
    local results_dir="allure-results-${wallet_mode}"

    echo "Running E2E tests with wallet mode: $wallet_mode"

    # Remove old results
    rm -rf "$results_dir"
    mkdir -p "$results_dir"

    if [[ "$RUN_ALL" == true ]]; then
        echo "Running full test suite..."
        pytest -s "$TESTS_DIR/" --alluredir="$results_dir" --wallet-mode "$wallet_mode"
    elif [[ -n "$TEST_FILE" ]]; then
        echo "Running single test file: $TEST_FILE"
        pytest -s "$TESTS_DIR/$TEST_FILE" --alluredir="$results_dir" --wallet-mode "$wallet_mode"
    else
        echo "No test file provided. Use --all to run all tests."
        exit 1
    fi

    # Check if pytest failed
    if [[ $? -ne 0 ]]; then
        echo "E2E tests failed!"
        exit 1
    fi
}

# Run tests for selected wallet modes
for mode in "${WALLET_MODES[@]}"; do
    run_e2e_tests "$mode"
done

echo "Setup and tests completed successfully!"
