import turtle
import random


class Game(object):

    def __init__(self, turtles):
        self._turtles = turtles
        self.turtles = []
        self.predictions = ()

        screen = turtle.Screen()
        screen.setup(1390, 800)
        screen.bgpic('./champcourse2.gif')

        x = -660
        y = -300

        for name, color in turtles:
            self.turtles.append((name, self.init_turtle(color, x, y)))
            y += 150

    def init_turtle(self, color, x, y):
        t = turtle.Turtle()
        t.speed(300)
        t.penup()
        t.color(color)
        t.shape('turtle')
        t.setpos(x, y)
        t.pendown()

        return t

    def ask_predictions(self):
        inputs = {
            'Player One': input("Prédictions du joueur 1\n"),
            'Player Two': input("Prédictions du joueur 2\n")
        }

        for i, n in inputs.items():
            inputs[i] = [self.turtles[int(a)][0] for a in n.split(',')]

        self.predictions = inputs

    def start_race(self):
        participants = list(self.turtles)
        winners = []

        while len(participants):
            index = random.randint(0, len(participants) - 1)

            t = participants[index]
            t[1].forward(10)

            if t[1].xcor() >= 680:
                winners.append(t[0])
                del participants[index]

        print("Résultat de la course:")
        for i, t in enumerate(winners):
            print("{} : {}".format(i + 1, t))

        someone_won = False

        for name, prediction in self.predictions.items():
            if prediction == winners:
                print('Il y a un gagnant, le {} avec comme prédiction: {}'.format(name, prediction))
                someone_won = True

        if not someone_won:
            print("Désolé personne n'a gagné")


if __name__ == '__main__':
    game = Game(turtles=[
        ('michel', 'Orange'),
        ('leonard', 'Deep Sky Blue'),
        ('raphael', 'Red'),
        ('donatelo', 'Purple'),
        ('splinter', 'Dark Slate Gray')
    ])

    game.ask_predictions()

    game.start_race()
