# Tuples
# list of tuples
champions = [
    ("AC Milan", "Liverpool",  2007),
    ("Manchester United", "Chelsea", 2008),
    ("Barcelona", "Manchester United", 2009),
    ("Inter Milan", "Bayern Munic", 2010)
]

for team1, year, team2 in champions:
    print("In {2}, {0} won the Champions League, by beating {1}".format(team1, year, team2))