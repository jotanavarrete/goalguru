import json
import os
from pathlib import Path
from goalguru.statsbombs_package.data import valid_competitions, read_matches
from goalguru.statsbombs_package.params import REQUEST_PATH


def save_competitions():

    competitions_df = valid_competitions()[['competition_id', 'competition_name']]\
        .drop_duplicates().rename(columns={'competition_name': 'name'})

    competitions_list = competitions_df.to_dict('records')

    with open(os.path.join(REQUEST_PATH, 'competitions.json'), 'w+') as f:
        json.dump(competitions_list, f)

    print(f'data saved to {os.path.join(REQUEST_PATH, "competitions.json")}')

    return

def load_competitions():
    with open(os.path.join(REQUEST_PATH, 'competitions.json'), 'r') as f:
        competitions = json.load(f)

    return competitions

def get_competitions():

    competitions_cache_path = Path(REQUEST_PATH).joinpath('competitions.json')
    competitions_cached_exists = competitions_cache_path.is_file()

    if not competitions_cached_exists:
        save_competitions()

    competitions = load_competitions()

    return competitions

def save_seasons():
    competitions_df = valid_competitions()
    competitions = get_competitions()
    seasons = {}

    for competition in competitions:
        competition_id = competition['competition_id']
        actual_competition_df = competitions_df.query(f'competition_id == {competition_id}')
        seasons_list = actual_competition_df[['season_id', 'season_name']].to_dict('records')

        for season in seasons_list:
            matches_df = read_matches(competition_id, season['season_id'])
            matchweeks = matches_df['match_week'].unique()
            season['matchweeks'] = sorted(matchweeks.tolist())
            season['dataset'] = 'statsbomb'

        seasons[competition_id] = seasons_list

    with open(os.path.join(REQUEST_PATH, 'seasons.json'), 'w+') as f:
        json.dump(seasons, f)

    print(f'data saved to {os.path.join(REQUEST_PATH, "seasons.json")}')

    return

def load_seasons():
    with open(os.path.join(REQUEST_PATH, 'seasons.json'), 'r') as f:
        seasons = json.load(f)

    return seasons

def get_seasons(competition_id):

    seasons_cache_path = Path(REQUEST_PATH).joinpath('seasons.json')
    seasons_cached_exists = seasons_cache_path.is_file()

    if not seasons_cached_exists:
        save_seasons()

    seasons = load_seasons()

    actual_season = seasons[str(competition_id)]

    return actual_season

def save_matches():
    seasons_per_competition = load_seasons()
    competitions_dict = {}

    for competition_id in seasons_per_competition.keys():
        seasons = seasons_per_competition[competition_id]
        seasons_dict = {}

        for season in seasons:
            season_id = season['season_id']
            matchweeks = season['matchweeks']
            matchweeks_dict = {}
            matches_df = read_matches(int(competition_id), int(season_id))

            for matchweek in matchweeks:
                actual_match_df = matches_df.query(f'match_week == {matchweek}')[['match_id', 'home_team', 'away_team']]
                actual_match_df.loc[:, 'home_team'] = actual_match_df.loc[:, 'home_team'].map(lambda x: x.get('home_team_name'))
                actual_match_df.loc[:, 'away_team'] = actual_match_df.loc[:, 'away_team'].map(lambda x: x.get('away_team_name'))
                actual_match_df.loc[:, 'name'] = actual_match_df.loc[:, 'home_team'] + ' vs ' + actual_match_df.loc[:, 'away_team']

                matches_list = actual_match_df.to_dict('records')
                matchweeks_dict[matchweek] = matches_list


            seasons_dict[int(season_id)] = matchweeks_dict

        competitions_dict[int(competition_id)] = seasons_dict


    with open(os.path.join(REQUEST_PATH, 'matches.json'), 'w+') as f:
        json.dump(competitions_dict, f)

    print(f'data saved to {os.path.join(REQUEST_PATH, "matches.json")}')

    return

def load_matches():
    with open(os.path.join(REQUEST_PATH, 'matches.json'), 'r') as f:
        matches = json.load(f)

    return matches

def get_matches(competition_id, season_id, matchweek):

    matches_cache_path = Path(REQUEST_PATH).joinpath('matches.json')
    matches_cached_exists = matches_cache_path.is_file()

    if not matches_cached_exists:
        save_matches()

    matches = load_matches()

    actual_matches = matches[str(competition_id)][str(season_id)][str(matchweek)]

    return actual_matches


# if __name__ == '__main__':
    # print(get_competitions())
    # save_seasons()
    # print(get_seasons(9))
    # print(get_matches(9, 27, 1))
    # save_competitions()
    # save_seasons()
    # save_matches()
