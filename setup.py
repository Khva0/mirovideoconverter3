"""
This is a setup.py script generated by py2applet

Usage:
    python2.7 setup.py py2app
"""
import sys
if sys.version < '2.7':
    raise RuntimeError('MVC requires Python 2.7')
import glob
import os.path
import shutil

from setuptools import setup
from setuptools.extension import Extension

from py2app.build_app import py2app as py2app_cmd

from mvc.settings import (get_ffmpeg_executable_path,
                          get_ffmpeg2theora_executable_path)

ROOT = os.path.dirname(__file__)

APP = ['mvc/ui/widgets.py']
DATA_FILES = ['mvc/widgets/osx/Resources-Widgets/MainMenu.nib']
OPTIONS = {
    'excludes': ['mvc.widgets.gtk'],
    'includes': ['mvc.widgets.osx.fasttypes'],
    'packages': ['mvc', 'mvc.widgets', 'mvc.widgets.osx', 'mvc.ui', 'mvc.resources']
}

class py2app_mvc(py2app_cmd):

    def run(self):
        py2app_cmd.run(self)
        bundle_root = os.path.join(self.dist_dir,
                                   'Miro Video Converter.app/Contents')
        helpers_root = os.path.join(bundle_root, 'Helpers')
        if os.path.exists(helpers_root):
            shutil.rmtree(helpers_root)
        print 'Copying FFmpeg to', helpers_root
        os.mkdir(helpers_root)
        self.copy_file(get_ffmpeg_executable_path(), helpers_root)
        self.copy_file(get_ffmpeg2theora_executable_path(), helpers_root)

setup(
    name="Miro Video Converter",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    cmdclass={'py2app': py2app_mvc},
    ext_modules=[
        Extension("mvc.widgets.osx.fasttypes",
                  [os.path.join(ROOT, 'mvc', 'widgets', 'osx', 'fasttypes.c')])],
    )
