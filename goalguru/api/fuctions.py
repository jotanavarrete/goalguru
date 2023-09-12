"""
Creamos las funciones para poder aplicar a la API y sepa donde buscar.
"""
## IMPORTANTE: Hayq eue descomentar cierta lineas que tenga ##%




## Model from soccermatch_package
#%from goalguru.soccermatch_package.preprocessor import preprocess_features

## Model from statsbombs_package
#%from goalguru.statsbombs_package.preprocessor  import preprocess_features



def get_competitions(data, df_name):

    ## This fuction returns a list of dictionaries with the following structure

    """""
    competitions = [
    {'competition_id': 0, 'name': 'Premier League'},
    {'competition_id': 1, 'name': 'Serie A'},
    {'competition_id': 2, 'name': 'Bundesliga'},
    {'competition_id': 3, 'name': 'La Liga'},
    {'competition_id': 4, 'name': 'World Cup'}
    ]
    """
    # Group the DataFrame by 'competition_id' and 'name' columns and aggregate them
    grouped_data = data.groupby(['competition_id', 'name']).size().reset_index(name='count')

    # Convert the grouped DataFrame to a list of dictionaries
    competition_list = [{'competition_id': row['competition_id'], 'name': row['name'], 'dataframe': df_name} for _, row in grouped_data.iterrows()]

    return competition_list


def get_seasons(competition_id):

    # ## This fuctions returns a list of all the available seasons for the given
    # competition_id, with the following structure:

    """
    seasons = {
    0: [
        {'season_id': 0, 'season': '2016/2017', 'matchweeks': list(range(1,11)), 'dataset': 'soccermatch'},
        {'season_id': 1, 'season': '2017/2018', 'matchweeks': list(range(1,11)), 'dataset': 'statsbomb'}
        ],
    1: [
        {'season_id': 0, 'season': '2015/2016', 'matchweeks': range(3,38), 'dataset': 'soccermatch'},
        {'season_id': 1, 'season': '2016/2017', 'matchweeks': range(4,7), 'dataset': 'statsbomb'}
        ],
    2: [
        {'season_id': 0, 'season': '2015/2016', 'matchweeks': range(5,11), 'dataset': 'soccermatch'}
        ],
    3: [
        {'season_id': 0, 'season': '2016/2017', 'matchweeks': range(6,15), 'dataset': 'statsbomb'},
        {'season_id': 1, 'season': '2017/2018', 'matchweeks': range(1,11), 'dataset': 'soccermatch'}
        ],
    4: [
        {'season_id': 0, 'season': '2018', 'matchweeks': range(1,8), 'dataset': 'statsbomb'}
        ]
    }
    """
    ## According to the dataframe asked create this fuction
    data=data

    # Filter the DataFrame based on the given competition_id
    filtered_data = data[data['competition_id'] == competition_id]

  # Check if there is data for the given competition_id
    if filtered_data.empty:
        return print("No data for the provided competition_id.")

    # Get unique season IDs for the selected competition
    unique_seasons = filtered_data['season_id'].unique()

    # Create a list of dictionaries for each unique season
    seasons_list = [
        {
            'season_id': season_id,
            'season': filtered_data[filtered_data['season_id'] == season_id]['season'].iloc[0],
            'matchweeks': list(range(len(filtered_data[filtered_data['season_id'] == season_id])))
        }
        for season_id in unique_seasons
    ]

    return seasons_list



## cada dataset tiene a priori tiene un season unico.
## matchweeks: Partidos de la temporada


"""
def get_matches(competition_id, season_id, matchweek, dataset (soccermatch or statsbomb)):
"""


# returns a list of all the matches for the given parameters, with the following
# structure. This method internally looks into the corresponding
#  dataset (soccermatch or statsbomb) and fetches the list of the matches
"""
    matches = {
        0: {
            0: {
                0: [
                    {'match_id': 1545, 'name': 'Arsenal vs Tottenham','home_team':'Asesnal', 'away_team':'Tottenham'},
                    {'match_id': 6545, 'name': 'ManU vs ManCity'}
                    ]
                },
            1: {
                0: [
                    {'match_id': 484, 'name': 'Liverpool vs Everton'},
                    {'match_id': 6546, 'name': 'Burnley vs Wolves'}
                    ]
                }
            },
        1: {
            0: {
                0: [
                    {'match_id': 198, 'name': 'Inter vs Milan'},
                    {'match_id': 1154, 'name': 'Juventus vs Torino'}
                    ]
                },
            1: {
                0: [
                    {'match_id': 1981, 'name': 'Lazio vs Fiorentina'},
                    {'match_id': 62, 'name': 'Napoli vs Palermo'}
                    ]
                }
            },
        2: {
            0: {
                0: [
                    {'match_id': 654, 'name': 'Borussia Dortmund vs Bayern Munchen'},
                    {'match_id': 98, 'name': 'Hannover vs Mainz'}
                    ]
                }
            },
        3: {
            0: {
                0: [
                    {'match_id': 78, 'name': 'Barcelona vs Real Madrid'},
                    {'match_id': 14, 'name': 'Real Sociedad vs Athletic Bilbao'}
                    ]
                },
            1: {
                0: [
                    {'match_id': 1, 'name': 'Athletic Bilbao vs Real Madrid'},
                    {'match_id': 2, 'name': 'Real Sociedad vs Barcelona'}
                    ]
                }
            },
        4: {
            0: {
                0:[
                    {'match_id': 33, 'name': 'Argentina vs France'},
                    {'match_id': 55, 'name': 'Croatia vs England'}
                    ]
                }
            },
    }
    """

 #   return None



# API predict(match_id, dataset)
# returns a prediction with the following structure
prediction = {
    'outcome': 1,
    'probabilities': [0.56, 0.24, 0.20]
}

# API get_result(match_id, dataset)
# returns the result of a given match with the following structure
# (to change for the real team names)

result = {
    'result': 'local team 2 - 1 away team'
}
