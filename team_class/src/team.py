class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, name):
        team_has_player = False
        for player in self.players:
            if player == name:
                return True
        return team_has_player

    def play_game(self, win):
        if win:
            self.points += 3