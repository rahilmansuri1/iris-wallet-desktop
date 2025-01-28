"""This module contain error messages"""
from __future__ import annotations

ERROR_NODE_ALREADY_INITIALIZED = 'Node has already been initialized'
ERROR_NODE_IS_LOCKED_CALL_UNLOCK = 'Node is locked (hint: call unlock)'
ERROR_PASSWORD_INCORRECT = 'The provided password is incorrect'
ERROR_NODE_IS_UNLOCKED_CALL_LOCK = 'Node is unlocked (hint: call lock)'
ERROR_NODE_WALLET_NOT_INITIALIZED = 'Wallet has not been initialized (hint: call init)'
ERROR_SOMETHING_WENT_WRONG = 'Something went wrong'
ERROR_UNABLE_TO_STOP_NODE = 'Unable to stop ln node'
ERROR_LN_OFF_CHAIN_SEND_FAILED = 'Unable to send asset. The channel might be closed or not open with.'
ERROR_LOCK_NODE = 'Please lock your node,Try again'
ERROR_UNABLE_TO_SET_FEE = 'Unable to set fee rate'
ERROR_UNABLE_GET_MNEMONIC = "'Unable to get mnemonic"
ERROR_UNABLE_TO_GET_PASSWORD = 'Unable to get password'
ERROR_UNABLE_TO_GET_HASHED_MNEMONIC = 'Unable to get hashed mnemonic'
ERROR_WHILE_RESTORE_DOWNLOAD_FROM_DRIVE = 'Something went wrong while download restore zip from drive'
ERROR_NATIVE_AUTHENTICATION = 'Authentication failed.'
ERROR_WHILE_RESTORE = 'Restore Failed.'
ERROR_NOT_BACKUP_FILE = 'Backup file not found in google drive'
ERROR_GOOGLE_CONFIGURE_FAILED = 'Google drive configuration Failed'
ERROR_GOOGLE_DRIVE_CONFIGURE_NOT_FOUND = 'Google drive configuration not found,Please re-configure'
ERROR_WHEN_DRIVE_STORAGE_FULL = 'Google Drive storage is full. Cannot upload the file.'
ERROR_NODE_CHANGING_STATE = 'Cannot call other APIs while node is changing state'
ERROR_UNABLE_TO_START_NODE = 'Unable to start node,Please close application and restart'
ERROR_NETWORK_MISMATCH = 'Network configuration does not match.'
ERROR_KEYRING_STATUS = 'Unable to set keyring status'
ERROR_KEYRING = 'Feature disabled: Keyring disabled or inaccessible.'
ERROR_KEYRING_STORE_NOT_ACCESSIBLE = 'Your keyring store not accessible'
ERROR_FAILED_TO_GET_FAUCET_URL = 'Failed to get faucet url'
ERROR_INVALID_NETWORK_TYPE = 'Invalid network type'
ERROR_IMAGE_PATH_NOT_EXITS = 'Provided image file path not exits'
ERROR_BACKUP_FILE_NOT_EXITS = 'Backup file does not exist at'
ERROR_CAPACITY_OF_CHANNEL = 'Channel amount must equal or higher then 5506 sats'
ERROR_SAVE_LOGS = 'Failed to save logs: {}'
ERROR_UNEXPECTED = 'An unexpected error occurred: {}'
ERROR_FIELD_MISSING = 'Few fields missing'
ERROR_AUTHENTICATION = 'Authentication failed'
ERROR_AUTHENTICATION_CANCELLED = 'Authentication failed or canceled.'
ERROR_G_DRIVE_CONFIG_FAILED = 'Google drive configuration Failed'
ERROR_INVALID_INVOICE = 'Please enter valid invoice.'
ERROR_FAILED_TO_GET_BALANCE = 'Failed to get balance: {}'
ERROR_NAVIGATION_BITCOIN_PAGE = 'Error: Unable to navigate on send bitcoin page - {}'
ERROR_NAVIGATION_RECEIVE_BITCOIN_PAGE = 'Error: Unable to navigate on receive bitcoin page - {}'
ERROR_UNABLE_TO_CALL_API_FROM_CATCH = 'Unable to call {} from cache'
ERROR_ENDPOINT_NOT_ALLOW_TO_CACHE_CHECK_CACHE_LIST = 'Provide endpoint {} not allow to cache please check cache list in endpoints.py file'
ERROR_CREATE_UTXO_FEE_RATE_ISSUE = 'Unexpected error'
ERROR_MESSAGE_TO_CHANGE_FEE_RATE = 'Please change default fee rate from setting page'
ERROR_OPERATION_CANCELLED = 'Operation cancelled'
ERROR_NEW_CONNECTION_ERROR = 'Failed to connect to the server.because of network connection.'
ERROR_MAX_RETRY_EXITS = 'Max retries exceeded. while checking internet connection.'
ERROR_NAME_RESOLUTION_ERROR = 'DNS resolution failed. Because DNS settings.'
ERROR_UNEXPECTED_WHILE_INTERNET = 'Error while checking internet connection: {}'
ERROR_CONNECTION_FAILED_WITH_LN = 'Connection failed with provide lightning node url'
ERROR_REQUEST_TIMEOUT = 'Request time out'
ERROR_UNSPECIFIED_SERVER_ERROR = 'Unspecified server error'
ERROR_TYPE_VALIDATION = 'Type validation error'
ERROR_SOMETHING_WENT_WRONG_WHILE_UNLOCKING_LN_ON_SPLASH = 'An error occurred while unlocking the node. Please try unlocking the node manually.'
ERROR_NOT_ENOUGH_UNCOLORED = 'No uncolored UTXOs are available (hint: call createutxos)'
ERROR_INSUFFICIENT_ALLOCATION_SLOT = 'Cannot open channel: InsufficientAllocationSlots'
ERROR_COMMITMENT_TRANSACTION_FEE = 'Insufficient capacity to cover transaction fees. You need at least {}'
ERROR_CREATE_UTXO = 'Error while creating UTXO: {}'
ERROR_TITLE = 'Error'
ERROR_SEND_ASSET = 'Error sending asset: {}'
ERROR_BACKUP_FAILED = "Backup couldn't complete. Please try once more."
ERROR_LN_OFF_CHAIN_UNABLE_TO_SEND_ASSET = 'Unable to send assets, a path to fulfill the required payment could not be found'
ERROR_UNABLE_TO_SET_EXPIRY_TIME = 'Unable to set expiry time'
ERROR_FAIL_TRANSFER = 'Failed to mark the transfer as unsuccessful.'
ERROR_UNABLE_TO_SET_INDEXER_URL = 'The indexer endpoint is invalid'
ERROR_UNABLE_TO_SET_PROXY_ENDPOINT = 'The proxy endpoint is invalid'
ERROR_UNABLE_TO_SET_MIN_CONFIRMATION = 'Unable to set min confirmation'
