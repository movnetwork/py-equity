from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

with open("requirements.txt", "r") as _requirements:
    requirements = list(map(str.strip, _requirements.read().split("\n")))[:-1]

setup(
    name="py-equity",
    version='0.1.0',
    description='Python wrapper around the eqt Equity compiler.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='AGPLv3+',
    author='Meheret Tesfaye',
    author_email='meherett@zoho.com',
    url='https://github.com/mehetett/py-equity',
    packages=find_packages(),
    python_requires=">=3.5,<4",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
)
