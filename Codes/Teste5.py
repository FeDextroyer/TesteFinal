import nltk
from itertools import permutations
import unittest
from flask import Flask

app = Flask(__name__)

class AnagramGenerator:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('rslp')
        self.pt_stopwords = set(nltk.corpus.stopwords.words('portuguese'))
        self.pt_words = set(nltk.corpus.words.words('portuguese'))

    def is_valid_word(self, word):
        return word.lower() in self.pt_words and word.lower() not in self.pt_stopwords

    def generate_anagrams(self, text):
        text = ''.join(ch.lower() for ch in text if ch.isalpha() or ch.isspace())
        words = [word for word in text.split() if self.is_valid_word(word)]
        anagrams = set()
        for word in words:
            anagrams.update(' '.join(p) for p in permutations(word))
        return anagrams

# Testes unitários
import unittest

class TestAnagramGenerator(unittest.TestCase):
    def setUp(self):
        self.anagram_generator = AnagramGenerator()

    def test_generate_anagrams_single_word(self):
        anagrams = self.anagram_generator.generate_anagrams('casa')
        self.assertIn('casa', anagrams)
        self.assertIn('saca', anagrams)

    def test_generate_anagrams_phrase(self):
        anagrams = self.anagram_generator.generate_anagrams('uma casa bonita')
        self.assertIn('uma casa bonita', anagrams)
        self.assertIn('casa bonita uma', anagrams)
        self.assertIn('casa uma bonita', anagrams)

    def test_generate_anagrams_invalid_word(self):
        anagrams = self.anagram_generator.generate_anagrams('wxyz')
        self.assertEqual(len(anagrams), 0)

    def test_generate_anagrams_mixed_text(self):
        anagrams = self.anagram_generator.generate_anagrams('12345 olá casa bonita 67890')
        self.assertIn('casa bonita', anagrams)
        self.assertIn('bonita casa', anagrams)

    def test_generate_anagrams_empty_input(self):
        anagrams = self.anagram_generator.generate_anagrams('')
        self.assertEqual(len(anagrams), 0)

if __name__ == "__main__":
    unittest.main()
    