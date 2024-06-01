from importlib.machinery import SourceFileLoader
from setuptools import setup, Extension
from pathlib import Path

dir = Path(__file__).resolve().parent
long_description = dir.joinpath('README.md').read_text()

version = SourceFileLoader('version', 'xdelta3/version.py').load_module()

package = dir.joinpath('xdelta3')
package_data = ['_xdelta3.c']
if package.joinpath('lib').exists():
    package_data += ['lib/' + f.name for f in package.joinpath('lib').iterdir()]

setup(
    name='xdelta3',
    version=str(version.VERSION),
    description='Modern Python wrapper around xdelta3',
    long_description=long_description,
    author='Guilherme M. Miranda',
    author_email='alchemist.software@proton.me',
    url='https://github.com/elf-alchemist/py-xdelta3',
    license='Apache License, Version 2.0',
    packages=['xdelta3'],
    package_data={ 'xdelta3': package_data },
    zip_safe=True,
    ext_modules=[
        Extension(
            '_xdelta3',
            sources=['xdelta3/_xdelta3.c'],
            include_dirs=['./xdelta3/lib'],
            define_macros=[
                ('SIZEOF_SIZE_T', '8'),
                ('SIZEOF_UNSIGNED_LONG_LONG', '8'),
                ('XD3_USE_LARGEFILE64', '1'),
            ]
        )
    ],
	classifiers=[
		"Development Status :: 4 - Beta",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: Unix",
		"Operating System :: POSIX :: Linux",
		"Topic :: System :: Archiving :: Compression",
	],
)
