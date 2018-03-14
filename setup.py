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
        'git+ssh://git@github.com/The-Politico/politico-civic-entity#egg=entity',
        'git+ssh://git@github.com/The-Politico/politico-civic-geography#egg=geography',
        'git+ssh://git@github.com/The-Politico/politico-civic-government#egg=government',
        'git+ssh://git@github.com/The-Politico/politico-civic-election#egg=election',
        'git+ssh://git@github.com/The-Politico/politico-civic-stump#egg=stump',
        'git+ssh://git@github.com/The-Politico/politico-civic-biography#egg=biography',
        'git+ssh://git@github.com/The-Politico/politico-civic-vote#egg=vote',
        'git+ssh://git@github.com/The-Politico/politico-civic-demography#egg=demography',
        'git+ssh://git@github.com/The-Politico/politico-civic-almanac#egg=almanac',
        'git+ssh://git@github.com/The-Politico/politico-civic-election-night#egg=electionnight'
    ]
)
