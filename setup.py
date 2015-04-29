import os
import sys

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

import leaf

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-leaf',
    version=leaf.__version__,
    author='Ryan Senkbeil',
    author_email='ryan.senkbeil@gsdesign.com',
    description='Render and serve django templates based on URL.',
    long_description=readme,
    packages=['leaf'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django-mptt >=0.7.2, <1.8',
        'six',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
