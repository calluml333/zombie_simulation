import random
import math
import pygame
import sys

class Environment:
    """
    A class that defines the behaviour of the environment that will be used 
    for the simulation.
    """

    clock = clock = pygame.time.Clock()
    tick_time = 30

    def __init__(self, height, width, Human, Zombie, Bat):
        self._height = height
        self._width = width
        self._Human = Human
        self._Zombie = Zombie    
        self.game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Zombie Outbreak Game")

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
   
    def draw_environment(self, population):
        self.game_display.fill((0, 0, 0))
        population = self.handle_collisions(population)
        
        for member_id in population:
            member = population[member_id]

            pygame.draw.circle(self.game_display, member.color, (member.x, member.y), member.size)
            
            if member.is_type == 'Human' and member.is_player:
                self.move_human(member)
            
            elif member.is_type == 'Zombie':
                member.hunt_human(population)
                self.random_move_agent(member)

            elif member.is_type == 'Weapon' and member.picked_up:
                member.track_agent(member.owner)

            member.check_bounds()
        pygame.display.update()
        return population

    def generate(self, population):
        while True:
            self.check_for_exit()
            population = self.draw_environment(population)
            self.check_empty_populations(population)
            self.clock.tick(self.tick_time)
  
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
                                self.human_kill_zombie(population, other_member_id)
                                break
                            elif sum_members == '1':
                                self.human_to_zombie(population, member_id)
                                break
                            elif sum_members == '2':
                                population[member_id].pick_up_weapon(population[other_member_id])
                                
        return population
           
    def human_to_zombie(self, population, human_id):
        if human_id in list(population):
            human = population[human_id]
            human_pos = human.position
            human.drop_all_weapons()
            del population[human_id]
        
        new_Zombie = self._Zombie(self._width, self._height, was_human = True)
        new_Zombie.position = human_pos
        new_z_key = max(population.keys()) + 1
        population.update({new_z_key: new_Zombie})
        print('Human has been bitten and is now a Zombie')

    def human_kill_zombie(self, population, zombie_id):
        if zombie_id in list(population):
            del population[zombie_id]
            print('Zombie has been killed by Human')

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