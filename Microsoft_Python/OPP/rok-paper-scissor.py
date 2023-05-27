class Participant:
    counter = 1 # class variable

    def __init__(self):
        self.name = input("Please enter Player{} Name: ".format(Participant.counter))
        self.points = 0 # Object variable or attribute
        self.choice = ""
        Participant.counter += 1

    def choose(self):
        self.choice = input("{}, select rock, paper or scissor: ".format(self.name))
        print("{} selects {}".format(self.name, self.choice))

    def toNumericalChoice(self):
        switcher = {"rock": 0, "paper": 1, "scissor": 2}
        return switcher[self.choice]
    
    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2, rules):
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2, rules)
        self.awardPoints(p1, p2, result)

    def compareChoices(self, p1, p2, rules):
        return rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def awardPoints(self, p1, p2, result):
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()


class Game:
    def __init__(self):
        self.rules = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        self.participant = Participant()
        self.secondParticipant = Participant()
        self.endGame = False

    def start(self):
        while self.endGame != True:
            GameRound(self.participant, self.secondParticipant, self.rules)
            self.checkEndCondition()


    def checkEndCondition(self):
        answer = input("One more game? y/n: ")
        if answer == "n":
            print("Game ended, {} has {}, and {} has {}".format(self.participant.name, self.participant.points, self.secondParticipant.name, self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {}".format(self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {}".format(self.secondParticipant.name)
        print(resultString)

game = Game()
game.start()