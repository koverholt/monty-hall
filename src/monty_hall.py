#!/usr/bin/env python

from __future__ import division
import numpy as np

correct_answers = np.zeros(3)
correct_answers_monty = 0
guesses = 10000


def generate():
    x = np.zeros(3)
    location = np.random.randint(3)
    x[location] = 1
    return x


def choose_door(x):
    global correct_answers
    x -= 1
    doors = generate()
    if doors[x] == 1:
        correct_answers[x] += 1
    else:
        pass


def choose_door_monty(x):
    global correct_answers, correct_answers_monty
    doors = generate()
    # print door
    free_door = np.where(doors[1:3] < 1)[0][0] + 1
    if free_door == 1:
        # print "switch to 1"
        new_guess = 2
    elif free_door == 2:
        # print "switch to 2"
        new_guess = 1

    if doors[new_guess] == 1:
        correct_answers_monty += 1
    else:
        pass

for i in range(guesses):
    choose_door(1)
    choose_door(2)
    choose_door(3)
    choose_door_monty(1)

print "Sticking with Door 1: %0.3f" % (correct_answers[0] / guesses)
print "Sticking with Door 2: %0.3f" % (correct_answers[1] / guesses)
print "Sticking with Door 3: %0.3f" % (correct_answers[2] / guesses)
print "Switching (Monty Hall): %0.3f" % (correct_answers_monty / guesses)
