# E2E Tests Using Dogtail

## Run Locally

## Prerequisites
Before you begin, ensure you have the following installed:
- **Operating System:** Ubuntu 22 (only)
- **Wayland must be disabled** (Ensure your session is running on **X11**)
- **Python 3.12**
- **Poetry** (Python dependency management tool)
- **Rust** (latest version for compiling the Lightning Node binary)
- **Docker** (required for running the regtest environment)
- **Meson** (required for `pycairo` package)
  ```bash
  sudo apt install meson
  ```
- **Python Development Package** (ensure you have `python3.12-dev` installed)
- **libgirepository1.0-dev** (required for `pygobject` package)
  ```bash
  sudo apt install libgirepository1.0-dev
  ```
- **libfuse2** (required for building the application)
  ```bash
  sudo apt install libfuse2
  ```
- **xclip** (required for the `pyperclip` package)
  ```bash
  sudo apt install xclip
  ```
- **wmctrl** (required to maximize the application window)
  ```bash
  sudo apt install wmctrl
  ```
- **Java (JRE & JDK)** (required for Allure report generation)
  ```bash
  sudo apt install default-jre default-jre-headless openjdk-11-jdk
  ```
- **Allure** (for detailed test reporting)
   1. Download the `.tgz` file from the [Allure Releases](https://github.com/allure-framework/allure2/releases).
   2. Extract the file:
      ```bash
      tar -xvzf allure-2.x.x.tgz
      ```
   3. Move the extracted folder to `/opt` and create a symbolic link:
      ```bash
      sudo mv allure-2.x.x /opt/allure
      sudo ln -s /opt/allure/bin/allure /usr/local/bin/allure
      ```

---

## Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RGB-Tools/iris-wallet-desktop.git
   cd iris-wallet-desktop
   ```

2. **Create a `.env` File**
   Create a `.env` file in the **root directory** and add the following values:
   ```dotenv
   EMAIL_ID=<EMAIL_ID>
   PASSWORD=<PASSWORD>
   SECRET_KEY=<GOOGLE_2FA_SETUP_KEY>
   AUTHENTICATION_PASSWORD=<AUTHENTICATION_PASSWORD>
   ```
   **Note:** These credentials will be used in the following tests:
   - `test_backup_and_restore`
   - `test_ask_auth_for_imp_operations`
   - `test_login_app_auth`

    Provide the `GOOGLE_AUTHENTICATOR` **without spaces**.
    Use **single quotes** around `<PASSWORD>`, and avoid passwords containing single quotes.

3. **Install Poetry**
   Install Poetry using pip:
   ```bash
   pip install poetry
   ```

4. **Install Dependencies**
   Run the following command to install all required dependencies:
   ```bash
   poetry install
   ```

5. **Run the Regtest Services**
   Start the regtest environment:
   ```bash
   poetry run regtest-start
   ```

6. **Run Test Cases**
   Run test cases with the following options:
   ```bash
   # Run all tests
   poetry run e2e-test all

   # Run tests for a specific wallet mode (optional)
   poetry run e2e-test all remote     # For remote mode
   poetry run e2e-test all embedded   # For embedded mode

   # Run a specific test
   poetry run single-test <TEST_NAME>

   # Run a specific test for a specific wallet mode (optional)
   poetry run single-test <TEST_NAME> remote     # For remote mode
   poetry run single-test <TEST_NAME> embedded   # For embedded mode

   # Force the build process during test execution
   poetry run e2e-test all --force-build
   poetry run single-test <TEST_NAME> force-build

   # Combine both options
   poetry run e2e-test all remote force-build
   ```
   **Note:** Both `wallet_mode` and `force-build` flags are optional.

7. **Check Test Results**
   ```bash
   # For embedded mode results
   poetry run result-embedded

   # For remote mode results
   poetry run result-remote
   ```

---

## E2E-Tests Directory Structure
```
e2e-tests/
├── assets/           # Static assets and resources used in tests
├── application/      # Application required for the test
├── test/             # Main test-related files
│   ├── features/     # Basic application functionalities to be tested
│   ├── pageobjects/  # Methods to interact with specific page objects
│   ├── specs/        # Test cases to be executed using Dogtail
│   └── utilities/    # Utilities shared across tests
```

---
