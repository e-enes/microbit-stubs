from setuptools import setup, find_packages

setup(
    name="microbit-stubs",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Enes Tahiri",
    author_email="contact@enes.gg",
    description="Python stubs for micro:bit modules",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/e-enes/microbit-stubs",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
