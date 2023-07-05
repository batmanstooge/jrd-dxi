class PlayerNameProcessor:
    def get_player_name(self, unprocessed_player_name):
        player_name = unprocessed_player_name.replace("(c)", "")
        player_name = player_name.replace("†", "")
        player_name = player_name.strip()
        return player_name