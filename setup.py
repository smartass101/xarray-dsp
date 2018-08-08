from setuptools import setup

setup(
    name='xarray-dsp',
    description='xarray-compatible digital signal processing tools',
    version='0.2',
    packages=['xarray_dsp'],
    requires=[
        'numpy',
        'scipy',
        'xarray>=0.9.0'
    ],
    author='Ondrej Grover',
    author_email='ondrej.grover@gmail.com',
)
