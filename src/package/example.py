# Source: https://www.tiktok.com/@shirleywirleyyy/video/7220949870897614122?_r=1&_t=8h8vPvL1Ire
def get_personality(moonphase):
  personalities = {
    "New Moon": "Good creativity, Adventure seeker, Spontaneous and rash",
    "Full Moon": "Sentimental, Oversensitive, Confused",
    "Waxing Crescent": "High ambition, Very productive, Disinclined to risks",
    "Waning Gibbous": "Thoughtful, Evaluative, Judgemental",
    "First Quarter" : "Competent, Doer, Restless",
    "Last Quater": "Faithful, Emotional, Devoted",
    "Waxing Gibbous": "Soothing, Caring, Stickler for perfection",
    "Waning Crescent": "Dreamy and comtemplative, Individualistic, Solitary"
  }
  return personalities[moonphase]

# Source: https://www.slownorth.com/blogs/journal/moon-phase-ritual-guide
def get_life_suggestion(moonphase):
  suggestions = {
    "New Moon": "This phase is an excellent time to plant metaphorical seeds, set goals for the future, and align with your deepest desires and dreams. The New Moon invites you to embrace new paths and possibilities, offering a fresh slate to write the next chapter of your life. It's best for setting new intentions, planting metaphorical seeds, and beginning new projects. A time for renewal and fresh starts.",
    "Full Moon": "The Full Moon is the phase when the entire face of the moon is illuminated. It symbolizes culmination, harvest, and celebration. This is the peak time for seeing the results of the intentions set during the New Moon, and it's a moment to honor what has come to fruition. It's best for celebrating achievements, embracing gratitude, and engaging in self-reflection. It's a time to honor yourself and others and give thanks for the blessings in your life.",
    "Waxing Crescent": "The waxing crescent phase follows the new moon, and it's visually characterized by a thin sliver of illumination on the right side of the moon. This phase symbolizes growth, intention, and hope, setting the stage for what you wish to achieve in the coming lunar cycle. It's best for taking initial steps towards the goals set during the New Moon. Focus on building, growth, and laying down roots.",
    "Waning Gibbous": "The Waning Gibbous Moon follows the Full Moon and represents the beginning of the moon's transition back to darkness. It symbolizes a time of release, gratitude, and introspection. This phase is about letting go of what no longer serves you and giving thanks for what you've learned. It's best for releasing and letting go of old patterns or habits, reflecting on lessons learned, and expressing gratitude.",
    "First Quarter" : "The First Quarter Moon appears as a half-lit sphere, with the right side illuminated and the left side in shadow. It symbolizes a time of action, decisions, and commitment. As intentions set during the New Moon begin to manifest, it's a period to reassess, make adjustments, and move forward with determination. It's best for taking action and overcoming obstacles. It's a time to make decisions and put in effort toward achieving goals.",
    "Last Quater": "The Last Quarter Moon appears as another half-lit sphere, but this time with the left side illuminated and the right side in shadow. It symbolizes a time of reflection, reassessment, and forgiveness. It's a period to release remaining burdens and prepare for a new beginning. It's best for reflecting on the past cycle, forgiving yourself and others, and letting go of remaining burdens.",
    "Waxing Gibbous": "The Waxing Gibbous Moon phase represents a time of refinement and preparation. As the Moon continues to grow, and more of its surface is illuminated, our focus shifts from initiating actions to perfecting them. This phase urges us to analyze our progress, make necessary adjustments, and hone our path towards our goals. It's a period to be diligent, detail-oriented, and mindful of the larger picture while remaining committed to our intentions. The Waxing Gibbous phase encourages us to be patient and persistent, as we prepare for the culmination of our efforts in the Full Moon. It's best for refinement and fine-tuning. Focus on adjustments, perseverance, and aligning closer to your intentions.",
    "Waning Crescent": "The Waning Crescent Moon appears as a thin crescent, symbolizing a time of surrender, rest, and healing. It's a period to fully let go, rest, and prepare for the new cycle ahead. It's best for Surrendering to the natural flow of life, resting, and rejuvenating your energy."
  }
  return suggestions[moonphase]

