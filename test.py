#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Dice rolling simulator

import random

question = input("Would you like to roll the dice? [y/n]")

if question.lower () == "n":
    print ("bye bye")

while question.lower () == "y":
    number = random.randint(1,6)
    print (number)
    print ("Would you like to roll again?")
    print (number)
    exit()
