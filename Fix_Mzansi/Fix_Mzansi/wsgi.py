"""
WSGI config for Fix_Mzansi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fix_Mzansi.settings')

application = get_wsgi_application()


# Define the directory and file paths
directory_path = os.path.expanduser('~/.postgresql')
file_path = os.path.join(directory_path, 'root.crt')

# Ensure the directory exists
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Write the content to the file
with open(file_path, 'w') as file:
    file.write(os.getenv('CERT'))

# For Vercel
app = application
