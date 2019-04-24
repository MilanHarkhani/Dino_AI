# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:45:27 2019

@author: Milan
"""
from grab_screen import grab_screen
class Game_state:
    def __init__(self,agent,game):
        self._agent = agent
        self._game=game
    
    def get_state(self,actions):
        score = self._game.get_score()
        reward = 0.1 *score/10 #dynamic reward
        is_over =False #game over
        if actions[1]==1: #else do nothing
            self._agent.jump()
            reward =0.1 *score/11
        image = grab_screen()
        
        if self._agent.is_crashed():
            self._game.restart()
            reward = -11/score
            is_over =True
        return image,reward,is_over
    
        
        