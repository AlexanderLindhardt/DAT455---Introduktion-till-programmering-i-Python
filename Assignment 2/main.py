# Imports everything from both model and graphics
from gamemodel import *
from gamegraphics import *


# Fires a shot for the current player and animates it until it stops
def graphicFire(game, graphics, angle, vel):
    # Get current player
    player = game.getCurrentPlayer()
    # Create a projectile and track until it hits ground or leaves window
    proj = player.fire(angle, vel)
    while proj.isMoving():
        proj.update(1/50)
        graphics.sync()  # This deals with all graphics-related issues
        update(50)  # Waits for a short amount of time before the next iteration
    return proj


# Shows dialog window where user decides the aim of the cannon
def graphicInput(game):
    player = game.getCurrentPlayer()
    oldAngle, oldVel = player.getAim()  # Takes the current values as initial angle and velocity
    dialog = InputDialog(oldAngle, oldVel, game.getCurrentWind())  # Input dialog window
    response = dialog.interact()  # See what action the user chooses
    if response == 'Fire!':  # If Fire, get the new angle and velocity and return them
        newAngle, newVel = dialog.getValues()
        dialog.close()
        return newAngle, newVel
    elif response == 'Quit':
        exit()


# This function looks where the projectile lands and makes the correct action depending on if it hits or not
def graphicFinishShot(game, proj):
    # Get the players
    player = game.getCurrentPlayer()
    other = game.getOtherPlayer()
    distance = other.projectileDistance(proj)  # The distance between the projectile and the other player
    if distance == 0.0:  # If it's a hit we increase score and go to the next round
        player.increaseScore()
        game.newRound()
    game.nextPlayer()  # Next player's turn


def graphicPlay():
    # Creates the game and the graphical game
    game = Game(10, 3)
    ggame = GameGraphics(game)

    while True:  # To make a loop, only exits when user presses 'Quit'
        angle, vel = graphicInput(game)  # Get user input
        proj = graphicFire(game, ggame, angle, vel)  # Fire a projectile from current player
        graphicFinishShot(game, proj)  # See where the projectile lands
        ggame.sync()  # Sync the graphics


# Run the game with graphical interface
graphicPlay()
