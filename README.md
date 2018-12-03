# README

## Description

A simple weather forecasting desktop app.

## Install dependencies

* python3
* python3-gi
* python3-requests
* python3-matplotlib

## How to install

You can use the already packaged versions in ./dist issuing:

```
$ sudo dpkg -i dist/weatherapp_X.Y.Z_amd64.deb
```

Or following the build instructions.

## How to test

Simply run:

```
python3 setup.py test
```

## How to build

Make sure you've installed the following dependencies:

* devscripts
* dh-python
* python3

And issue the following command:

```
$ debuild -us -uc
```

The actual .deb package will be realeased in the `./../` directory.

Simply install it via:

```
$ sudo dpkg -i ../weatherapp_0.1.0_amd64.deb
```
