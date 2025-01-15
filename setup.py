from setuptools import setup

setup(
    name="pykiller",
    version="0.2",  # Increment the version
    packages=["pykiller"],
    long_description="PYKILLER is a stress-testing tool that simulates extreme system conditions to test stability and performance under heavy loads. Use responsibly in isolated, non-production environments. .",
    long_description_content_type="text/x-rst",  # or 'text/markdown' based on your file type
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
