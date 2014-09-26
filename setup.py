import setuptools
import codecs
import os

here = os.path.abspath( os.path.dirname( __file__ ) )

with codecs.open( os.path.join( here, "DESCRIPTION.rst" ), encoding = "utf-8" ) as f:
	long_description = f.read()

setuptools.setup(

	name = "dnspod-int-to-swagger",
	version = "0.1.0",
	description = "Convert DNSPod International API Documents to Swagger",

	long_description = long_description,

	url = "https://github.com/aucampia/dnspod-int-swagger",

	author = "Iwan Aucamp",
	author_email = "aucampia@gmail.com",

	maintainer = "Iwan Aucamp",
	maintainer_email = "aucampia@gmail.com",

	license = "...",

	classifiers=[
			"Development Status :: 3 - Alpha",
			"Environment :: Console",
			"Intended Audience :: Developers",
			"Intended Audience :: Information Technology",
			"Natural Language :: English",
			"Programming Language :: Python",
			"Programming Language :: Python :: 3",
			"Programming Language :: Python :: 3.4",
			"Topic :: Documentation",
			"Topic :: Internet",
			"Topic :: Internet :: Name Service (DNS)",
                        "Topic :: Other/Nonlisted Topic",
			"Topic :: Software Development",
                        "Topic :: Software Development :: Code Generators",
                        "Topic :: Software Development :: Documentation",
                        "Topic :: Software Development :: Interpreters",
                        "Topic :: Software Development :: Pre-processors",
			"Topic :: Text Processing",
                        "Topic :: Text Processing :: Markup"
	],

	keywords="dns dnspod swagger restructuredtext converter",

	package_dir = { "" : "src" },

	#packages = setuptools.find_packages( where=".", exclude=[], include=[ "*" ] ),
	packages = [ "dnspod-int-to-swagger" ],

	entry_points = {
		"console_scripts": [
			"dnspod-cli = dnspod-int-to-swagger.main:main",
		]
	}

)

