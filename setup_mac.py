"""
This is a setup.py script generated by py2applet

Usage:
    python setup_mac.py py2app
"""

from setuptools import setup

APP = ['main.py']
APP_NAME="Casulana"
DATA_FILES = [('', ['Recordings'])]
OPTIONS = {'argv_emulation': True,
           'iconfile': 'Other_data/music.icns',
           'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleShortVersionString': "1.03.m",
        'NSHumanReadableCopyright': u"Copyright © 2016, Antoine Somma, All Rights Reserved"
           }
}


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
