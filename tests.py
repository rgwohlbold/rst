import unittest

loader = unittest.TestLoader()
tests = loader.discover("rst/")
runner = unittest.TextTestRunner(verbosity=2).run(tests)