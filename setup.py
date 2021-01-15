import sys

if (2, 7) != sys.version_info[:2] < (3, 5):
    print("This mycobot version requires Python2.7, 3.5 or later.")
    sys.exit(1)

import setuptools

long_description = '''
# 2021.1.9

Fix the API problem that `is_moving()` and other methods of mycobot cannot be used.

# 2021.1.8

Python API add new methods:

- `jog_angle()`
- `jog_coord()`
- `jog_stop()`

# 2020.12.30

Adding usage documents to Python API.

# 2020.12.29

Python API supports python2.7

Modify the serial port to manual setting, support the use of window.

'''

setuptools.setup(
    name="pymycobot",
    version="0.0.1",
    author="Zachary Zhang",
    author_email="lijun.zhang@elephantrobotics.com",
    description="Python API for myCobot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elephantrobotics/myCobot/tree/main/API/Python",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pyserial'],
    python_requires= '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, != 3.4.*',
)

