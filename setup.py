try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
	'description' : 'A crappy blackjack game',
	'author' : 'David Godow',
	'url' : 'https://github.com/nonpapa',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : [],
	'py_modules' : [],
	'scripts' : [],
	'name' : 'blackjack'}

setup(**config)