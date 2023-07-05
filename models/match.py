from models.team import Team


class Match:
    def __init__(self):
        self.team_a: Team = None
        self.team_b: Team = None

    # def __repr__(self):
    #     return f"Team A: {self.team_a}\nTeam B: {self.team_b}"