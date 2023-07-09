from dataclasses import asdict

import pandas as pandas


def get_dataframe_from_file():
    try:
        with open("vb.csv") as vb_file:
            data_frame = pandas.read_csv("vb.csv")
            return data_frame
    except FileNotFoundError as e:
        return pandas.DataFrame()


def set_model_points_and_average_points(players):
    for player in players:
        runs = player.runs
        wickets = player.wickets
        points = 0
        if runs is not None and wickets is not None:
            points = runs + wickets * 25
        elif runs is not None:
            points = runs
        elif wickets is not None:
            points = wickets * 25
        player.points = points
        player.average_points = player.points / player.matches_played


def get_match_player_models(match):
    team_a_player_models = match.team_a.players
    team_b_player_models = match.team_b.players
    return team_a_player_models + team_b_player_models


def get_team_players_from_players_who_have_played(team_name, players_who_have_played_dict):
    return [player for player in players_who_have_played_dict if player["team_name"] == team_name]


def get_team_players_from_all_players_dict(team_name, all_players_dict):
    insert_index = -1
    players_in_all_players_dict = []
    for index, one_in_all_player_dict in enumerate(all_players_dict):
        if one_in_all_player_dict["team_name"] == team_name:
            if insert_index == -1:
                insert_index = index
            players_in_all_players_dict.append(one_in_all_player_dict)
    insert_index_tuple = (insert_index, players_in_all_players_dict)
    return insert_index_tuple


def remove_team_players_from_all_players_dict(team_players, players_who_have_played_dict):
    for team_player in team_players:
        players_who_have_played_dict.remove(team_player)


def get_team_player_who_has_already_played(current_team_player, team_players_who_have_played):
    current_player_name = current_team_player["player_name"]
    for team_player in team_players_who_have_played:
        if team_player["player_name"] == current_player_name:
            return team_player
    return None


def get_players_to_be_inserted(current_team_players, team_players_who_have_played):
    players_who_have_to_be_inserted = []
    for current_team_player in current_team_players:
        team_player_who_has_played = get_team_player_who_has_already_played(current_team_player,
                                                                            team_players_who_have_played)
        if team_player_who_has_played is None:
            players_who_have_to_be_inserted.append(current_team_player)
        else:
            team_players_who_have_played.remove(team_player_who_has_played)


def get_players_who_played_for_team_from_all_players_dict_and_index_of_first_player(team_name, all_players_dict):
    players_who_have_already_played_for_team = []
    index_of_first_player = -1
    for index, player in enumerate(all_players_dict):
        player_team_name = player["team_name"]
        if player_team_name == team_name:
            if index_of_first_player == -1:
                index_of_first_player = index
            players_who_have_already_played_for_team.append(player)
    index_and_players_who_have_already_played_for_team = (
        index_of_first_player, players_who_have_already_played_for_team)
    return index_and_players_who_have_already_played_for_team


def get_player_already_played(team_player, all_players_dict):
    for player in all_players_dict:
        team_player_name = team_player["player_name"]
        player_name = player["player_name"]
        if player_name == team_player_name:
            return player
    return None


def get_player_if_already_played(team_player, team_players_in_all_players_dict):
    team_player_name = team_player["player_name"]
    for player_in_all_players_dict in team_players_in_all_players_dict:
        player_name = player_in_all_players_dict["player_name"]
        if player_name == team_player_name:
            return player_in_all_players_dict
    return None


MATCHES_PLAYED = "matches_played"
RUNS = "runs"
BALLS_FACED = "balls_faced"
OVERS_BOWLED = "overs_bowled"
WICKETS = "wickets"
POINTS = "points"
AVERAGE_POINTS = "average_points"


def set_total_runs(team_player, player_already_played):
    team_player_runs = team_player.get(RUNS)
    player_already_played_runs = player_already_played.get(RUNS)
    if team_player_runs is not None and not pandas.isnull(player_already_played_runs):
        team_player[RUNS] = int(team_player_runs) + int(player_already_played_runs)
    elif not pandas.isnull(player_already_played_runs):
        team_player[RUNS] = int(player_already_played_runs)
    elif team_player_runs is not None:
        return


def set_total_matches(team_player, player_already_played):
    team_player["matches_played"] = int(team_player.get("matches_played")) + int(
        player_already_played.get("matches_played"))


def set_total_balls_faced(team_player, player_already_played):
    team_player_balls_faced = team_player.get(BALLS_FACED)
    player_already_played_balls_faced = player_already_played.get(BALLS_FACED)
    if team_player_balls_faced is not None and not pandas.isnull(player_already_played_balls_faced):
        team_player[BALLS_FACED] = int(team_player_balls_faced) + int(player_already_played_balls_faced)
    elif not pandas.isnull(player_already_played_balls_faced):
        team_player[BALLS_FACED] = int(player_already_played_balls_faced)
    elif team_player_balls_faced is not None:
        return


def set_total_overs_bowled(team_player, player_already_played):
    team_player_overs_bowled = team_player.get(OVERS_BOWLED)
    player_already_played_overs_bowled = player_already_played.get(OVERS_BOWLED)
    if team_player_overs_bowled is not None and not pandas.isnull(player_already_played_overs_bowled):
        team_player[OVERS_BOWLED] = int(team_player_overs_bowled) + int(player_already_played_overs_bowled)
    elif not pandas.isnull(player_already_played_overs_bowled):
        team_player[OVERS_BOWLED] = int(player_already_played_overs_bowled)
    elif team_player_overs_bowled is not None:
        return


def set_total_wickets(team_player, player_already_played):
    team_player_wickets = team_player.get(WICKETS)
    player_already_wickets = player_already_played.get(WICKETS)
    if team_player_wickets is not None and not pandas.isnull(player_already_wickets):
        team_player[WICKETS] = int(team_player_wickets) + int(player_already_wickets)
    elif not pandas.isnull(player_already_wickets):
        team_player[WICKETS] = int(player_already_wickets)
    elif team_player_wickets is not None:
        return


def set_points_and_average_point(players_to_be_inserted):
    for player in players_to_be_inserted:
        matches_played = player[MATCHES_PLAYED]
        runs = player.get(RUNS)
        wickets = player.get(WICKETS)
        points = 0
        if runs is not None:
            points = runs
        if wickets is not None:
            points = points + wickets * 25
        player[POINTS] = points
        average_points = points / matches_played
        player[AVERAGE_POINTS] = average_points


def add_new_players_and_merge_existing_players(team_players_dict, team_players_in_all_players_dict):
    players_to_be_inserted = []
    for team_player in team_players_dict:
        player_already_played = get_player_if_already_played(team_player, team_players_in_all_players_dict)
        if player_already_played is not None:
            set_total_matches(team_player, player_already_played)
            set_total_runs(team_player, player_already_played)
            set_total_balls_faced(team_player, player_already_played)
            set_total_wickets(team_player, player_already_played)
            team_players_in_all_players_dict.remove(player_already_played)
        players_to_be_inserted.append(team_player)
    set_points_and_average_point(players_to_be_inserted)
    for player in team_players_in_all_players_dict:
        player.pop("batting_order")
        player.pop("bowling_order")
        players_to_be_inserted.append(player)
    return players_to_be_inserted


def remove_team_players_from_dataframe(team_name, all_players_dataframe):
    all_players_dataframe_dict = all_players_dataframe.to_dict(orient="records")
    start_index = -1
    end_index = -1
    for index, player_who_has_already_played in enumerate(all_players_dataframe_dict):
        player_who_has_played_team_name = player_who_has_already_played["team_name"]
        if player_who_has_played_team_name == team_name:
            if start_index == -1:
                start_index = index
        else:
            if start_index > -1:
                if end_index == -1:
                    end_index = index
    if start_index == 0:
        all_players_dataframe_dict = all_players_dataframe_dict[end_index:]
    else:
        all_players_dataframe_dict = all_players_dataframe_dict[0:start_index] + all_players_dataframe_dict[end_index:]
    new_dataframe = pandas.DataFrame(all_players_dataframe_dict)
    index_and_dataframe = (start_index, new_dataframe)
    return index_and_dataframe


def merge_current_team_players_with_all_players(merge_arguments, all_players_dataframe):
    for merge_argument in merge_arguments:
        team_name = merge_argument[0]
        team_players_in_all_players_df = merge_argument[1]
        team_players_in_all_players_dict = team_players_in_all_players_df.to_dict(orient="records")
        current_team_players = merge_argument[2]
        players_to_be_inserted = add_new_players_and_merge_existing_players(current_team_players,
                                                                            team_players_in_all_players_dict)
        index_and_dataframe = remove_team_players_from_dataframe(team_name, all_players_dataframe)
        index_to_insert = index_and_dataframe[0]
        dataframe_to_insert_dict = index_and_dataframe[1].to_dict(orient="records")
        for player in players_to_be_inserted:
            dataframe_to_insert_dict.insert(index_to_insert, player)
            index_to_insert += 1
        all_players_dataframe = pandas.DataFrame(dataframe_to_insert_dict)
    return all_players_dataframe.to_dict(orient="records")
        # team_name = merge_argument[0]
        # # team_players_who_have_played_dict = get_team_players_from_players_who_have_played(team_name, players_who_have_played_dict)
        # insert_index_team_players_tuple = get_team_players_from_all_players_dict(team_name, players_who_have_played_dict)
        # insert_index = insert_index_team_players_tuple[0]
        # team_players_who_have_played = insert_index_team_players_tuple[1]
        # remove_team_players_from_all_players_dict(team_players_who_have_played, players_who_have_played_dict)
        # current_team_players = merge_argument[1]
        # get_players_to_be_inserted(current_team_players, team_players_who_have_played)


def add_current_match_players_with_all_players(match, all_players_dataframe):
    if all_players_dataframe.empty:
        current_match_players_dict = add_current_match_team_players(match)
        return current_match_players_dict
    else:
        team_a_name = match.team_a.team_name
        team_b_name = match.team_b.team_name
        team_a_df = all_players_dataframe[all_players_dataframe["team_name"] == team_a_name]
        team_b_df = all_players_dataframe[all_players_dataframe["team_name"] == team_b_name]
        if team_a_df.empty and team_b_df.empty:
            current_match_players_dict = add_current_match_team_players(match)
            all_players_dict = all_players_dataframe.to_dict(orient="records")
            all_players_and_current_match_players_dict = all_players_dict + current_match_players_dict
            return all_players_and_current_match_players_dict
        elif not team_a_df.empty and not team_b_df.empty:
            team_a_players = match.team_a.players
            team_a_players_dict = [asdict(player) for player in team_a_players]
            team_b_players = match.team_b.players
            team_b_players_dict = [asdict(player) for player in team_b_players]
            merge_arguments = [(team_a_name, team_a_df, team_a_players_dict),
                               (team_b_name, team_b_df, team_b_players_dict)]
            all_players_dataframe_dict = merge_current_team_players_with_all_players(merge_arguments, all_players_dataframe)
            return all_players_dataframe_dict
        elif not team_a_df.empty:
            team_a_players = match.team_a.players
            team_a_players_dict = [asdict(player) for player in team_a_players]
            merge_arguments = [(team_a_name, team_a_df, team_a_players_dict)]
            all_players_dataframe_dict = merge_current_team_players_with_all_players(merge_arguments,
                                                                                     all_players_dataframe)
            return all_players_dataframe_dict
        elif not team_b_df.empty:
            team_b_players = match.team_b.players
            team_b_players_dict = [asdict(player) for player in team_b_players]
            merge_arguments = [(team_b_name, team_b_df, team_b_players_dict)]
            all_players_dataframe_dict = merge_current_team_players_with_all_players(merge_arguments,
                                                                                     all_players_dataframe)
            return all_players_dataframe_dict

def add_current_match_team_players(match):
    team_a_players = match.team_a.players
    team_b_players = match.team_b.players
    set_model_points_and_average_points(team_a_players)
    set_model_points_and_average_points(team_b_players)
    match_player_models = team_a_players + team_b_players
    match_players_dict = [asdict(player) for player in match_player_models]
    return match_players_dict


class PandasProcessor:
    def __init__(self):
        self.all_players_who_have_played_dataframe = pandas.DataFrame()
        self.all_players_who_have_played_dataframe = get_dataframe_from_file()

    def add_match(self, match):
        merged_players_dict = add_current_match_players_with_all_players(match,
                                                                         self.all_players_who_have_played_dataframe)
        self.all_players_who_have_played_dataframe = pandas.DataFrame(merged_players_dict)

    def save_dataframe_to_file(self):
        self.all_players_who_have_played_dataframe.to_csv("vb.csv", index=False)
