#!/usr/bin/env python

from setuptools import find_packages, setup


def get_requirements(filename='requirements.txt'):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]


if __name__ == '__main__':
    setup(
        name='realesrgan',
        version='0.3.0',  # Set a static version number
        description='Real-ESRGAN aims at developing Practical Algorithms for General Image Restoration',
        author='Xintao Wang',
        author_email='xintao.wang@outlook.com',
        url='https://github.com/xinntao/Real-ESRGAN',
        packages=find_packages(exclude=('tests', 'docs')),
        install_requires=get_requirements(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        license='BSD-3-Clause License',
        zip_safe=False,
    )
