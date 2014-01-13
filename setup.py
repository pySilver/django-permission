# coding=utf-8
from setuptools import setup, find_packages

NAME = 'django-permission'
VERSION = '0.5.0'

def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as fi:
        return fi.read()

def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows]
    rows = filter(lambda x: x, rows)
    return rows

setup(
    name = NAME,
    version = VERSION,
    description = ('A enhanced permission system which enable logical permission'
                   'systems to complex permissions'),
    long_description = read('README.rst'),
    classifiers = (
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ),
    keywords = 'django object logical permission auth authentication',
    author = 'Alisue',
    author_email = 'lambdalisue@hashnote.net',
    url = 'https://github.com/lambdalisue/%s' % NAME,
    download_url = ('https://github.com/lambdalisue/%s/'
                    'tarball/master') % NAME,
    license = 'MIT',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    exclude_package_data = {'': 'README.rst'},
    zip_safe=True,
    install_requires=readlist('requirements.txt'),
    test_suite='runtests.runtests',
    tests_require=readlist('requirements-test.txt'),
)
