from setuptools import setup

setup(
    name='flask_google_auth',
    packages=['flask_google_auth'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-Dance',
        'Flask-Login',
        'pyOpenSSL'
    ],
)