"""
Setup configuration for installation via pip, easy_install, etc.

"""
from setuptools import setup, find_packages

# The find_packages function does a lot of the heavy lifting for us w.r.t.
# discovering any Python packages we ship.
setup(
    name='thrustcurve',
    version='0.1.0',
    packages=find_packages(),

    # PyPI packages required for the *installation* and usual running of the
    # tools.
    install_requires=[
        'pandas',
        'future', # Python 2/3 compatibility
    ],

    # Metadata for PyPI (https://pypi.python.org).
    description='Parse engine thrust curve files for amateur rocketry',
    url='https://github.com/rjw57/thrustcurve',
    author='Rich Wareham',
    author_email='rich.thrustcurve@richwareham.com',
)

