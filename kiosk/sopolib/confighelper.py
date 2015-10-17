import configparser
from configparser import SafeConfigParser
import os

class SopoConfig(SafeConfigParser):

	sources = ['/etc/sopo.conf', os.path.expanduser('~/.sopo.conf')]

	def __init__(self):
		super(SafeConfigParser, self).__init__()
		self.read(self.sources)
