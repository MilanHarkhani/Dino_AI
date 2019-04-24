# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:51:01 2019

@author: Milan
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



class game:
    def __init__(self,custom_config=True):
        chrome_option =webdriver.ChromeOptions()
        chrome_option.add_argument("disable-infobars")
        self.driver_path =r"C:/selenium/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.driver_path,options=chrome_option)
        self.driver.set_window_position(x=-10,y=0)
        self.driver.set_window_size(200,300)
        self.driver.get('chrome://dino')
        #modify game before training 
        if custom_config:
            self.driver.execute_script("Runner.config.ACCELERATION=0")
    
    def get_crashed(self):
        return self.driver.execute_script("return Runner.instance_.crashed")
    def get_playing(self):
        return self.driver.execute_script("return Runner.instance_.playing")
    def restart(self):
        self.driver.execute_script("Runner.instance_.restart()")
        time.sleep(0.25)
        
    def press_up(self):
        print('send key up')
        self.driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)
    
    def press_down(self):
        self.driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_DOWN)
    
    def get_score(self):
        score_array = self.driver.execute_script("return Runner.instance_.distanceMeter.digits")
        score =''.join(score_array)
        return int(score)
    
    def pause(self):
        return self.driver.execute_script("return Runner.instance_.stop()")
    def resume(self):
        return self.driver.execute_script("return Runner.instance_.play()")
    def end(self):
        self.driver.close()
        