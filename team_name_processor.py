class TeamNameProcessor:
    def get_team_name(self, team_name_div):
        team_name_text = team_name_div.getText()
        team_name_array = team_name_text.split("(")
        team_name = team_name_array[0].replace("\xa0", "")
        return team_name
