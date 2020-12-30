Greetings!

This program fulfills the kata outlined in 'McDonaldVsBurgler.txt'. It is written using python 3.8.5

The first program is VoteCounter.py. This program acts as the legitimate counter of votes. It calculates
  the checksum and lenght of the array of votes.

To use it, you may do one of two things:

1: Simply run the program! I have created it such that it will allow you to manually enter votes one at
  a time. It will reject invalid votes, and accept valid votes in either upper or lower case.

2: Run the program with a command line argument that has the votes in a comma separated list. The list:
  1: can have upper and lower case letters
  2: cannot contain spaces ('R,B' is valid, while 'M, B' is invalid)
  3: cannot contain any invalid votes. Invalid votes in a list will result in an invalid collection of
    votes.

The second program is TheBurglator.py (bərɡ·lei·tr). This program is designed to manipulate the votes 
  coming from VoteCounter.py. This program will run VoteCounter on it's own and can accept a command line
  argument or allow for manual entry.