#!/usr/bin/python3

from distutils.core import setup


setup(
    name="WeatherApp",
    version="0.1.0",
    descripition="A simple forecasting app using OWM",
    author="efkin",
    author_email="efkin@riseup.net",
    license="GPLv3",
    scripts=["WeatherApp"],
    packages=["weatherapp"],
    data_files=[
        ("lib/WeatherApp", ["ui.glade"]),
        ("share/applications", ["WeatherApp.desktop"])
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
