import math 
import pygame
import random
from Objects import Human, Zombie, Bat
from Objects import Environment


n_humans = 1
n_zombies = 5
n_bats = 1
WIDTH = 500
HEIGHT = 500

def create_population(*args):
    key_count = 0
    population = {}
    for population_class in args:
        if population_class.is_type == 'Human':
            for i in range(n_humans):
                population[key_count] = population_class(WIDTH, HEIGHT)
                if i == 0:
                    population[key_count].is_player = True
                key_count += 1
        
        elif population_class.is_type == 'Zombie':
            for i in range(n_zombies):
                population[key_count] = population_class(WIDTH, HEIGHT)
                key_count += 1
        
        elif population_class.is_type == 'Weapon':
            for i in range(n_bats):
                population[key_count] = population_class(WIDTH, HEIGHT)
                key_count += 1
    return population

def main():
    env = Environment(HEIGHT, WIDTH, Human, Zombie, Bat)
    population = create_population(Human, Zombie, Bat)
    env.generate(population)


if __name__ == "__main__":
    main()