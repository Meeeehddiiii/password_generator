import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    
    def test_generate_password_length(self):
        # Test la longueur du mot de passe
        password = generate_password(8)
        self.assertEqual(len(password), 8)

    def test_generate_password_digits(self):
        # Test si les chiffres sont inclus
        password = generate_password(10, use_digits=True)
        self.assertTrue(any(char.isdigit() for char in password))

    def test_generate_password_specials(self):
        # Test si les caractères spéciaux sont inclus
        password = generate_password(10, use_specials=True)
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_password_no_specials(self):
        # Test si aucun caractère spécial n'est inclus
        password = generate_password(10, use_specials=False)
        self.assertFalse(any(char in string.punctuation for char in password))

if __name__ == "__main__":
    unittest.main()
