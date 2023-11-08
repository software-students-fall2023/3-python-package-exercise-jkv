# __main__.py

import PyMoon as moon_phases
  


def main():

    moonphase = moon_phases.get_type()
    compatability = moon_phases.get_compatability(moonphase)
    personality = moon_phases.get_personality(moonphase)
    lifeSuggestion = moon_phases.get_life_suggestion(moonphase)

    print(moonphase)
    print(compatability)
    print(personality)
    print(lifeSuggestion)

if __name__ == "__main__":
    main()