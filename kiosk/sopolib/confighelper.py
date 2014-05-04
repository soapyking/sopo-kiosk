import configparser
from configparser import SafeConfigParser

class SopoConfig(SafeConfigParser):

	sources = ['/etc/sopo.conf', '~/.sopo.conf']

	def __init__(self):
		super().__init__()
		self.read(self.sources)
