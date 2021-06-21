class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, name):
        team_has_player = False
        for player in self.players:
            if player == name:
                return True
        return team_has_player