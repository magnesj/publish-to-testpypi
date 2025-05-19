"""
Tests for the core module.
"""

import unittest
from minimal_package.core import greet

class TestCore(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, World!")
        
    def test_greet_custom(self):
        self.assertEqual(greet("PyPI"), "Hello, PyPI!")

if __name__ == "__main__":
    unittest.main()