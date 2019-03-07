try:
    from setuptools import setup
except ImportError as err:
    print("Missing Python module requirement: setuptools.")
    raise err

import sys
if sys.version_info < (3 , 6):
    print("TabPy requires python version >= 3.6.5.  Detected")
    print(sys.version)
    raise Exception("Python Version Not Supported")

from tabpy_server import __version__

setup(
    name='tabpy-server',
    python_requires='>=3.6.5',
    version=__version__,
    description='Web server Tableau uses to run Python scripts.',
    url='https://github.com/tableau/TabPy',
    author='Tableau',
    author_email='github@tableau.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    packages=['tabpy_server',
              'tabpy_server.common',
              'tabpy_server.management',
              'tabpy_server.psws',
              'tabpy_server.static'],
    package_data={'tabpy_server.static': ['*.*'],
                  'tabpy_server': ['startup.*', 'state.ini']},
    license='MIT',
    install_requires=[
        'backports_abc',
        'cloudpickle',
        'configparser',
        'decorator',
        'future',
        'genson',
        'jsonschema~=2.3.0',
        'mock',
        'numpy',
        'python-dateutil',
        'pyOpenSSL',
        'requests',
        'singledispatch',
        'simplejson',
        'six',
        'tornado==5.1.1',
        'Tornado-JSON',
        'urllib3'
    ]
)
