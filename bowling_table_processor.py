def get_player_by_name(name, team_players):
    for team_player in team_players:
        player_name = team_player.player_name
        if player_name == name:
            return team_player


class BowlingTableProcessor:
    def add_bowler_information(self, bowling_table_trs, team_players):
        name = None
        overs = None
        wickets = None
        for tr_index, bowling_table_tr in enumerate(bowling_table_trs):
            for td_index, bowler_table_tr_td in enumerate(bowling_table_tr.children):
                if td_index == 0:
                    name = bowler_table_tr_td.getText()
                if td_index == 1:
                    overs = float(bowler_table_tr_td.getText())
                if td_index == 4:
                    wickets = int(bowler_table_tr_td.getText())
            player = get_player_by_name(name, team_players)
            player.bowling_order = tr_index + 1
            player.overs_bowled = overs
            player.wickets = wickets
