# My skeleton project

This exercise only about make a skeleton of any project.

Before go to exercise here are the few new tools:

**1. virtualenv**

virtualenv use it to create a “fake” Python installation, which makes it easier to manage versions of your packages for different projects. 

Step to install and run:
1. Check if already install `pip list`.
2. Install:
    ```sh
    sudo pip install virtualenv
    ```
3. Check `whereis virtualenv`
4. Make directory in home
    ```bash
    $ mkdir ~/.venvs
    ```
5. Run virtualenv and tell it to include the system site packages, then instruct it to build the virtualenv in ~/.venvs/lpthw.
    ```bash
    $ virtualenv --system-site-packages ~/.venvs/lpthw
    ```
6. using . operator then put ~/.venvs/lpthw/bin/activate script, prompt changes to (lpthw).
    ```bash
    $ . ~/.venvs/lpthw/bin/activate
    (lpthw) $
    ```

**2. pytest**

In book, `nose` was used but it not working above python3 version so `pytest` works better. Both nose and pytest are similar work.

It's the testing framework that simplifies writing, running, and debugging tests for Python code.

Step to install and run:
1. Install
    ```bash
    pip install pytest
    ```
2. Run in Project directory
    ```bash
    pytest
    ```

## Creating the Skeleton Project directory

1. Structure of skeleton directory
    ```sh
    mkdir -p projects/skeleton/{bin,NAME,tests,docs}
    ```
    - NAME will be renamed to projcets main module.
2. Initial files.
    ```sh
    touch NAME/__init__.py tests/__init__.py
    ```
3. Create a setup.py in skeleton dir:
    ```py
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
    ```
    Edit this file so that it has your contact information and is ready to go for when you copy it.
4. Finally, a simple skeleton file for tests named tests/NAME_tests.py
    ```py
    import NAME

    def setup():
        print("SETUP!")

    def teardown():
        print("TEAR DOWN!")

    def test_basic():
        print("I RAN!")
    ```

**Overall Final Directory Structure**
```
skeleton/
    NAME/
        __init__.py
    bin/
    docs/
    setup.py
    tests
        NAME_tests.py
        __init__.py
```

Then Try `pytest`.

## Using the Skeleton
You are now done with most of your yak shaving. Whenever you want to start a new project, just do this:
1. Make a copy of your skeleton directory. Name it after your new project.
2. Rename (move) the NAME directory to be the name of your project or whatever you want to call your root module.
3. Edit your setup.py to have all the information for your project.
4. Rename tests/NAME_tests.py to also have your module name.
5. Double check it’s all working by using nosetests again.
6. Start coding.