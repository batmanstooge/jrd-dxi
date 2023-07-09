import dataclasses


@dataclasses.dataclass
class Player:
    batting_order: int = None
    player_name: str = ""
    team_name: str = ""
    matches_played: int = 1
    runs: int = None
    balls_faced: int = None
    bowling_order: int = None
    overs_bowled: float = None
    wickets: int = None
    points: int = 0
    average_points: float = 0.0

# def __str__(self):
#     return f"Batting Order: {self.batting_order}, Player Name: {self.player_name}, Team Name: {self.team_name}, " \
#            f"Runs: {self.runs}, Balls Faced: {self.balls_faced}, Overs: {self.overs_bowled}, Wickets: {self.wickets}, Points: {self.points}, Average Points: {self.average_points}"

# def __repr__(self):
#     return f"Batting Order: {self.batting_order}, Player Name: {self.player_name}, Team Name: {self.team_name}, " \
#            f"Runs: {self.runs}, Balls Faced: {self.balls_faced}, Bowling Order: {self.bowling_order}, " \
#            f"Overs: {self.overs_bowled}, Wickets: {self.wickets}, Points: {self.points}, " \
#            f"Average Points: {self.average_points}"
