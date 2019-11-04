import unittest
import agent


class TestAgent(unittest.TestCase):

    def test_name(self):
        a = agent.Agent(1, (3, 3))
        self.assertEqual(a.name, 1)
        
        a.name = 2
        self.assertEqual(a.name, 2)        


    def test_position(self):
        a = agent.Agent(1, (3, 3))
        self.assertEqual(a.position, (3, 3))
        
        a.position = (2, 2)
        self.assertEqual(a.position, (2, 2))    

    
    def test_position_not_correct_type(self):
        a = agent.Agent(1, (3, 3))
        with self.assertRaises(ValueError):
            a.position = 4
        with self.assertRaises(ValueError):
            a.position = '4'
  

    def test_move_north(self):
        a = agent.Agent(1, (0, 0))
        a.move_north()
        self.assertEqual(a.position, (-1, 0))


    def test_move_north_east(self):
        a = agent.Agent(1, (0, 0))
        a.move_north_east()
        self.assertEqual(a.position, (-1, 1))


    def test_move_east(self):
        a = agent.Agent(1, (0, 0))
        a.move_east()
        self.assertEqual(a.position, (0, 1))


    def test_move_south_east(self):
        a = agent.Agent(1, (0, 0))
        a.move_south_east()
        self.assertEqual(a.position, (1, 1))


    def test_move_south(self):
        a = agent.Agent(1, (0, 0))
        a.move_south()
        self.assertEqual(a.position, (1, 0))


    def test_move_south_west(self):
        a = agent.Agent(1, (0, 0))
        a.move_south_west()
        self.assertEqual(a.position, (1, -1))


    def test_move_west(self):
        a = agent.Agent(1, (0, 0))
        a.move_west()
        self.assertEqual(a.position, (0, -1))


    def test_move_north_west(self):
        a = agent.Agent(1, (0, 0))
        a.move_north_west()
        self.assertEqual(a.position, (-1, -1))


    def test_human(self):
        h = agent.Human(1, (0, 0))
        self.assertEqual(h.name, 1)
        self.assertEqual(h.position, (0, 0))


    def test_zombie(self):
        z = agent.Zombie(1, (0, 0))
        self.assertEqual(z.name, 1)
        self.assertEqual(z.position, (0, 0))


if __name__ == "__main__":
    unittest.main()