from setuptools import setup

setup(
    name='todo-api',
    packages=['todo_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restful',
    ]
)
