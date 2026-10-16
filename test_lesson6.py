import unittest
import lesson6 as m

class LessonTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(list(m.TrafficLight().running(lambda _:None)),["red","yellow","green"])
        self.assertEqual(m.Road(20,5000).asphalt_tons(),12500)
        self.assertEqual(m.Position("A","B","Dev",100,10).get_total_income(),110)
        self.assertIn("speeding",m.TownCar(61,"red","Car").show_speed())
        self.assertNotIn("speeding",m.WorkCar(40,"red","Car").show_speed())

if __name__ == "__main__":
    unittest.main()
