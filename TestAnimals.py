import unittest
from unittest.mock import patch
from io import StringIO
from animal import Animal
from dog import Dog

class TestAnimals(unittest.TestCase):
    total_points = 0  # Class-level variable to track points
    user_name = ""  # Class-level variable to store the user's name

    @classmethod
    def setUpClass(cls):
        # Ask for the user's name before tests start
        cls.user_name = input("What is your name?")

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

    @patch('sys.stdout', new_callable=StringIO)  # Mock stdout to capture print output
    def test_animal_speak(self, mock_stdout):
        try:
            generic_animal = Animal("Generic", "Unknown")
            generic_animal.speak()
            output = mock_stdout.getvalue().strip()  # Capture printed output
            self.assertEqual(output, "The animal makes a noise.")
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

    @patch('sys.stdout', new_callable=StringIO)  # Mock stdout to capture print output
    def test_dog_speak(self, mock_stdout):
        try:
            buddy = Dog("Buddy", "Canine", "Golden Retriever")
            buddy.speak()
            output = mock_stdout.getvalue().strip()  # Capture printed output
            self.assertEqual(output, "The dog barks.")
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
        # Print the total points and the user's name
        print(f"\nTotal Points: {cls.total_points}/70")
        print(f"Great job, {cls.user_name}!")
        if cls.total_points == 70:
            print("Congratulations! You passed all tests.")
        else:
            print("Keep working on the tasks to improve your score.")

if __name__ == "__main__":
    unittest.main()
