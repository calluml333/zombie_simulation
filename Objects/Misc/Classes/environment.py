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

    def __init__(self, height, width, Human, Zombie, Bat):
        self._height = height
        self._width = width
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

    def handle_collisions(self, population):
        for member_id, member in population.copy().items():
            if member.is_type == 'Human':
                for other_member_id, other_member in population.copy().items():
                    if member != other_member:
                        
                        if self.is_touching(member, other_member):
                            sum_members = member + other_member
                            if sum_members == '0':
                                self.human_killed_zombie(population, other_member_id)
                                break
                            elif sum_members == '1':
                                self.human_to_zombie(population, member_id)
                                break
                            elif sum_members == '2':
                                self.human_get_weapon(population, member_id, other_member_id)
        return population
           
    def human_to_zombie(self, population, human_id):
        if human_id in list(population):
            human = population[human_id]
            human_pos = human.position
            del population[human_id]
        
        new_Zombie = self._Zombie(self._width, self._height, was_human = True)
        new_Zombie.position = human_pos
        new_z_key = max(population.keys()) + 1
        population.update({new_z_key: new_Zombie})

    def human_killed_zombie(self, population, zombie_id):
        if zombie_id in list(population):
            del population[zombie_id]

    def human_get_weapon(self, population, human_id, weapon_id):
        population[human_id].pick_up_weapon(population[weapon_id])
        population[weapon_id].picked_up = True
        population[weapon_id].owner_id = human_id


    @staticmethod
    def check_empty_populations(population):
        human_count = 0
        zombie_count = 0
        for member_id in population:
            if population[member_id].is_type == 'Human':
                human_count += 1
            elif population[member_id].is_type == 'Zombie':
                zombie_count += 1

        if not human_count or not zombie_count:
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

    @staticmethod
    def random_move_agent(agent):
        choice = random.randint(0,4)
        if choice == 0:
            agent.move_north()
        elif choice == 1:
            agent.move_east()
        elif choice == 2:
            agent.move_south()
        elif choice == 3:
            agent.move_west()
            

if __name__ == "__main__":
    pass