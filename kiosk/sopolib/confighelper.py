import configparser
from configparser import SafeConfigParser

class SopoConfig(SafeConfigParser):

	sources = ['/etc/sopo.conf', '~/.sopo.conf']

	def __init__(self):
		super(SafeConfigParser, self).__init__()
		self.read(self.sources)
