

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.stats = []
        self.file = None
        self.load()

    def load(self):
        print("hello")
        self.file = open(self.filename, "r")
        for line in self.file:
            gameStarted, gameWon, gameLose, bestTime = line.strip().split(";")
            self.stats = [int(gameStarted), int(gameWon), int(gameLose), int(bestTime)]

        self.file.close()

    def get_data(self):
        return self.stats

    def add_data(self,gameData):

        self.stats[0] +=1
        self.stats[1] += gameData[0]
        self.stats[2] += gameData[1]
        if self.stats[3] == 0:
             self.stats[3] = gameData[2]
        elif self.stats[3] > gameData[2]:
            self.stats[3] = gameData[2]
        self.save()

    def reset(self):
        self.stats[0] = 0
        self.stats[1] = 0
        self.stats[2] = 0
        self.stats[3] = 0
        self.save()

    def save(self):
        with open(self.filename, "w") as f:
            f.write(str(self.stats[0]) + ";" + str(self.stats[1]) + ";" + str(self.stats[2]) + ";" + str(self.stats[3]))
