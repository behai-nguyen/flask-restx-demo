"""Installation script for flask_restx demo project."""
from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='flask-restx-demo',
    description='Flask-RESTX and Swagger UI Demo.',
    version='1.0.0',
    author='Van Be Hai Nguyen',
    author_email='behai_nguyen@hotmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires='>=3.10',
    install_requires=[
        'Flask',
        'python-dotenv',
        'Flask-RESTX',
        'Flask-SQLAlchemy',
        'Flask-Cors',
        'werkzeug==2.1.2',
    ],
)