import os
from setuptools import find_packages, setup

with open(os. path. join(os. path. dirname(__file__), ' README.rst' )) as readme:
	README = readme. read()
	os. chdir(os. path. normpath(os. path. join(os. path. abspath(__file__), os. pardir)))
setup(
	name=' Todolist' ,
	version=' 0.1' ,
	packages=find_packages(),
	include_package_data=True,
	license=' BSD License' , # example license
	description='Todolist' ,
	long_description=README,
	url='' ,
	author='Hola Nguyen' ,
	author_email=' kevinhoa95@gmail.com' ,
	classifiers=[
	' Environment :: Web Environment' ,
	' Framework :: Django' ,
	' Framework :: Django :: 1.10' , # replace "X.Y" as appropriate
	' Intended Audience :: Developers' ,
	' License :: OSI Approved :: BSD License' , # example license
	' Operating System :: OS Independent' ,
	' Programming Language :: Python' ,
	' Programming Language :: Python :: 3.5' ,
	' Programming Language :: Python :: 3.6' ,
	' Topic :: Internet :: WWW/HTTP' ,
	' Topic :: Internet :: WWW/HTTP :: Dynamic Content' ,
	],
)