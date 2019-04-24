# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:43:44 2019                                                    ---------------

@author: Milan
"""
from game import game
from GameAgent import DinoAgent
from GameStates import Game_state
from CNN_Model import buidmodel
from trainNetwork import trainNetwork
def playGame(observer=False):
    game_ = game()
    dino = DinoAgent(game_)
    game_states = Game_state(dino,game_)
    
    model = buidmodel()
    trainNetwork(model,game_states)
    
if __name__== "__main__":
    playGame()
    
    