"""Module to clean up the iriswallet directory by deleting all its contents. Use with caution as this will permanently remove all wallet data."""
from __future__ import annotations

import os
import shutil
import sys

from src.utils.local_store import local_store


def delete_app_data(directory_path: str):
    """
    Delete all files and directories in the specified directory.

    Args:
        directory_path (str): The path to the directory from which files and directories will be deleted.

    Raises:
        Exception: If an error occurs during the deletion process.
    """
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            print(f'Directory does not exist: {directory_path}')
            return

        # Remove all files and directories in the path
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)  # Remove file or symbolic link
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove directory and its contents

        print(
            f'All files and directories in {directory_path} have been deleted.',
        )
    except Exception as e:
        print(f'An error occurred while deleting files: {e}')


def main():
    """
    Main function to clean up the iriswallet directory.

    It retrieves the path to the iriswallet directory and then deletes all its contents.

    Note:
        This script is intended for development and testing purposes only. Use with caution as it will
        permanently delete data in the specified directory.
    """
    # Path to the iriswallet directory
    iriswallet_path = local_store.get_path()
    print(f'Directory to clean: {iriswallet_path}')

    # Prompt user for confirmation
    confirm = input(
        'Warning: This will permanently delete all data in the iriswallet directory. Proceed? (y/n): ',
    ).strip().lower()

    if confirm != 'y':
        print('Operation cancelled. No data was deleted.')
        sys.exit(1)

    try:
        # Delete all files and directories in the iriswallet path
        delete_app_data(iriswallet_path)

        print('Cleanup complete.')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
