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
  