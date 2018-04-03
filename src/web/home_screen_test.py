import unittest

from src.bases.test_base import TestBase

class HomeScreenTest(TestBase):
    
    def loadIndex(self):
        pass

if __name__ == "__main__":
    SUITE = unittest.TestLoader().loadTestsFromTestCase(HomeScreenTest)
    unittest.TextTestRunner(verbosity=2).run(SUITE)