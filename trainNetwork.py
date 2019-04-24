# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:13:48 2019

@author: Milan
"""
from CNN_Model import ACTIONS
import numpy as np
from collections import deque
import random
import time

GAMMA =0.99 #decay rate
OBESERVATION = 50000 # oberservation before start training 
EXPLORE = 100000
FINAL_EPS = 0.0001
INITIAL_EPS = 0.1
REPLAY_MEMORY =50000 # remember previous steps
BATCH =32
FRAME_PER_ACTION = 1

Q_sa =0
s_t =None

def trainNetwork(model,game_state):
    D = deque()
    #first step do nothing
    do_nothing =np.zeros(ACTIONS)
    do_nothing[0]=1 #0 => do nothin
                    #1 => jump
    x_t,r_0,terminal = game_state.get_state(do_nothing)
    s_t = np.stack((x_t,x_t,x_t,x_t),axis=2).reshape(1,20,40,4)
    
    OBSERVE = OBESERVATION
    epsilon = INITIAL_EPS
    t=0
    while(True):
        loss =0
        
        action_index =0
        r_t =0 #reward at t
        a_t =np.zeros([ACTIONS])
        
        #choose an action epsilon greedy
        if random.random() <= epsilon:
            print("--------Random Action--------")
            action_index = random.randrange(ACTIONS)
            a_t[action_index]=1
        else:
            q= model.predict(s_t)
            max_Q = np.argmax(q) #chosing index with max q values
            action_index = max_Q
            a_t[action_index]=1
            
        #reduce epsilon gradually
        if epsilon > FINAL_EPS and t>OBSERVE:
            epsilon -= (INITIAL_EPS - FINAL_EPS)/EXPLORE
            
        #run the selected action and observed next state and reward
        x_t1,r_t,terminal = game_state.get_state(a_t)
        last_time = time.time()
        x_t1 = x_t1.reshape(1,x_t1.shape[0],x_t1.shape[1],1) #1x20x40x1
        s_t1 = np.append(x_t1,s_t[:,:,:,:3],axis=3)
        
        #store the transition in D
        D.append((s_t,action_index,r_t,s_t1,terminal))
        if len(D) > REPLAY_MEMORY:
            D.popleft()
            
        #only train if done observing; simple a minibatch to train on
        if t > OBSERVE:
            trainBatch(random.sample(D,BATCH),model) 
        s_t = s_t1
        t+=1
        print("TIMESTEP", t, "/ EPSILON", epsilon, "/ ACTION", action_index, "/ REWARD", r_t,"/ Q_MAX " , np.max(Q_sa), "/ Loss ", loss)
        
        
            
        
def trainBatch(minibatch,model):
    
    inputs = np.zeros((BATCH,s_t.shape[1],s_t.shape[2],s_t.shape[3]))  
    targets = np.zeros((inputs.shape[0],ACTIONS))
    loss =0
    
    for i in range(0,len(minibatch)):
        state_t = minibatch[i][0]
        action_t = minibatch[i][1]
        reward_t = minibatch[i][2]
        state_t1 = minibatch[i][3]
        terminal = minibatch[i][4]
        inputs[i:i+1] = state_t
        targets[i]=model.predict(state_t)
        Q_sa = model.predict(state_t1)
        if terminal:
            targets[i,action_t] = reward_t
        else:
            targets[i,action_t]= reward_t + GAMMA * np.max(Q_sa)
        loss += model.tain_on_batch(inputs,targets)
        
        
        