import random
random.seed(None)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.current_stroke = 0
        self.choices = ["pierre", "feuille", "ciseaux"]

    def equals(self, other):
        return self.current_stroke == other.current_stroke

    def isWinning(self, other):
        return self.score > other.score

    def updateStroke(self):
        self.current_stroke = random.randint(0, 2)
        print(self.current_stroke)

    def strokeType(self):
        return f"{self.choices[self.current_stroke]}"

    def __str__(self):
        return f"{self.name}"

    def current_plays(self):
        return f"{self} a joué {self.strokeType()}"

    def inc_score(self):
        self.score += 1


def updateRound(player1: Player, player2: Player):
    random.seed(None)
    player1.updateStroke()
    player2.updateStroke()
    if player1.equals(player2):
        return
    if (player1.current_stroke == 2 and player2.current_stroke == 1) or \
            (player1.current_stroke == 1 and player2.current_stroke == 0) or \
            (player1.current_stroke == 0 and player2.current_stroke == 2):
        player1.inc_score()
    else:
        player2.inc_score()


def selectWinner(player1: Player, player2: Player):
    if player1.equals(player2):
        return None
    return player1 if player1.isWinning(player2) else player2


def display_score(player1: Player, player2: Player):
    return f"Score : {player1} {player1.score} - {player2} {player2.score}"


def display_winner(player1: Player, player2: Player):
    return f"Le vainqueur est : {player1}" if player1.isWinning(player2) else f"Le vainqueur est : {player2}"
