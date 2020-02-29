"""
Module that contains the environment class.
"""

import random
import math
import pygame
import sys

class Environment:
    """
    A class that defines the behaviour of the environment that will be used 
    for the simulation.
    """

    def __init__(self, height, width, Human, Zombie, n_humans, n_zombies):
        self._height = height
        self._width = width
        self._n_humans = n_humans
        self._n_zombies = n_zombies
        self._Human = Human
        self._Zombie = Zombie

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(value) == int or type(value) == float:
            self._height = value
        else:
            raise TypeError("x is required to be either an int or a float")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) == int or type(value) == float:
            self._width = value
        else:
            raise TypeError("y is required to be either an int or a float")
   
    def is_touching(self, agent1, agent2):
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip([agent1.x, agent1.y], [agent2.x, agent2.y])]))
        return  distance < (agent1.size + agent2.size)

    def handle_collisions(self, agents):
        humans, zombies = agents
        new_agent_dicts = []
        for human_id, human in humans.copy().items():
            for other_agents in humans, zombies:
                for other_agent_id, other_agent in other_agents.copy().items():
                    if human != other_agent:
                        
                        if self.is_touching(human, other_agent):
                            sum_agents = human + other_agent
                            if sum_agents == '0':
                                self.human_killed_zombie(zombies, other_agent_id)
                                break
                            elif sum_agents == '1':
                                self.human_to_zombie(humans, zombies, human_id)
                                break
        return humans, zombies

    def human_to_zombie(self, humans_dict, zombies_dict, human_id):
        if human_id in list(humans_dict):
            human = humans_dict[human_id]
            human_pos = human.position
            del humans_dict[human_id]
        
        new_Zombie = self._Zombie(self._width, self._height, was_human = True)
        new_Zombie.position = human_pos
        new_z_key = max(zombies_dict.keys()) + 1
        zombies_dict.update({new_z_key: new_Zombie})

    def human_killed_zombie(self, zombies_dict, zombie_id):
        if zombie_id in list(zombies_dict):
            del zombies_dict[zombie_id]   

    @staticmethod
    def check_empty_populations(*args):
        for population in args:
            if len(population) == 0:
                pygame.quit()
                print('------- Game over -------')
                sys.exit(0)

    @staticmethod
    def check_for_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print('\n ------- Game over -------')
                sys.exit(0)

    @staticmethod
    def move_human(agent):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            agent.move_west()

        if keys_pressed[pygame.K_RIGHT]:
            agent.move_east()

        if keys_pressed[pygame.K_UP]:
            agent.move_north()

        if keys_pressed[pygame.K_DOWN]:
            agent.move_south()

        pygame.display.update()

if __name__ == "__main__":
    pass