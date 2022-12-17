import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))

def read_file(filename: str) -> str:
    with open(os.path.join(this_dir, filename), encoding='utf-8') as f:
        return f.read()

def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(
    name='balderich',
    python_requires='>=3.8.0',
    version='1.1',
    keywords='NSSCTF Balderich',
    description='A Python library for the NSSCTF Balderich API',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    license='MIT License',
    url='https://github.com/NSSCTF/balderich-py',
    author='Xenny',
    author_email='xennyxd1@gmail.com',
    packages=find_packages('.'),
    include_package_data=True,
    platforms='any',
    install_requires=read_requirements('requirements.txt'),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)