#!/usr/bin/python3
from distutils.cmd import Command
from distutils.core import setup


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        raise SystemExit(
            subprocess.call(
                [
                    sys.executable,
                    '-m',
                    'unittest'
                ]
            )
        )


setup(
    name="WeatherApp",
    version="0.1.0",
    author="efkin",
    author_email="efkin@riseup.net",
    license="GPLv3",
    scripts=["WeatherApp"],
    packages=["weatherapp"],
    package_data={
        "weatherapp": ["data/ui.glade"],
    },
    data_files=[
        ("share/applications", ["WeatherApp.desktop"])
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    cmdclass={
        'test': TestCommand
    }
)
