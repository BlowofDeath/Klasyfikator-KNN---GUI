# -*- coding: utf-8 -*-
import math
"""
Created on Tue Apr  7 15:17:15 2020

@author: Tomasz Jabłoński
"""

def euclideanDistance(sample_one, sample_two):
    distance =0
    for i in range(len(sample_one)):
        distance+= pow(sample_one[i] - sample_two[i],2)
    return math.sqrt(distance)

def manhattanDistance(sample_one, sample_two):
    distance =0
    for i in range(len(sample_one)):
        distance+= abs(sample_one[i] - sample_two[i])
    return distance
    
#metryka czbyszewa
def chessboardDdistance(sample_one, sample_two):
    distance = []
    for i in range(len(sample_one)):
        distance.append(abs(sample_one[i] - sample_two[i])) 
    return max(distance)

def minkowskiDistance(sample_one, sample_two, p):
    distance =0
    for i in range(len(sample_one)):
        distance+= pow(abs(sample_one[i] - sample_two[i]),p)
    return (distance/p)

def logDistance(sample_one, sample_two):
    distance =0
    for i in range(len(sample_one)):
        if sample_one[i] <= 0:
            print(sample_one)
        distance+= abs(math.log(sample_one[i]) - math.log(sample_two[i]))
    return distance

