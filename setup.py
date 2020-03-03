import setuptools


setuptools.setup(
    name="swapi-sdk-lykata", # Replace with your own username
    version="0.0.1",
    author="Samuel Lindgren",
    author_email="samuel@dyna.mo",
    description="A Python SDK for StarWars API",
    long_description="A Python SDK for StarWars API",
    long_description_content_type="text/markdown",
    url="https://github.com/lykata/python_swapi_sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)