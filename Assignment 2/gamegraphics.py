# ------------------------------------------------------
# This module contains all graphics-classes for the cannon game.
# The two primary classes have these responsibilities:
#  * GameGraphics is responsible for the main window
#  * Each PlayerGraphics is responsible for the graphics of a 
#    single player (score, cannon, projectile)
# In addition there are two UI-classes that have no
# counterparts in the model:
#  * Button
#  * InputDialog
# ------------------------------------------------------

# This is the only place where graphics should be imp
from graphics import *


# Creates the main window of the game and the graphical players, also draws the ground.
class GameGraphics:
    def __init__(self, game):
        self.game = game
        win = GraphWin("Cannon game", 640, 480, autoflush=False)
        win.setCoords(-110, -10, 110, 155)
        self.win = win

        # Draw the ground as a line
        self.line = Line(Point(-110, 0), Point(110, 0))
        self.line.draw(self.getWindow())

        # Create the graphical players
        self.player1 = PlayerGraphics(self.game.players[0], self)
        self.player2 = PlayerGraphics(self.game.players[1], self)

    def getWindow(self):
        return self.win

    def sync(self):
        self.player1.sync()
        self.player2.sync()
        self.win.update()


# Draws the player cannon and the score.
# Has a function sync that draws the player's current projectile in the main window.
class PlayerGraphics:
    def __init__(self, player, ggame):
        self.player = player
        self.ggame = ggame

        # Draw the cannon
        self.x_coord = self.player.getX()
        self.cannon_size = self.ggame.game.cannonSize
        self.cannon = Rectangle(Point(self.x_coord - self.cannon_size / 2, self.cannon_size),
                                Point(self.x_coord + self.cannon_size / 2, 0))
        self.cannon.draw(self.ggame.getWindow())
        self.cannon.setFill(self.player.getColor())

        # Draw the current score of the player
        self.score = Text(Point(self.x_coord, -self.cannon_size / 2), "Score: " + str(self.player.getScore()))
        self.score.draw(self.ggame.getWindow())
        self.proj = self.player.getProjectile()

        self.graphProj = None

    # Updates the score text and the projectile in the main window
    def sync(self):
        self.score.undraw()
        self.score = Text(Point(self.x_coord, -self.cannon_size / 2), "Score: " + str(self.player.getScore()))
        self.score.draw(self.ggame.getWindow())

        proj_new = self.player.getProjectile()
        if proj_new is not None:
            if self.graphProj is None:  # If it's the first time the player fires a projectile
                self.graphProj = Circle(Point(proj_new.getX(), proj_new.getY()), self.ggame.game.getBallSize())
                self.graphProj.draw(self.ggame.getWindow())
                self.graphProj.setFill(self.player.getColor())

            else:  # If there already exists a drawn projectile we first undraw it and replace it with the updated
                self.graphProj.undraw()
                self.graphProj = Circle(Point(proj_new.getX(), proj_new.getY()), self.ggame.game.getBallSize())
                self.graphProj.draw(self.ggame.getWindow())
                self.graphProj.setFill(self.player.getColor())

        self.proj = proj_new


""" A somewhat specific input dialog class (adapted from the book) """


class InputDialog:
    """ Creates an input dialog with initial values for angle and velocity and displaying wind """

    def __init__(self, angle, vel, wind):
        self.win = win = GraphWin("Fire", 200, 300)
        win.setCoords(0, 4.5, 4, .5)
        Text(Point(1, 1), "Angle").draw(win)
        self.angle = Entry(Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1, 2), "Velocity").draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1, 3), "Wind").draw(win)
        self.height = Text(Point(3, 3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))

        self.fire = Button(win, Point(1, 4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3, 4), 1.25, .5, "Quit")
        self.quit.activate()

    """ Waits for the player to enter values and click a button """

    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    """ Gets the values entered into this window, typically called after interact """

    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        return a, v

    """ Closes the input window """

    def close(self):
        self.win.close()


""" A general button class (from the book) """


class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """

        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "RETURNS true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        "RETURNS the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0
