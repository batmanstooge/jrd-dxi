from models.player import Player
from player_name_processor import PlayerNameProcessor


class TeamPlayersProcessor:
    def get_players_who_batted(self, player_trs):
        players = []
        batting_order = 0
        for player_tr in player_trs:
            batting_order += 1
            player = Player()
            player.batting_order = batting_order
            for index, player_td in enumerate(player_tr.children):
                if index == 0:
                    player_name_processor = PlayerNameProcessor()
                    player_name = player_name_processor.get_player_name(player_td.getText())
                    player.player_name = player_name
                if index == 2:
                    runs = player_td.getText()
                    player.runs = int(runs)
                if index == 3:
                    balls_faced = player_td.getText()
                    player.balls_faced = int(balls_faced)
            players.append(player)
        return players

    def get_players_who_did_not_bat(self, batters_who_did_not_bat_tr):
        batters_who_did_not_bat_tr_text = batters_who_did_not_bat_tr.getText()
        batters_who_did_not_bat_tr_text = batters_who_did_not_bat_tr_text.replace("Did not bat:", "")
        batters_who_did_not_bat_tr_array = batters_who_did_not_bat_tr_text.split(",")
        batters_who_did_not_bat = []
        for batter_who_did_not_bat_text in batters_who_did_not_bat_tr_array:
            batter_who_did_not_bat = Player()
            player_name_processor = PlayerNameProcessor()
            player_name = player_name_processor.get_player_name(batter_who_did_not_bat_text)
            batter_who_did_not_bat.player_name = player_name
            batters_who_did_not_bat.append(batter_who_did_not_bat)
        return batters_who_did_not_bat
