from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_determiner = [ "bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit",  "woman"]

    for _ in range(12):
         words = get_noun (1)
         assert words in single_determiner
    
    plural_determiner =  [ "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women" ]

    for _ in range(20):
        words = get_noun(2)
        assert words in plural_determiner

def test_get_verb():
    past_verb =  [ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    present_verb =  [ "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    future_verb =  [ "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(20):
       
       words = get_verb(1, 1)
       assert words in words
       assert past_verb 
       assert  present_verb
       assert  future_verb


def test_get_preposition():
    for _ in range(30):
        preposition = get_preposition(1)
        assert preposition in preposition

def test_get_preposition_phrase():
    for i in range(1):

        prepostion = get_preposition(1)
        determiner  = get_determiner(1)
        noun = get_noun(1)
        prepostion_phrase = (prepostion, determiner, noun)
        assert prepostion_phrase

pytest.main(["-v", "--tb=line", "-rN", __file__])