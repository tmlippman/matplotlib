"""
Poor man's setuptools script...
"""

from setuptools import setup
exec(compile(open('setup.py').read(), 'setup.py', 'exec'),
         {'additional_params' :
          {'namespace_packages' : ['mpl_toolkits'],
           #'entry_points': {'nose.plugins':  ['KnownFailure =  matplotlib.testing.noseclasses:KnownFailure', ] }
           }})
