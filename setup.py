from setuptools import setup, find_packages

setup(
    name="TaigiTools",
    version="0.1.0",
    description="A description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Adamz0ne/TaigiTools",
    author="Your Name",
    author_email="ad1224am@gmail.com",
    license="Apache License 2.0",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "nemo_toolkit[all]>=1.10.0",
    ],
)