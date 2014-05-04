import configparser
from configparser import ConfigParser

class SopoConfig(ConfigParser):

	sources = ['/etc/sopo.conf', '~/.sopo.conf']

	def __init__(self):
		super().__init__()
		self.read(self.sources)
