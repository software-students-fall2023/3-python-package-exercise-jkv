# test_moon_phase.py
import unittest
from unittest.mock import patch
from package import moon_phrases

#from package.moon_phases import get_type, get_compatability, get_personality, get_life_suggestion
import datetime

class TestMoonPhase(unittest.TestCase):

    @patch('builtins.input', return_value='2020,6,21')
    def test_get_type_new_moon(self, mock_input):
        # This will replace input() with a mock that returns '2020,6,21'
        expected_phase = 'New Moon'  # Expected phase for the mocked date
        result_phase = get_type()
        self.assertEqual(result_phase, expected_phase)

    @patch('builtins.input', return_value='2017,2,18')
    def test_get_type_third_quarter(self, mock_input):
        expected_phase = 'Third Quarter'
        result_phase = get_type()
        self.assertEqual(result_phase, expected_phase)

    @patch('builtins.input', return_value='2010,5,18')
    def test_get_type_waxing_crescent(self, mock_input):
        expected_phase = 'Waxing Crescent'
        result_phase = get_type()
        self.assertEqual(result_phase, expected_phase)

   
    def test_get_compatability_new_moon(self):
        phase = 'New Moon'
        expected_output = "Full Moon is most compatable with you! The dreamer (new moon) and the doer (full moon) often balance each other out—but the full moon's high-energy vibe could also overpower the new moon's calmer, meditative nature."
        self.assertEqual(get_compatability(phase), expected_output)

    def test_get_compatability_third_quarter(self):
        phase = 'Third Quarter'
        expected_output = "First Quarter is most compatable with you! The activist (first quarter) and the philosopher (third quarter) both have a high tolerance for tension and may lean into conflict. But while the first quarter seeks to produce external change, the third is primarily working through an internal change of heart."
        self.assertEqual(get_compatability(phase), expected_output)

    def test_get_compatability_waxing_crescent(self):
        phase = 'Waxing Crescent'
        expected_output = "Waning Gibbous is most compatable with you! The rising star (waxing crescent) and the mentor (waning gibbous) share a preference for growth and ease. But in some cases, the thoughtful waning gibbous could grow frustrated with the waxing crescent's carefree curiosity and spontaneity."
        self.assertEqual(get_compatability(phase), expected_output)

    def test_get_personality_waxing_crescent(self):
        phase = 'Waxing Crescent'
        expected_output = 'High ambition, Very productive, Disinclined to risks'
        self.assertEqual(get_personality(phase), expected_output)

    def test_get_personality_third_quarter(self):
        phase = 'Third Quarter'
        expected_output = "Faithful, Emotional, Devoted"
        self.assertEqual(get_personality(phase), expected_output)

    def test_get_personality_new_moon(self):
        phase = 'New Moon'
        expected_output = 'Good creativity, Adventure seeker, Spontaneous and rash'
        self.assertEqual(get_personality(phase), expected_output)

    def test_get_life_suggestion_waxing_crescent(self):
        phase = 'Waxing Crescent'
        expected_output = "The waxing crescent phase follows the new moon, and it's visually characterized by a thin sliver of illumination on the right side of the moon. This phase symbolizes growth, intention, and hope, setting the stage for what you wish to achieve in the coming lunar cycle. It's best for taking initial steps towards the goals set during the New Moon. Focus on building, growth, and laying down roots."
        self.assertEqual(get_life_suggestion(phase), expected_output)

    def test_get_life_suggestion_third_quarter(self):
        phase = 'Third Quarter'
        expected_output = "The Last Quarter Moon appears as another half-lit sphere, but this time with the left side illuminated and the right side in shadow. It symbolizes a time of reflection, reassessment, and forgiveness. It's a period to release remaining burdens and prepare for a new beginning. It's best for reflecting on the past cycle, forgiving yourself and others, and letting go of remaining burdens."
        self.assertEqual(get_life_suggestion(phase), expected_output)

    def test_get_life_suggestion_new_moon(self):
        phase = 'New Moon'
        expected_output = "This phase is an excellent time to plant metaphorical seeds, set goals for the future, and align with your deepest desires and dreams. The New Moon invites you to embrace new paths and possibilities, offering a fresh slate to write the next chapter of your life. It's best for setting new intentions, planting metaphorical seeds, and beginning new projects. A time for renewal and fresh starts."
        self.assertEqual(get_life_suggestion(phase), expected_output)

    def test_get_compatibility_invalid_phase(self):
        invalid_phase = 'No Moon'  # An example of an invalid phase
        expected_output = "Invalid moonphase"  # Expected error message for an invalid phase
        result = get_compatability(invalid_phase)
        self.assertEqual(result, expected_output, f"Expected error message for an invalid phase. Instead, it returned '{result}'")

    def test_get_life_suggestion_invalid_phase(self):
        invalid_phase = 'No Moon'  # An example of an invalid phase
        expected_output = "Invalid moonphase"  # Expected error message for an invalid phase
        result = get_compatability(invalid_phase)
        self.assertEqual(result, expected_output, f"Expected error message for an invalid phase. Instead, it returned '{result}'")
    
    def test_get_personality_invalid_phase(self):
        invalid_phase = 'No Moon'  # An example of an invalid phase
        expected_output = "Invalid moonphase"  # Expected error message for an invalid phase
        result = get_compatability(invalid_phase)
        self.assertEqual(result, expected_output, f"Expected error message for an invalid phase. Instead, it returned '{result}'")
