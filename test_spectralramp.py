# test_spectralramp.py
"""
Tests for SpectralRamp module.
"""

import unittest
from spectralramp import SpectralRamp

class TestSpectralRamp(unittest.TestCase):
    """Test cases for SpectralRamp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SpectralRamp()
        self.assertIsInstance(instance, SpectralRamp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SpectralRamp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
