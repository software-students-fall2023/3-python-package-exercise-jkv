# test_moon_phase.py
import unittest
from unittest.mock import patch
from package.moon_phase import get_type, get_compatability, get_personality, get_life_suggestion
import datetime

class TestMoonPhase(unittest.TestCase):

    @patch('builtins.input', return_value='2020,6,21')
    def test_get_type(self, mock_input):
        # This will replace input() with a mock that returns '2020,6,21'
        expected_phase = 'New Moon'  # Expected phase for the mocked date
        result_phase = get_type()
        self.assertEqual(result_phase, expected_phase)

    def test_get_compatability():
        phase = 'Full Moon'
        expected_output = 'New Moon is most compatable with you! The dreamer (new moon) and the doer (full moon) often balance each other out—but the full moon's high-energy vibe could also overpower the new moon's calmer, meditative nature.' # expected output
        self.assertEqual(get_compatability(phase), expected_output)
    
    def test_get_personality():
        phase = 'Waxing Crescent'
        expected_output = 'High ambition, Very productive, Disinclined to risks'
        self.assertEqual(get_personality(phase), expected_output)
    
    def test_get_life_suggestion():
        phase = 'Waxing Crescent'
        expected_output = "The waxing crescent phase follows the new moon, and it's visually characterized by a thin sliver of illumination on the right side of the moon. This phase symbolizes growth, intention, and hope, setting the stage for what you wish to achieve in the coming lunar cycle. It's best for taking initial steps towards the goals set during the New Moon. Focus on building, growth, and laying down roots."
        self.assertEqual(get_life_suggestion(phase), expected_output)
       
