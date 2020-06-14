import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-madusonovidiusscrumy',
	version='0.1',
	packages=find_packages(),
	include_package_data=True,
	license='BSD License',
	description='A simple Django app',
	long_description=README,
	url='https://www.example.com',
	author='Madu Chika',
	author_email='cmadu42@yahoo.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Framework :: Django :: X.Y',
		'Intended Audience :: OS Independent',
		'Licence :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.8',
		'Topic :: Internet :: WWW/HTTP',
		'TOPIC :: Internet :: WWW/HTTP :: Dynamic Content'

	],
)