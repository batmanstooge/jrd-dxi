from bowling_table_processor import BowlingTableProcessor
from models.match import Match
from models.team import Team
from team_name_processor import TeamNameProcessor
from team_name_setter import TeamNameSetter
from team_players_processor import TeamPlayersProcessor


def process_team_scores_wrapping_divs_to_get_team_headings(team_scores_wrapping_divs):
    team_heading_divs = []
    for team_scores_wrapping_div in team_scores_wrapping_divs:
        for index, team_heading_and_scores_div in enumerate(team_scores_wrapping_div.parent):
            if index == 0:
                team_heading_divs.append(team_heading_and_scores_div)
    return team_heading_divs


def process_bowling_table_tbody_to_get_trs(bowling_table_tbody):
    bowling_table_trs = []
    for bowling_table_tr_tuple in enumerate(bowling_table_tbody.children):
        bowling_table_tr = bowling_table_tr_tuple[1]
        count_of_tds = len(list(bowling_table_tr.children))
        if count_of_tds == 11:
            bowling_table_trs.append(bowling_table_tr)
    return bowling_table_trs


def process_bowling_table_to_get_bowling_trs(bowling_table):
    bowling_table_trs = []
    for index, bowling_table_thead_and_tbody in enumerate(bowling_table.children):
        if index == 1:
            bowling_table_tbody = bowling_table_thead_and_tbody
            bowling_table_trs = process_bowling_table_tbody_to_get_trs(bowling_table_tbody)
    return bowling_table_trs


def process_team_scores_wrapping_divs_to_get_team_headings_and_bowling_table_trs(team_scores_wrapping_divs):
    team_a_bowling_table_trs = None
    team_b_bowling_table_trs = None
    for team_scores_index, team_scores_wrapping_div in enumerate(team_scores_wrapping_divs):
        for index, team_scores_wrapping_div_child in enumerate(team_scores_wrapping_div.children):
            if index == 1 and team_scores_index == 0:
                team_b_bowling_table_trs = process_bowling_table_to_get_bowling_trs(team_scores_wrapping_div_child)
            if index == 1 and team_scores_index == 1:
                team_a_bowling_table_trs = process_bowling_table_to_get_bowling_trs(team_scores_wrapping_div_child)
    team_heading_divs = process_team_scores_wrapping_divs_to_get_team_headings(team_scores_wrapping_divs)
    team_heading_divs_and_bowling_table_trs = [team_heading_divs[0], team_a_bowling_table_trs, team_heading_divs[1],
                                               team_b_bowling_table_trs]
    return team_heading_divs_and_bowling_table_trs


def process_batting_table_wrapping_divs_to_get_team_headings_and_bowling_trs(batting_table_wrapping_divs):
    team_scores_wrapping_divs = []
    for batting_table_wrapping_div in batting_table_wrapping_divs:
        team_scores_wrapping_divs.append(batting_table_wrapping_div)
    return process_team_scores_wrapping_divs_to_get_team_headings_and_bowling_table_trs(team_scores_wrapping_divs)


def process_batting_tables_to_get_team_headings_and_bowling_trs(batting_tables):
    batting_table_wrapping_divs = []
    for batting_table in batting_tables:
        batting_table_wrapping_divs.append(batting_table.parent)
    return process_batting_table_wrapping_divs_to_get_team_headings_and_bowling_trs(batting_table_wrapping_divs)


def get_batters_and_batters_who_did_not_bat(batting_table_tbody):
    team_batter_trs = []
    team_batters_who_did_not_bat_tr = None
    for batting_table_tbody_tr_tuple in enumerate(batting_table_tbody.children):
        batting_table_tbody_tr = batting_table_tbody_tr_tuple[1]
        tr_text = batting_table_tbody_tr.getText()
        if "Extras" in tr_text:
            pass
        elif "TOTAL" in tr_text:
            pass
        elif "Fall of wickets" in tr_text:
            pass
        elif "Did not bat" in tr_text:
            team_batters_who_did_not_bat_tr = batting_table_tbody_tr
        else:
            team_batter_trs.append(batting_table_tbody_tr)
    return [team_batter_trs, team_batters_who_did_not_bat_tr]


def process_table_tbodies(batting_table_tbodies):
    team_a_batters_and_batters_who_did_not_bat = []
    team_b_batters_and_batters_who_did_not_bat = []
    for tbody_index, batting_table_tbody in enumerate(batting_table_tbodies):
        if tbody_index == 0:
            team_a_batters_and_batters_who_did_not_bat = get_batters_and_batters_who_did_not_bat(batting_table_tbody)
        elif tbody_index == 1:
            team_b_batters_and_batters_who_did_not_bat = get_batters_and_batters_who_did_not_bat(batting_table_tbody)
    return team_a_batters_and_batters_who_did_not_bat + team_b_batters_and_batters_who_did_not_bat


def get_batting_table_tbodies(batting_tables):
    batting_table_tbodies = []
    for batting_table in batting_tables:
        for index, batting_table_child in enumerate(batting_table.children):
            if index == 1:
                batting_table_tbodies.append(batting_table_child)
    return batting_table_tbodies


def get_batting_tables(batting_th_tr_theads):
    batting_tables = []
    for batting_th_tr_thead in batting_th_tr_theads:
        batting_tables.append(batting_th_tr_thead.parent)
    return batting_tables


def get_batting_th_tr_theads(batting_th_trs):
    batting_th_tr_theads = []
    for batting_th_tr in batting_th_trs:
        batting_th_tr_theads.append(batting_th_tr.parent)
    return batting_th_tr_theads


def get_batting_th_trs(batting_ths):
    batting_th_trs = []
    for batting_th in batting_ths:
        batting_th_trs.append(batting_th.parent)
    return batting_th_trs


class SoupToMatchProcessor:
    def __init__(self):
        self.team_a_heading_div = None
        self.team_a_batter_trs = None
        self.team_a_batters_who_did_not_bat_tr = None
        self.team_a_bowling_table_trs = None
        self.team_b_heading_div = None
        self.team_b_batter_trs = None
        self.team_b_batters_who_did_not_bat_tr = None
        self.team_b_bowling_table_trs = None

    def get_match_from_soup(self, soup):
        self.process_soup(soup)
        match = Match()
        team_a = Team()
        team_b = Team()
        team_name_processor = TeamNameProcessor()
        team_a_name = team_name_processor.get_team_name(self.team_a_heading_div)
        team_b_name = team_name_processor.get_team_name(self.team_b_heading_div)
        team_a.team_name = team_a_name
        team_b.team_name = team_b_name
        match.team_a = team_a
        match.team_b = team_b
        print(match)
        team_players_processor = TeamPlayersProcessor()
        team_a_players_who_batted = team_players_processor.get_players_who_batted(self.team_a_batter_trs)
        team_b_players_who_batted = team_players_processor.get_players_who_batted(self.team_b_batter_trs)
        team_a_players_who_did_not_bat = team_players_processor.get_players_who_did_not_bat(
            self.team_a_batters_who_did_not_bat_tr)
        team_b_players_who_did_not_bat = team_players_processor.get_players_who_did_not_bat(
            self.team_b_batters_who_did_not_bat_tr)
        team_a_players = team_a_players_who_batted + team_a_players_who_did_not_bat
        team_b_players = team_b_players_who_batted + team_b_players_who_did_not_bat
        team_name_setter = TeamNameSetter()
        team_name_setter.set_team_name_to_players(team_a_name, team_a_players)
        team_name_setter.set_team_name_to_players(team_b_name, team_b_players)
        team_a.players = team_a_players
        team_b.players = team_b_players
        bowling_table_processor = BowlingTableProcessor()
        bowling_table_processor.add_bowler_information(self.team_a_bowling_table_trs, team_a_players)
        bowling_table_processor.add_bowler_information(self.team_b_bowling_table_trs, team_b_players)
        return match

    def process_soup(self, soup):
        batting_ths = soup.findAll("th", string="BATTING")
        batting_th_trs = get_batting_th_trs(batting_ths)
        batting_th_tr_theads = get_batting_th_tr_theads(batting_th_trs)
        batting_tables = get_batting_tables(batting_th_tr_theads)
        batting_table_tbodies = get_batting_table_tbodies(batting_tables)
        teams_batters_and_batters_who_did_not_bat = process_table_tbodies(batting_table_tbodies)
        self.team_a_batter_trs = teams_batters_and_batters_who_did_not_bat[0]
        self.team_a_batters_who_did_not_bat_tr = teams_batters_and_batters_who_did_not_bat[1]
        self.team_b_batter_trs = teams_batters_and_batters_who_did_not_bat[2]
        self.team_b_batters_who_did_not_bat_tr = teams_batters_and_batters_who_did_not_bat[3]
        team_headings_and_bowling_tables = process_batting_tables_to_get_team_headings_and_bowling_trs(batting_tables)
        self.team_a_heading_div = team_headings_and_bowling_tables[0]
        self.team_a_bowling_table_trs = team_headings_and_bowling_tables[1]
        self.team_b_heading_div = team_headings_and_bowling_tables[2]
        self.team_b_bowling_table_trs = team_headings_and_bowling_tables[3]
