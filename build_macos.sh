#!/bin/bash

# Getting the app name and version from version.py and constant.py.
APP_NAME=$(grep 'APP_NAME' ./src/utils/constant.py | awk -F'=' '{print $2}' | tr -d ' "' | xargs)
VERSION=$(grep '__version__' ./src/version.py | awk -F'=' '{print $2}' | tr -d ' "' | xargs)


# Check if APP_NAME and VERSION are non-empty
if [ -z "${APP_NAME}" ]; then
    echo "APP_NAME is empty. Please check the extraction command."
    exit 1
fi

if [ -z "${VERSION}" ]; then
    echo "VERSION is empty. Please check the extraction command."
    exit 1
fi

# Get the current directory
CURRENT_DIR="$(pwd)"
DIST_PATH="$CURRENT_DIR/dist"
APP_BUNDLE="${DIST_PATH}/${APP_NAME}.app"

# Build the .app with PyInstaller
echo "Building .app with PyInstaller..."
poetry run pyinstaller iris_wallet_desktop.spec

# List the contents of the dist directory to see what was created
echo "Contents of dist directory:"
ls -l "${DIST_PATH}"

# Check if the app bundle was created successfully
if [ -d "${APP_BUNDLE}" ]; then
    echo "App bundle created successfully."
    echo "Creating DMG file..."
    npx create-dmg --dmg-title="${APP_NAME}-${VERSION}" "${APP_BUNDLE}"

    echo "DMG file created successfully."

    echo "Removing app bundle..."
    rm -rf "${DIST_PATH}"

else
    echo "Failed to create app bundle. Expected path not found: ${APP_BUNDLE}"
fi
