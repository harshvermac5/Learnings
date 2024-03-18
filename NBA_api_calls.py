from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    try:
        response = get(BASE_URL + ALL_JSON)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        links = data['links']
        return links
    except Exception as e:
        print(f"Error getting links: {e}")
        return None

def get_scoreboard():
    links = get_links()
    if links:
        try:
            scoreboard = links['currentScoreboard']
            response = get(BASE_URL + scoreboard)
            response.raise_for_status()
            games = response.json()['games']

            for game in games:
                home_team = game['hTeam']
                away_team = game['vTeam']
                clock = game['clock']
                period = game['period']

                print("----------------------------------")
                print(f"{home_team['triCode']} vs {away_team['triCode']}")
                print(f"{home_team['score']} - {away_team['score']}")
                print(f"{clock} - {period['current']}")
        except Exception as e:
            print(f"Error getting scoreboard: {e}")

def get_stats():
    links = get_links()
    if links:
        try:
            stats = links['leagueTeamStatsLeaders']
            response = get(BASE_URL + stats)
            response.raise_for_status()
            teams = response.json()['league']['standard']['regularSeason']['teams']

            teams = list(filter(lambda x: x['name'] != 'Team', teams))
            teams.sort(key=lambda x: int(x['ppg']['rank']))

            for i ,team in enumerate(teams):
                name = team['name']
                nickname = team['nickname']
                ppg = team['ppg']['avg']
                print(f"{i + 1}. {name} - {nickname} - {ppg}")
        except Exception as e:
            print(f"Error getting stats: {e}")

get_stats()