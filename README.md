# dictionary_exercises

## Exercise 1

Given the following dictionary, representing a mapping from names to phone numbers:

    phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
    }

Write code to do the following:

1. Print Elizabeth's phone number.
2. Add an entry to the dictionary: Kareem's number is 938-489-1234.
3. Delete Alice's phone entry.
4. Change Bob's phone number to '968-345-2345'.
5. Print all the phone entries.

**Solution stored in: phonebook_dictionary.py**

## Exercise 2: Nested Dictionaries

```
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
```

1. Write a python expression that gets the email address of Ramit.
2. Write a python expression that gets the first of Ramit's interests.
3. Write a python expression that gets the email address of Jasmine.
4. Write a python expression that gets the second of Jan's two interests.

**Solution stored in: nested_dictionary.py**

## Letter Summary

Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

    $ python letter_summary.py
    Please enter a word: banana
    {'a': 3, 'b': 1, 'n': 2}

**Solution stored in: letter_summary.py**

## Word Summary

Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

    $ python word_summary.py
    Please enter a sentence: To be or not to be
    {'to': 2, 'be': 2, 'or': 1, 'not': 1}

**Solution stored in: word_summary.py**

## Bonus Challenge

Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.

    $ python word_histogram_tally.py

    Please enter a sentence: To be or not to be do be do be do
    The top three words are:
    be: 4
    do: 3
    to: 2

**Solution stored in: word_histogram_tally.py**