# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="DRodriguez615-lambdata-pt4",
    version="1.1",
    author="Damon Rodriguez",
    author_email="drjrodriguez615@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/DRodriguez615/DRodriguez615-lambdata-pt4",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)