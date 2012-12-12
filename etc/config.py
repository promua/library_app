from os.path import realpath, normpath, dirname, join

#current dir
currdir = realpath(dirname(__file__))
#app root dir
approot = normpath(join(currdir, ".."))


class Container: pass

#base class for misc config profiles
class Profile:
	def __init__(self):
		self.db = Container()
		self.db.url = "sqlite:///%s/var/db/libapp.db" % approot
	
	
#production profile
production = Profile()

testing = Profile()
testing.db.url = "sqlite:///"

#default config entry point
profile = production
