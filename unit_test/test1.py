import unittest

# Function to be tested
def replace_word(sentence, old_word, new_word):
    return sentence.replace(old_word, new_word)

# Test class
class TestStringMethods(unittest.TestCase):

    # Test replacing one occurrence of a word
    def test_replace_word(self):
        self.assertEqual(replace_word("I love cats", "cats", "dogs"), "I love dogs")
    
    # Test replacing multiple occurrences of a word
    def test_replace_multiple(self):
        self.assertEqual(replace_word("I love cats and cats love me", "cats", "dogs"), "I love dogs and dogs love me")
    
    # Test replacing a word that doesn't exist
    def test_replace_nonexistent(self):
        self.assertEqual(replace_word("I love cats", "birds", "dogs"), "I love cats")
    
    # Test replacing with an empty string
    def test_replace_empty_string(self):
        self.assertEqual(replace_word("I love cats", "cats", ""), "I love ")
    
    # Test replacing with the same word
    def test_replace_same_word(self):
        self.assertEqual(replace_word("I love cats", "cats", "cats"), "I love cats")

# Run the tests
if __name__ == '__main__':
    unittest.main()
