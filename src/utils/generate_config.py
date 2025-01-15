"""
This script reads environment variables for client configuration secrets and
writes them into a `config.py` file. The `config.py` file will contain a
dictionary named `client_config` with the provided secrets.

Steps:
1. Read environment variables for the client configuration secrets.
2. Format the secrets into a dictionary structure.
3. Write the formatted dictionary to a `config.py` file.
"""
from __future__ import annotations

import os

# Read environment variables
client_id = os.getenv('CLIENT_ID')
project_id = os.getenv('PROJECT_ID')
auth_uri = os.getenv('AUTH_URI')
token_uri = os.getenv('TOKEN_URI')
auth_provider_cert_url = os.getenv('AUTH_PROVIDER_CERT_URL')
client_secret = os.getenv('CLIENT_SECRET')

# Create the content of config.py
config_content = f"""
client_config = {{
    'installed': {{
        'client_id': '{client_id}',
        'project_id': '{project_id}',
        'auth_uri': '{auth_uri}',
        'token_uri': '{token_uri}',
        'auth_provider_x509_cert_url': '{auth_provider_cert_url}',
        'client_secret': '{client_secret}',
    }},
}}
"""

# Write the content to config.py
with open('../../config.py', 'w', encoding='utf-8') as config_file:
    config_file.write(config_content)
