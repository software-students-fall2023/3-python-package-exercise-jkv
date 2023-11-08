# test_moon_phase_pytest.py
from unittest.mock import patch
from src.package import get_type, get_compatability, get_personality, get_life_suggestion
import pytest

@pytest.mark.parametrize("input_date,expected_phase", [
    ('2020,6,21', 'New Moon'),
    ('2017,2,18', 'Third Quarter'),
    ('2010,5,18', 'Waxing Crescent'),
])
def test_get_type(input_date, expected_phase):
    with patch('builtins.input', return_value=input_date):
        result_phase = get_type()
        assert result_phase == expected_phase

@pytest.mark.parametrize("phase,expected_output", [
    ('New Moon', "Full Moon is most compatable with you! The dreamer (new moon) and the doer (full moon) often balance each other out—but the full moon's high-energy vibe could also overpower the new moon's calmer, meditative nature."),
    ('Third Quarter', "First Quarter is most compatable with you! The activist (first quarter) and the philosopher (third quarter) both have a high tolerance for tension and may lean into conflict. But while the first quarter seeks to produce external change, the third is primarily working through an internal change of heart."),
    ('Waxing Crescent', "Waning Gibbous is most compatable with you! The rising star (waxing crescent) and the mentor (waning gibbous) share a preference for growth and ease. But in some cases, the thoughtful waning gibbous could grow frustrated with the waxing crescent's carefree curiosity and spontaneity."),
])
def test_get_compatability(phase, expected_output):
    assert get_compatability(phase) == expected_output

@pytest.mark.parametrize("phase,expected_output", [
    ('Waxing Crescent', 'High ambition, Very productive, Disinclined to risks'),
    ('Third Quarter', "Faithful, Emotional, Devoted"),
    ('New Moon', 'Good creativity, Adventure seeker, Spontaneous and rash'),
])
def test_get_personality(phase, expected_output):
    assert get_personality(phase) == expected_output

@pytest.mark.parametrize("phase,expected_output", [
    ('Waxing Crescent', "The waxing crescent phase follows the new moon, and it's visually characterized by a thin sliver of illumination on the right side of the moon. This phase symbolizes growth, intention, and hope, setting the stage for what you wish to achieve in the coming lunar cycle. It's best for taking initial steps towards the goals set during the New Moon. Focus on building, growth, and laying down roots."),
    ('Third Quarter', "The Last Quarter Moon appears as another half-lit sphere, but this time with the left side illuminated and the right side in shadow. It symbolizes a time of reflection, reassessment, and forgiveness. It's a period to release remaining burdens and prepare for a new beginning. It's best for reflecting on the past cycle, forgiving yourself and others, and letting go of remaining burdens."),
    ('New Moon', "This phase is an excellent time to plant metaphorical seeds, set goals for the future, and align with your deepest desires and dreams. The New Moon invites you to embrace new paths and possibilities, offering a fresh slate to write the next chapter of your life. It's best for setting new intentions, planting metaphorical seeds, and beginning new projects. A time for renewal and fresh starts."),
])
def test_get_life_suggestion(phase, expected_output):
    assert get_life_suggestion(phase) == expected_output

@pytest.mark.parametrize("invalid_phase,expected_output", [
    ('No Moon', "Invalid moonphase"),
])
def test_invalid_phase_responses(invalid_phase, expected_output):
    assert get_compatability(invalid_phase) == expected_output
    assert get_life_suggestion(invalid_phase) == expected_output
    assert get_personality(invalid_phase) == expected_output
