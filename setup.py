from setuptools import setup, find_packages

setup(
    name="ft8decoder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "ft8decoder = ft8decoder.cli:main",
        ]
    }
)