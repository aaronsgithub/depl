from setuptools import find_packages, setup
from depl import __version__

setup(
    name="depl",
    version=__version__,
    packages=find_packages(),
    author="Aaron Ghani",
    author_email="sendaaronstuff@outlook.com",
    description="Super easy remote compute",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aaronsgithub/depl",
    python_requires=">=3.8",
    entry_points={"console_scripts": ["depl=depl.depl:main"]},
)
