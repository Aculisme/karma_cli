from setuptools import setup
setup(
    name = 'karma_cli',
    version = '0.1.0',
    author="Aculisme",
    author_email="luca.mehl@gmail.com",
    description="This is a test CLI for mass-voting on Reddit",
    keywords="praw reddit botnet cli karma mass-voting bots ",
    url="https://github.com/Aculisme/karma_cli",
    packages = ['karma_cli'],
    entry_points = {
        'console_scripts': [
            'karma_cli = karma_cli.__main__:main'
        ]
    })