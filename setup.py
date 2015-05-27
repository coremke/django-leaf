import os

from codecs import open
from setuptools import setup

import leaf

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-leaf',
    version=leaf.__version__,
    author='Ryan Senkbeil',
    author_email='ryan.senkbeil@gsdesign.com',
    description='Render and serve django templates based on URL.',
    long_description=long_description,
    url='https://github.com/gsmke/django-leaf',
    license='BSD',
    packages=['leaf'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django-mptt >=0.7.2, <1.8',
        'six',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
