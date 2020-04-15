#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dice rolling simulator

"""
#import packages

from random import randint

while True:
    #getting value from user
    choice = input("Do you want to roll the dice ? (y/n)").lower()
    
    if choice=="y":
        print("Dice rolled",randint(1, 6))
        continue
    
    else:
        print("Game is closing")
        break #break the loop