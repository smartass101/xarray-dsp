from setuptools import setup

setup(
    name='xarray-compatible digital signal processing tools',
    version='0.1',
    packages=['xarray_dsp'],
    requires=[
        'numpy',
        'scipy',
        'xarray'
    ],
    author='Ondrej Grover',
    author_email='ondrej.grover@gmail.com',
)
