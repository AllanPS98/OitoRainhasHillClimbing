class Rainha:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getNome__(self):
        return 1

    def __getPosicao__(self):
        return [self.x, self.y]

    def __getX__(self):
        return self.x

    def __getY__(self):
        return self.y

    def __setY__(self, y):
        self.y = y
