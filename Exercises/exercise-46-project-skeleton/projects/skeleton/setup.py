try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    pass
config = {
        'description': 'My Project',
        'author': 'My Name',     
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'My_email',
        'version': '0.1',
        'install_requires': ['pytest'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
        }

setup(**config)
