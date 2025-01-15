"""
This module provides the service for restore.
"""
from __future__ import annotations

import os

from src.data.repository.common_operations_repository import CommonOperationRepository
from src.model.common_operation_model import RestoreRequestModel
from src.model.common_operation_model import RestoreResponseModel
from src.utils.custom_exception import CommonException
from src.utils.error_message import ERROR_NOT_BACKUP_FILE
from src.utils.error_message import ERROR_UNABLE_GET_MNEMONIC
from src.utils.error_message import ERROR_UNABLE_TO_GET_HASHED_MNEMONIC
from src.utils.error_message import ERROR_UNABLE_TO_GET_PASSWORD
from src.utils.error_message import ERROR_WHILE_RESTORE_DOWNLOAD_FROM_DRIVE
from src.utils.gdrive_operation import GoogleDriveManager
from src.utils.handle_exception import handle_exceptions
from src.utils.helpers import hash_mnemonic
from src.utils.local_store import local_store
from src.utils.logging import logger


class RestoreService:
    """
    Service class to handle the backup operations.
    """

    @staticmethod
    def restore(mnemonic: str, password: str) -> RestoreResponseModel:
        """
        Creates a backup of the node's data and uploads it to Google Drive.

        Returns:
            bool: True if the backup and upload were successful, False otherwise.

        Raises:
            CommonException: If any operation fails during the backup process.
        """
        try:
            if not mnemonic:
                raise CommonException(ERROR_UNABLE_GET_MNEMONIC)

            hashed_mnemonic = hash_mnemonic(mnemonic_phrase=mnemonic)

            if not hashed_mnemonic:
                raise CommonException(ERROR_UNABLE_TO_GET_HASHED_MNEMONIC)

            restore_file_name: str = f'{hashed_mnemonic}.rgb_backup'

            local_store_base_path = local_store.get_path()
            restore_folder_path = os.path.join(
                local_store_base_path, 'restore',
            )

            # Ensure the backup folder exists
            if not os.path.exists(restore_folder_path):
                logger.info('Creating backup folder')
                local_store.create_folder('restore')

            restore_file_path = os.path.join(
                restore_folder_path, restore_file_name,
            )

            # Remove if old backup file available at local store of application
            if os.path.exists(restore_file_path):
                os.remove(restore_file_path)

            if not password:
                raise CommonException(
                    ERROR_UNABLE_TO_GET_PASSWORD,
                )

            # Download restore zip from Google Drive
            logger.info('Downloading restore zip from drive')
            restore = GoogleDriveManager()
            success: bool | None = restore.download_from_drive(
                file_name=restore_file_name, destination_dir=restore_folder_path,
            )

            if success is None:
                raise CommonException(ERROR_NOT_BACKUP_FILE)

            if not success:
                raise CommonException(ERROR_WHILE_RESTORE_DOWNLOAD_FROM_DRIVE)

            # Perform the Restore operation
            logger.info('Calling restore api')
            response: RestoreResponseModel = CommonOperationRepository.restore(
                RestoreRequestModel(
                    backup_path=restore_file_path, password=password,
                ),
            )
            return response
        except Exception as exc:
            return handle_exceptions(exc)
