import datetime

#Source: https://www.omnicalculator.com/everyday-life/moon-phase
def get_type():
    # Prompt user for their date of birth
    user_input = input("Enter your date of birth (YYYY,MM,DD): ")
    
    # Split the input string into components and convert them to integers
    year, month, day = map(int, user_input.split(','))

    # Create a datetime.date object from the provided input
    user_date = datetime.date(year, month, day)
    
    # Calculate the number of days since a known new moon (e.g., 2000-01-06)
    last_nm = (user_date - datetime.date(2000, 1, 6)).days
    cycles = last_nm / 29.53058770576
    cycles = cycles - int(cycles)
    lunar_day = cycles * 29.53058770576

    if 0 < lunar_day <= 1:
        return "New Moon"
    elif 1 < lunar_day <= 6.382647:
        return "Waxing Crescent"
    elif 6.382647 < lunar_day <= 8.382647:
        return "First Quarter"
    elif 8.382647 < lunar_day <= 13.765294:
        return "Waxing Gibbous"
    elif 13.765294 < lunar_day <= 15.765294:
        return "Full Moon"
    elif 15.765294 < lunar_day <= 21.147941:
        return "Waning Gibbous"
    elif 21.147941 < lunar_day <= 23.147941:
        return "Last Quarter"
    elif 23.147941 < lunar_day <= 28.530588:
        return "Waning Crescent"
    elif 28.530588 < lunar_day <= 29.530588:
        return "New Moon"
    else:
        return "Invalid lunar day value"
      
# Source https://www.wellandgood.com/moon-phase-compatibility/
def get_compatability(moonphase):
  compatable_list = {
    "New Moon": "Full Moon is most compatable with you! The dreamer (new moon) and the doer (full moon) often balance each other out—but the full moon's high-energy vibe could also overpower the new moon's calmer, meditative nature.",
    "Full Moon": "New Moon is most compatable with you! The dreamer (new moon) and the doer (full moon) often balance each other out—but the full moon's high-energy vibe could also overpower the new moon's calmer, meditative nature.",
    "Waxing Crescent": "Waning Gibbous is most compatable with you! The rising star (waxing crescent) and the mentor (waning gibbous) share a preference for growth and ease. But in some cases, the thoughtful waning gibbous could grow frustrated with the waxing crescent's carefree curiosity and spontaneity.",
    "Waning Gibbous": "Waxing Crescent is most compatable with you! The rising star (waxing crescent) and the mentor (waning gibbous) share a preference for growth and ease. But in some cases, the thoughtful waning gibbous could grow frustrated with the waxing crescent's carefree curiosity and spontaneity.",
    "First Quarter" : "Third Quater is most campatable with you! The activist (first quarter) and the philosopher (third quarter) both have a high tolerance for tension and may lean into conflict. But while the first quarter seeks to produce external change, the third is primarily working through an internal change of heart.",
    "Third Quarter": "First Quarter is most compatable with you! The activist (first quarter) and the philosopher (third quarter) both have a high tolerance for tension and may lean into conflict. But while the first quarter seeks to produce external change, the third is primarily working through an internal change of heart.",
    "Waxing Gibbous": "Waning Crescent is most compatable with you! The thinker (waning crescent) and the coach (waxing gibbous) share an emphasis on transformation, but tensions could arise from the waning crescent's need for internal processing.",
    "Waning Crescent": "Waxing Gibbous is most compatable with you! The thinker (waning crescent) and the coach (waxing gibbous) share an emphasis on transformation, but tensions could arise from the waning crescent's need for internal processing."
  }
  if moonphase not in compatable_list:
      return "Invalid moonphase"
  return compatable_list[moonphase]

# Source: https://www.tiktok.com/@shirleywirleyyy/video/7220949870897614122?_r=1&_t=8h8vPvL1Ire
def get_personality(moonphase):
  personalities = {
    "New Moon": "Good creativity, Adventure seeker, Spontaneous and rash",
    "Full Moon": "Sentimental, Oversensitive, Confused",
    "Waxing Crescent": "High ambition, Very productive, Disinclined to risks",
    "Waning Gibbous": "Thoughtful, Evaluative, Judgemental",
    "First Quarter" : "Competent, Doer, Restless",
    "Third Quarter": "Faithful, Emotional, Devoted",
    "Waxing Gibbous": "Soothing, Caring, Stickler for perfection",
    "Waning Crescent": "Dreamy and comtemplative, Individualistic, Solitary"
  }
  if moonphase not in personalities:
      return "Invalid moonphase"
  return personalities[moonphase]

# Source: https://www.slownorth.com/blogs/journal/moon-phase-ritual-guide
def get_life_suggestion(moonphase):
  suggestions = {
    "New Moon": "This phase is an excellent time to plant metaphorical seeds, set goals for the future, and align with your deepest desires and dreams. The New Moon invites you to embrace new paths and possibilities, offering a fresh slate to write the next chapter of your life. It's best for setting new intentions, planting metaphorical seeds, and beginning new projects. A time for renewal and fresh starts.",
    "Full Moon": "The Full Moon is the phase when the entire face of the moon is illuminated. It symbolizes culmination, harvest, and celebration. This is the peak time for seeing the results of the intentions set during the New Moon, and it's a moment to honor what has come to fruition. It's best for celebrating achievements, embracing gratitude, and engaging in self-reflection. It's a time to honor yourself and others and give thanks for the blessings in your life.",
    "Waxing Crescent": "The waxing crescent phase follows the new moon, and it's visually characterized by a thin sliver of illumination on the right side of the moon. This phase symbolizes growth, intention, and hope, setting the stage for what you wish to achieve in the coming lunar cycle. It's best for taking initial steps towards the goals set during the New Moon. Focus on building, growth, and laying down roots.",
    "Waning Gibbous": "The Waning Gibbous Moon follows the Full Moon and represents the beginning of the moon's transition back to darkness. It symbolizes a time of release, gratitude, and introspection. This phase is about letting go of what no longer serves you and giving thanks for what you've learned. It's best for releasing and letting go of old patterns or habits, reflecting on lessons learned, and expressing gratitude.",
    "First Quarter" : "The First Quarter Moon appears as a half-lit sphere, with the right side illuminated and the left side in shadow. It symbolizes a time of action, decisions, and commitment. As intentions set during the New Moon begin to manifest, it's a period to reassess, make adjustments, and move forward with determination. It's best for taking action and overcoming obstacles. It's a time to make decisions and put in effort toward achieving goals.",
    "Third Quater": "The Last Quarter Moon appears as another half-lit sphere, but this time with the left side illuminated and the right side in shadow. It symbolizes a time of reflection, reassessment, and forgiveness. It's a period to release remaining burdens and prepare for a new beginning. It's best for reflecting on the past cycle, forgiving yourself and others, and letting go of remaining burdens.",
    "Waxing Gibbous": "The Waxing Gibbous Moon phase represents a time of refinement and preparation. As the Moon continues to grow, and more of its surface is illuminated, our focus shifts from initiating actions to perfecting them. This phase urges us to analyze our progress, make necessary adjustments, and hone our path towards our goals. It's a period to be diligent, detail-oriented, and mindful of the larger picture while remaining committed to our intentions. The Waxing Gibbous phase encourages us to be patient and persistent, as we prepare for the culmination of our efforts in the Full Moon. It's best for refinement and fine-tuning. Focus on adjustments, perseverance, and aligning closer to your intentions.",
    "Waning Crescent": "The Waning Crescent Moon appears as a thin crescent, symbolizing a time of surrender, rest, and healing. It's a period to fully let go, rest, and prepare for the new cycle ahead. It's best for Surrendering to the natural flow of life, resting, and rejuvenating your energy."
  }
  if moonphase not in suggestions:
      return "Invalid moonphase"
  return suggestions[moonphase]

