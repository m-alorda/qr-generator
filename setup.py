from setuptools import find_packages, setup

setup(
    name="QR Generator",
    version="1.0",
    description="CLI Wrapper for qrcode",
    author="m-alorda",
    author_email="miguel.alorda.cantero@gmail.com",
    packages=find_packages(exclude=["example"]),
)
