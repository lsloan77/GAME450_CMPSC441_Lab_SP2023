''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
import sys
from pathlib import Path
import typing

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.pygame_combat import run_turn, PyGameComputerCombatPlayer;
from lab11.turn_combat import Combat
from lab11.pygame_ai_player import PyGameAICombatPlayer


currentGame = Combat()

player = PyGameAICombatPlayer("AI")
opponent = PyGameComputerCombatPlayer("Computer")


def run_episode()->typing.List[tuple]:
    
    episodeHistory = []

    while player.health > 0 :
        (player_health, opponent_health, reward) = run_turn(currentGame,player,opponent)
        episodeHistory.append(((player_health, opponent_health),player.action, reward))
    
    return episodeHistory
    

print(run_episode())