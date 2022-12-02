from setuptools import setup

setup(
    name='logger',
    version='0.1.0',
    py_modules=['logger'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'logger = logger:log',
        ],
    },
)

