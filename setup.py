from setuptools import setup, find_packages

setup(
    name="pykiller",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "pygame"
    ],
)
