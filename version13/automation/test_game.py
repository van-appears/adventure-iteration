import unittest
from game import main
from base.state import reset_state, has_state
from base.map import reset_map

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print("\n====================")
        print(self._testMethodName)
        print("====================")
        reset_state()
        reset_map()

    def create_actions(self, script):
        commands = iter(script.split("\n"))
        def actions():
            command = next(commands).strip()
            print("> TESTING:", command)
            return command
        return actions


    def test_win(self):
        actions = self.create_actions("""
            go north
            open drawers
            take hammer
            smash bottle
            take matches
            go south
            go east
            go north
            read notebook
            go south
            go south
            take candle
            go north
            go east
            go south
            go east
            light candle
            read earthsea
            take key
            go west
            go north
            go north
            open cupboard
            take honey
            go south
            give honey
            open door
        """)

        main(actions)
        self.assertTrue(has_state("escaped"))
        self.assertFalse(has_state("died"))

    def test_bear_death_1(self):
        actions = self.create_actions("""
            attack bear
        """)

        main(actions)
        self.assertFalse(has_state("escaped"))
        self.assertTrue(has_state("died"))

    def test_bear_death_2(self):
        actions = self.create_actions("""
            go north
            open drawers
            take hammer
            smash bottle
            take matches
            go south
            go east
            go north
            read notebook
            go south
            go south
            take candle
            go north
            go east
            go south
            go east
            light candle
            read earthsea
            take key
            go west
            go north
            go north
            open cupboard
            take hotsauce
            go south
            give hotsauce
        """)

        main(actions)
        self.assertFalse(has_state("escaped"))
        self.assertTrue(has_state("died"))

    def test_match_death_1(self):
        actions = self.create_actions("""
            go north
            open drawers
            take hammer
            smash bottle
            take matches
            light match
            light match
            light match
        """)

        main(actions)
        self.assertFalse(has_state("escaped"))
        self.assertTrue(has_state("died"))

    def test_match_death_2(self):
        actions = self.create_actions("""
            go north
            open drawers
            take hammer
            smash bottle
            take matches
            go south
            go east
            go north
            read notebook
            go south
            go south
            take candle
            go north
            go east
            go south
            go east
            light candle
            read earthsea
            take key
            read earthsea
            read earthsea
            read earthsea
        """)

        main(actions)
        self.assertFalse(has_state("escaped"))
        self.assertTrue(has_state("died"))

    def test_match_death_3(self):
        actions = self.create_actions("""
            go north
            open drawers
            take hammer
            smash bottle
            take matches
            go south
            go east
            go north
            read notebook
            go south
            go south
            take candle
            go north
            go east
            go south
            go east
            light candle
            read earthsea
            take key
            go west
            open chest
            open chest
            open chest
        """)

        main(actions)
        self.assertFalse(has_state("escaped"))
        self.assertTrue(has_state("died"))

    def test_match_death_4(self):
        actions = self.create_actions("""
            go north
            open drawers
            take hammer
            smash bottle
            take matches
            go south
            go east
            go north
            read notebook
            go south
            go south
            take candle
            go north
            go east
            go south
            go east
            light candle
            read earthsea
            take key
            go west
            go north
            go east
            go east
            go east
            go east
            go east
            go east
            go east
        """)

        main(actions)
        self.assertFalse(has_state("escaped"))
        self.assertTrue(has_state("died"))

if __name__ == '__main__':
    unittest.main()
