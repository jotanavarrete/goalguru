import numpy as np

##################  API_LOGIC  #####################
# dictionary with all the competitions (independent from dataset origin)
ALL_COMPETITIONS = {
    0: 'Premier League',
    1: 'Serie A',
    2: 'La Liga',
    3: 'Ligue 1',
    4: '1. Bundesliga',
    5: 'FIFA World Cup',
    6: 'UEFA Euro Cup',
    7: "FA Women's Super League",
    8: "Women's World Cup",
    9: "UEFA Women's Euro",
    10: 'Indian Super league'
}
# from ALL_COMPETITIONS to soccermatch dataset
TO_SOCCERMATCH_COMPETITIONS = {
    1: 524,  # 'Serie A'
    0: 364,  # Premier League
    2: 795,  # 'LaLiga'
    3: 412,  # 'Ligue 1'
    4: 426,  # 'Bundesliga'
    6: 102,  # 'Euro Cup'
    5: 28  # 'World Cup'
}
# from ALL_COMPETITIONS to statsbomb dataset
TO_STATSBOMB_COMPETITIONS = {
    4: 9,  # '1. Bundesliga'
    7: 37,  # "FA Women's Super League"
    5: 43,  # 'FIFA World Cup'
    10: 1238,  # 'Indian Super league'
    2: 11,  # 'La Liga'
    3: 7,  # 'Ligue 1'
    0: 2,  # 'Premier League'
    1: 12,  # 'Serie A'
    6: 55,  # 'UEFA Euro'
    8: 72,  # "Women's World Cup"
    9: 53  # "UEFA Women's Euro"
}
