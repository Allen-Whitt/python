import VoteCounter

electionDate = 4 #12*30-4

def calculateVotesToChange():
  # see what votes are in the array cause if B is winning don't change
  mVotes = 0
  bVotes = 0

  # If there are fewer votes than the election date, the set will not repeat and won't have the ability
  # to be manipulated
  if electionDate > VoteCounter.retArr[1]:
    return -2
  for vote in VoteCounter.retArr[0]:
    if str(vote).upper() == 'M':
      mVotes +=1
    else:
      bVotes +=1
  # if Burgler is winning, don't do anything
  if bVotes > mVotes:
    return -1
  
  # to get to the same number remainder of the next set, we must got up by that amount of days in election
  # Return how many votes need to be changed
  for x in range(bVotes, VoteCounter.retArr[1], electionDate):
    if VoteCounter.retArr[1] - x < x:
      return x - bVotes



calculateVotesToChange()

