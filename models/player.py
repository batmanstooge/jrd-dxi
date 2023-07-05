class Player(dict):
    def __init__(self):
        super().__init__()
        self.batting_order = None
        self.player_name = ""
        self.team_name = ""
        self.runs = None
        self.balls_faced = None
        self.bowling_order = None
        self.overs_bowled = None
        self.wickets = None
        self.points = 0
        self.average_points = 0.0

    # def __str__(self):
    #     return f"Batting Order: {self.batting_order}, Player Name: {self.player_name}, Team Name: {self.team_name}, " \
    #            f"Runs: {self.runs}, Balls Faced: {self.balls_faced}, Overs: {self.overs_bowled}, Wickets: {self.wickets}, Points: {self.points}, Average Points: {self.average_points}"

    # def __repr__(self):
    #     return f"Batting Order: {self.batting_order}, Player Name: {self.player_name}, Team Name: {self.team_name}, " \
    #            f"Runs: {self.runs}, Balls Faced: {self.balls_faced}, Bowling Order: {self.bowling_order}, " \
    #            f"Overs: {self.overs_bowled}, Wickets: {self.wickets}, Points: {self.points}, " \
    #            f"Average Points: {self.average_points}"
