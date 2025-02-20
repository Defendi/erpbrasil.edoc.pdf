#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='erpbrasil.edoc.pdf',
    version='1.0.3',
    license='MIT',
    description='Impressão de documentos fiscais a partir do XML: NF-E, NFC-E, CT-E, MDF-E, GNRE e etc.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='KMEE',
    author_email='dev@kmee.com.br',
    url='https://github.com/erpbrasil/erpbrasil.edoc.pdf',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    namespace_packages=["erpbrasil", "erpbrasil.edoc"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    # project_urls={
    #     'Documentation': 'https://erpbrasiledocpdf.readthedocs.io/',
    #     'Changelog': 'https://erpbrasiledocpdf.readthedocs.io/en/latest/changelog.html',
    #     'Issue Tracker': 'https://github.com/erpbrasil/erpbrasil.edoc.pdf/issues',
    # },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.5, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        'click',
        'erpbrasil.base',
        'genshi',
        'reportlab>=3.5',
        'lxml',
        'py3o.template',
        'sh',
        'python-dateutil',
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    entry_points={
        'console_scripts': [
            'erpbrasil-edoc-pdf = erpbrasil.edoc.pdf.cli:main',
        ]
    },
)
