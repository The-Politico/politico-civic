import os

from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='politico-civic',
    version='0.1.0',
    packages=find_packages(exclude=('', 'docs',)),
    include_package_data=True,
    url='https://github.com/The-Politico/politico-civic',
    license='MIT',
    description='A Django project for collecting civic data.',
    python_requires='>=3',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'celery',
        'djangorestframework',
        'flake8',
        'fabric3',
        'jinja2',
        'psycopg2',
        'dj-database-url',
        'whitenoise',
        'django-environ',
        'social-auth-core',
        'social-auth-app-django',
        'sphinx',
        'sphinxcontrib-django',
        'sphinx-rtd-theme',
        'politico-civic-election-night',
        'politico-civic-entity',
        'politico-civic-geography',
        'politico-civic-government',
        'politico-civic-election',
        'politico-civic-biography',
        'politico-civic-stump',
        'politico-civic-demography',
        'politico-civic-almanac',
    ],
    entry_points='''
        [console_scripts]
        onespot=onespot:cli
    '''
)
