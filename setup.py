from setuptools import setup, find_packages

setup(
    name='sg-mongodb-migrations',
    version='0.1.0',
    description='A database migration tool for MongoDB forked from David Xie\'s mongodb-migrations',
    long_description=__doc__,
    url='https://github.com/solusguard/mongodb-migrations',
    author='Joel Rathgaber',
    author_email='joel@solusguard.com',
    license='GPLv3',
    packages=find_packages(),
    platforms='any',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pymongo>=3.2.1',
        'configparser>=3.5.0'
    ],
    entry_points={
        'console_scripts': ['mongodb-migrate=mongodb_migrations.cli:main'],
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
