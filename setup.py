from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Error Cats',
    version='0.1.0',
    url='https://github.com/Behoston/error-cats',
    license='MIT',
    author='Behoston',
    author_email='mlegiecki@gmail.com',
    description='Extension to return cats! Works with Flask and Sanic.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['error_cats'],
    include_package_data=True,
    setup_requires=[
        'flake8',
        'isort',
    ],
    tests_require=[
        'flake8',
        'pytest',
        'flask',
        'sanic',
        'sanic_testing',
        'aiohttp',
    ],
    platforms='any',
    python_requires='>=3',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
