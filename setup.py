from setuptools import *

with open('requirements.txt') as f_required:
    required = f_required.read().splitlines()
with open("readme.md", "r") as fh:
    long_description = fh.read()
with open("version.txt", "r") as fh:
    vers = fh.read().splitlines()[0]

setup(
	name='gskymongofactory',
	version=vers,
	py_modules=['gskymongofactory'],
	packages=find_packages(),
	install_requires=required,
	long_description=long_description,
    long_description_content_type="text/markdown",
	author="graboskyc",
	author_email="chris@grabosky.net",
	description="Sample mongo connection library with all the bells and whistles as a learning experiment.",
    url="https://github.com/graboskyc/MongoDBConnectorBandWs",
)