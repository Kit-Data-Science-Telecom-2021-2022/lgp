#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def get_freq(filename):
  """
  Gets a file as parameter, opens it, splits on white space 
  and fills a dict using the lower case words as keys
  and the number of occurences as values

  Returns a dict 
  """
  d=dict()
  with open(filename) as f:
    c = f.read()
    words=c.split()
    #print(words)
    for w in words:
      wl = w.lower()
      if wl in d.keys():
        d[wl] += 1
      else:
        d[wl] = 1
  return d


def display_freq(d, sorted_by=1, reversed=False, number=0):
  """
  Displays the content of a dict on two columns as follow:
    word1 frequency1
    word2 frequency2

  Parameters
    sorted_by: {0, 1} 
      if set to 0 result will be sorted by word in alphabetic order, 
      if set to 1 it is sorted by frequency
    reversed: {True, False}
      if set to True it will display items in reverse order (alphabetically or descending order)
    number: 
      sets the number of occurences to display (0 far all)
      if number is set to value superior to dict lenght defaults to len(dict))
  
  """
  if number > len(d) or number == 0:
    n = len(d)
  else:
    n = number
  i=0
  l = list()
  for w,f in d.items(): l.append((w, f))
  l.sort(key=lambda x: x[sorted_by], reverse=reversed)
  for w,f in l: 
    if i < n:
      print(w + " " + str(f))
      i+=1
    else:
      return

def print_words(filename):
  d=get_freq(filename)
  # display all words, sorted by alphabetic order, 
  display_freq(d, sorted_by=0, reversed=False, number=0)


def print_top(filename):
  d=get_freq(filename)
  # display 20 words, sorted descending order by frequency
  display_freq(d, sorted_by=1, reversed=True, number=20)


# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
