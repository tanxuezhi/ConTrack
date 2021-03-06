#!/usr/bin/env python

from setuptools import setup, find_packages


with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name="ConTrack",
    version="0.1.0",
    description="Contour Tracking of circulation anomalies in Weather and Climate Data.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="steidani",
    author_email="daniel.steinfeld@alumni.ethz.ch",
    url="https://github.com/steidani/ConTrack",
    packages=find_packages(exclude=("tests", "docs")),
    python_requires=">=3.6",
    install_requires=open("requirements.txt").read().split(),
    classifiers=[
        "Programming Language :: Python :: 3",
	"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["data", "science", "meteorology", "climate", "atmospheric blocking", "troughs and ridges"]
)
