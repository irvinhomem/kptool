from setuptools import setup, find_packages
import sys, os


sys.path.append('./tests')


#-----------------------------------------------------------------------------
# Main setup
#-----------------------------------------------------------------------------

long_desc = \
"""
Keepass DB managing tool
-------------------------------------

This version can use Keepass v1 DB only.
This version can read DB only.
"""

version = '0.1'

setup(name='kptool',
      version=version,
      description = "Keepass v1 DB tool",
      long_description = long_desc, 
      classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
	'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Security',
        'Topic :: Utilities'
      ],
      keywords = ['security', 'password'],
      author = "WAKAYAMA Shirou",
      author_email = "shirou.faw@gmail.com",
      url='',
      license = "GPL v2",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'argparse', 'pycrypto'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      test_suite = 'tests.test'
      )