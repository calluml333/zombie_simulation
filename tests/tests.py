import unittest
from agent import Agent, Human, Zombie
from environment import Environment


#==================================================================#
#-------------------------- Agent Tests ---------------------------#
#==================================================================#

class Tests(unittest.TestCase):
    
    def test_position(self):
        a = Agent(10, 10)        
        a.x, a.y = 2, 2
        self.assertEqual((a.x, a.y), (2, 2))    
    

    def test_speed(self):
        a = Agent(10, 10)
        self.assertEqual(a._speed, 5)
        
        a._speed = 9
        self.assertEqual(a._speed, 9)    


    def test_speed_not_correct_type(self):
        a = Agent(10, 10)
        with self.assertRaises(ValueError):
            a.speed = 0
        with self.assertRaises(TypeError):
            a.speed = '0.6'


    def test_move_position(self):
        a = Agent(10, 10)
        x, y = a.x, a.y
        a.move_position((1,1))
        self.assertEqual((a.x, a.y), (x+1, y+1))


    def test_color(self):
        a = Agent(10, 10)
        self.assertEqual(a.color, (0,0,0))


    def test_human(self):
        h = Human(10, 10)
        self.assertEqual(h._speed, 7)
        self.assertEqual(h.color, (0,0,255))
        self.assertEqual(type(h), Human)


    def test_zombie(self):
        z = Zombie(10, 10)
        self.assertEqual(z._speed, 3)
        self.assertEqual(z.color, (255,0,0))
        self.assertEqual(type(z), Zombie)


    def test_zombie_was_human_true(self):
        z = Zombie(10, 10, was_human=True)
        self.assertEqual(z.was_human, True)


#==================================================================#
#------------------------ Environment Tests -----------------------#
#==================================================================#

    def test_environment(self):
        g = Environment(10,10, Human, Zombie, 50,1) 
        self.assertEqual(g._height, 10)
        self.assertEqual(g._width, 10)
        self.assertEqual(g._n_humans, 50)
        self.assertEqual(g._n_zombies, 1)


if __name__ == "__main__":
    unittest.main()