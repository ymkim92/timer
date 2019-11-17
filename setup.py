from setuptools import setup, find_packages

setup(name='timer',
    scripts=['bin/pytimer'],
    version='0.1',
    description='Simple timer working in Linux',
    author='Youngmin Kim',
    author_email='ymkim92@gmail.com',
    license='WTFPL',
    packages=find_packages(),
    install_requires=[
    ],
)