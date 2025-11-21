"""
Setup script for creating a macOS .app bundle using py2app
Usage: python3 setup.py py2app
"""

from setuptools import setup

APP = ['calculator.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'plist': {
        'CFBundleName': 'Calculator',
        'CFBundleDisplayName': 'Simple Calculator',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleIdentifier': 'com.machinelearning.calculator',
        'NSHumanReadableCopyright': 'Open source calculator application',
    }
}

setup(
    name='Calculator',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
