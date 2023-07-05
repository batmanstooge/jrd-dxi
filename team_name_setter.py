class TeamNameSetter:
    def set_team_name_to_players(self, team_name, players):
        for player in players:
            player.team_name = team_name
