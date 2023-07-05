import pandas as pandas


def set_dataframe_from_file(dataframe):
    try:
        with open("vb.csv") as vb_file:
            data_frame = pandas.read_csv("vb.csv")
    except FileNotFoundError as e:
        print(e)


class PandasProcessor:
    def __init__(self):
        self.dataframe = pandas.DataFrame()
        set_dataframe_from_file(self.dataframe)

    def add_match(self, match):
        if self.dataframe.empty:
            match_players = match.team_a.players + match.team_b.players
            self.dataframe = pandas.DataFrame(match_players)
            print(self.dataframe)