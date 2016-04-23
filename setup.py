from setuptools import setup

setup(
    # Application name:
    name="Passman",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Tarun Mukherjee",
    author_email="tmukherjee13@gmail.com",

    # Packages
    packages=["app","cli"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/tmukherjee13/passman",

    #
    # license="LICENSE.txt",
    description="A Simple Password Manager",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "django",
        "pyperclip",
        "argparse",
        "wsgiref"
    ],

    entry_points={
        'console_scripts': [
            'getpass = cli.passman:get',
            'setpass = cli.passman:set',
        ],
    },
)