import unittest
from animal import Animal
from dog import Dog

class TestAnimals(unittest.TestCase):
    total_points = 0  # Class-level variable to track points

    def test_animal_initialization(self):
        try:
            generic_animal = Animal("Generic", "Unknown")
            self.assertEqual(generic_animal.name, "Generic")
            self.assertEqual(generic_animal.species, "Unknown")
            self.assertEqual(Animal.kingdom, "Animalia")
            TestAnimals.total_points += 10  # Add points for passing this test
            print("test_animal_initialization passed: +10 points")
        except Exception as e:
            print(f"test_animal_initialization failed: {e}")

    def test_animal_speak(self):
        try:
            generic_animal = Animal("Generic", "Unknown")
            with self.assertLogs() as log:
                generic_animal.speak()
            self.assertIn("The animal makes a noise.", log.output[0])
            TestAnimals.total_points += 10  # Add points for passing this test
            print("test_animal_speak passed: +10 points")
        except Exception as e:
            print(f"test_animal_speak failed: {e}")

    def test_animal_str(self):
        try:
            generic_animal = Animal("Generic", "Unknown")
            self.assertEqual(str(generic_animal), "Kingdom: 'Animalia', Name: 'Generic', Species: 'Unknown'")
            TestAnimals.total_points += 10  # Add points for passing this test
            print("test_animal_str passed: +10 points")
        except Exception as e:
            print(f"test_animal_str failed: {e}")

    def test_dog_initialization(self):
        try:
            buddy = Dog("Buddy", "Canine", "Golden Retriever")
            self.assertEqual(buddy.name, "Buddy")
            self.assertEqual(buddy.species, "Canine")
            self.assertEqual(buddy.breed, "Golden Retriever")
            TestAnimals.total_points += 10  # Add points for passing this test
            print("test_dog_initialization passed: +10 points")
        except Exception as e:
            print(f"test_dog_initialization failed: {e}")

    def test_dog_speak(self):
        try:
            buddy = Dog("Buddy", "Canine", "Golden Retriever")
            with self.assertLogs() as log:
                buddy.speak()
            self.assertIn("The dog barks.", log.output[0])
            TestAnimals.total_points += 10  # Add points for passing this test
            print("test_dog_speak passed: +10 points")
        except Exception as e:
            print(f"test_dog_speak failed: {e}")

    def test_dog_str(self):
        try:
            buddy = Dog("Buddy", "Canine", "Golden Retriever")
            self.assertEqual(str(buddy), "Kingdom: 'Animalia', Name: 'Buddy', Species: 'Canine', Breed: 'Golden Retriever'")
            TestAnimals.total_points += 10  # Add points for passing this test
            print("test_dog_str passed: +10 points")
        except Exception as e:
            print(f"test_dog_str failed: {e}")

    def test_all_animals(self):
        try:
            Animal.all_animals = []  # Reset list for testing
            generic_animal = Animal("Generic", "Unknown")
            buddy = Dog("Buddy", "Canine", "Golden Retriever")
            self.assertIn(generic_animal, Animal.all_animals)
            self.assertIn(buddy, Animal.all_animals)
            self.assertEqual(len(Animal.all_animals), 2)
            TestAnimals.total_points += 10  # Add points for passing this test
            print("test_all_animals passed: +10 points")
        except Exception as e:
            print(f"test_all_animals failed: {e}")

    @classmethod
    def tearDownClass(cls):
        print(f"\nTotal Points: {cls.total_points}/70")
        if cls.total_points == 70:
            print("Congratulations! You passed all tests.")
        else:
            print("Keep working on the tasks to improve your score.")

if __name__ == "__main__":
    unittest.main()
