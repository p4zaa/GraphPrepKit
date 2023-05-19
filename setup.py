from setuptools import setup, find_packages

setup(
    name='GraphPrepKit',
    version='0.1',
    description='A powerful and versatile graph preprocessing library designed to simplify and streamline the data preparation phase for graph-based applications.',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
)
