from Objects import Human, Zombie, Bat, Sword
from Objects import Environment


WIDTH = 500
HEIGHT = 500
pop_dict = {
    'Human': 1,
    'Zombie': 5,
    'Bat': 2,
    'Sword': 2
}

def create_population(population_numbers, *args):
    key_count = 0
    population = {}
    for population_class in args:
        try:
            n_members = population_numbers[population_class.__name__]
        except:
            n_members = 0
            
        for i in range(n_members):
            population[key_count] = population_class(WIDTH, HEIGHT)
            if population_class.__name__ == 'Human':
                if i == 0:
                    population[key_count].is_player = True
            key_count += 1            
    return population

def main():
    env = Environment(HEIGHT, WIDTH, Human, Zombie, Bat)
    population = create_population(pop_dict, Human, Zombie, Bat, Sword)
    env.generate(population)


if __name__ == "__main__":
    main()
