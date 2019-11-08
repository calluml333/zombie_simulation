import unittest
from ClassesAndObjects import Agent, Human, Zombie, Environment


#==================================================================#
#-------------------------- Agent Tests ---------------------------#
#==================================================================#

class Tests(unittest.TestCase):

    def test_name(self):
        a = Agent(1, (3, 3))
        self.assertEqual(a.name, 1)     


    def test_name_not_correct_type(self):
        a = Agent(1, (3, 3))
        with self.assertRaises(TypeError):
            a.name = '4'
        with self.assertRaises(ValueError):
            a.name = -1


    def test_position(self):
        a = Agent(1, (3, 3))
        self.assertEqual(a.position, (3, 3))
        
        a.position = (2, 2)
        self.assertEqual(a.position, (2, 2))    

    
    def test_position_not_correct_type(self):
        a = Agent(1, (3, 3))
        with self.assertRaises(TypeError):
            a.position = 4
        with self.assertRaises(ValueError):
            a.position = (1,2,3)


    def test_speed(self):
        a = Agent(1, (3, 3))
        self.assertEqual(a.speed, 0.5)
        
        a.speed = 0.9
        self.assertEqual(a.speed, 0.9)    

    
    def test_speed_not_correct_type(self):
        a = Agent(1, (3, 3))
        with self.assertRaises(ValueError):
            a.speed = 0
        with self.assertRaises(TypeError):
            a.speed = '0.6'
            

    def test_move_position(self):
        a = Agent(1, (0, 0))
        a.move_position((1,1))
        self.assertEqual(a.position, (1, 1))


    def test_human(self):
        h = Human(1, (0, 0))
        self.assertEqual(h.name, 1)
        self.assertEqual(h.position, (0, 0))
        self.assertEqual(h.speed, 0.7)


    def test_zombie(self):
        z = Zombie(1, (0, 0))
        self.assertEqual(z.name, 1)
        self.assertEqual(z.speed, 0.3)

    
    def test_zombie_was_human_true(self):
        z = Zombie(1, (0, 0), was_human=True)
        self.assertEqual(z.was_human, True)


#==================================================================#
#------------------------ Environment Tests -----------------------#
#==================================================================#

    def test_environment(self):
        g = Environment(10,10,50,1) 
        self.assertEqual(g.x, 10)
        self.assertEqual(g.y, 10)
        self.assertEqual(g.n_humans, 50)
        self.assertEqual(g.n_zombies, 1)


if __name__ == "__main__":
    unittest.main()