from setuptools import setup, Extension

# Define the extension module
xdelta3_extension = Extension(
    name='xdelta3._xdelta3',  # Module name, including package
    sources=['xdelta3/_xdelta3.c'],  # Path to the C source file
    include_dirs=['/usr/local/include'],  # Modify as needed
    libraries=['xdelta3'],  # Libraries to link against
    library_dirs=['/usr/local/lib'],  # Modify as needed
    extra_compile_args=['-std=c99'],  # Additional compile arguments if necessary
    extra_link_args=[]  # Additional linker arguments if necessary
)

# Setup script
setup(
    name='py-xdelta3',
    version='0.3.2',
    description='Modern Python wrapper around xdelta3',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Guilherme M. Miranda, Samuel Colvin',
    author_email='alchemist.software@proton.me, s@muelcolvin.com',
    url='https://github.com/elf-alchemist/py-xdelta3',
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
    packages=['xdelta3'],
    ext_modules=[xdelta3_extension],
)
