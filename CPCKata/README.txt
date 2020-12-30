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

METHODOLOGY:
  The method behind this works like this:

  The checksum is not truly a remainder, it is the decimal value of the quotient, BUT a modulous divided
    by the election date will give that decimal value. 
  The interesting thing about modulus is that, numerically, every number mod x will be between 0 and x-1. 
    so if this is treated like a set [0,x-1]. Not only that, but set inrements in a pattern. For Example:
      1 % 4 = 1
      2 % 4 = 2
      3 % 4 = 3
      4 % 4 = 0
      5 % 4 = 1
      6 % 4 = 2
      7 % 4 = 3
      8 % 4 = 0
      etc.
    To have the remainder be the same, I must increment the dividend by a factor of the divisor
      3 % 4 = 3
      to find the next 2, I must increment the dividend (3) by the divisor (4);  3 + 4 = 7
      7 % 4 = 3
      so 
      3 % 4 = 7 % 4 = 3
    The reason this is important is that to end up with the same checksum, I must be able to "get to" the 
      next dividend in the set that will give me that same remainder.
  With all of that thought out, all I need to do is 
    1. check whether the number of votes cast is large to be manipulated: 
      if there are fewer votes than the divisor, then the set will not repeat anywhere
    2. check to see if the next 'jump' will get Mr. Burgler more votes
      if not, keep jumping until either I run out of votes or Mr. Burgler has more votes

  