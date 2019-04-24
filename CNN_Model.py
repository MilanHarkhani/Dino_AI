# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:46:33 2019

@author: Milan
"""

from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten,Activation
from keras import optimizers

LEARNING_RATE =1e-4
img_rows, img_cols =40,20
img_channels =4 #stack 4 frames
ACTIONS =2

def buidmodel():
    print("building a model..")
    model = Sequential()
    model.add(Conv2D(32,(8,8),strides=(4,4),padding='same',input_shape=(img_cols,img_rows,img_channels)))
    model.add(Activation('relu'))
    model.add(Conv2D(64,(4,4),strides=(2,2),padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64,(3,3),strides=(1,1),padding='same'))
    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dense(ACTIONS))
    adam = optimizers.Adam(lr=LEARNING_RATE)
    model.compile(loss='mse',optimizer=adam)
    print("model created sucessfully")
    return model
