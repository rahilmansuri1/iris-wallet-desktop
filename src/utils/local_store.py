# pylint: disable=missing-docstring
from __future__ import annotations

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QDir
from PySide6.QtCore import QSettings
from PySide6.QtCore import QStandardPaths

from src.flavour import __network__
from src.utils.constant import APP_NAME
from src.utils.constant import ORGANIZATION_DOMAIN
from src.utils.constant import ORGANIZATION_NAME


class LocalStore:
    def __init__(self, app_name, org_name, org_domain):
        # Set application-wide properties
        QCoreApplication.setApplicationName(app_name)
        QCoreApplication.setOrganizationName(org_name)
        QCoreApplication.setOrganizationDomain(org_domain)

        # Adjust the base path to include directory like 'com.iris'
        self.base_path = QStandardPaths.writableLocation(
            QStandardPaths.AppDataLocation,
        )

        # Initialize settings with a custom location
        self.settings_path = QDir(self.base_path).filePath(
            f'{app_name}-{__network__}.ini',
        )
        self.settings = QSettings(self.settings_path, QSettings.IniFormat)

    def set_value(self, key, value):
        self.settings.setValue(key, value)

    def get_value(self, key, value_type=None):
        value = self.settings.value(key)
        if value_type and value is not None:
            try:
                return value_type(value)
            except (TypeError, ValueError):
                return None
        return value

    def remove_key(self, key):
        self.settings.remove(key)

    def clear_settings(self):
        self.settings.clear()

    def all_keys(self):
        return self.settings.allKeys()

    def get_path(self):
        return self.base_path

    def create_folder(self, folder_name):
        print('Base path', self.base_path)
        folder_path = QDir(self.base_path).filePath(folder_name)
        QDir().mkpath(folder_path)
        print('after', folder_path)
        return folder_path


local_store = LocalStore(APP_NAME, ORGANIZATION_NAME, ORGANIZATION_DOMAIN)
