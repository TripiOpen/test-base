import unittest

from bases import TestBase

class HomeScreenTest(TestBase):
    def loadIndex(self):
        self.load_page("https://www.tripi.vn/")

if __name__ == "__main__":
    SUITE = unittest.TestLoader().loadTestsFromTestCase(HomeScreenTest)
    unittest.TextTestRunner(verbosity=2).run(SUITE)