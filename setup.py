from setuptools import setup
from setuptools import find_packages

"""Packaging tool for the Yeti python bindings and CLI utility."""

from setuptools import setup
from setuptools import find_packages

"""Returns contents of README.md."""
with open("README.md", "r", encoding="utf-8") as readme_fp:
    long_description = readme_fp.read()

setup(
    name="suricata_misp",
    version="1.0",
    description="Import indicators of MISP to dataset Suricata and add sightings in MISP on this indicators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
    ],
    keywords="misp suricata datasets",
    url="https://github.com/sebdraven/suricata_misp",
    author="Sebastien Larinier @Sebdraven",
    license="Apache",
    packages=["suricata_misp", "scripts"],
    install_requires=[
        "pymisp",
        "redis",
        "tailer",
    ],
    entry_points={
        "console_scripts": ["suricata_misp=scripts.suricata_misp:main"],
    },
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=False,
)