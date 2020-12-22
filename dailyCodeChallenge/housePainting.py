# Daily Coding Problem 19

houses1 = [[1, 4, 5], [5, 8, 9], [11,4,6]] # 13
houses2 = [[3,9],[4,11],[2,22],[6,1000]]  # 41

# I need to find a way to do it backwards and forwards from the given array. 
# The way I have those array set up is that if you get the cheapest one in the first house,
# you will not end up with the optimal price
#   I will treat one as a node and work back and forward from there
def backIter(arr, pos, choice):
    # array is the house and price array
    # pos is the position that that array exists 
    # choice is the inital choice because we can't choose the same going backwards or forwards
    
    # I can set the int of the next arr element in my current postion to int max
    # that is if I continue down the array
    return x + forIter(pos -1) if pos > 0  else x

def forIter(arr, pos, choice):
    arr[pos-1][choice] = sys.maxint
    for idx in range(0, len(arr))
          if min(arr[pos+1]) == arr[pos][idx]:
            choice = idx
    return x + forIter(arr, pos +1, choice) if pos + 1 < len(arr) else x

def colorChooser(arr):
    for x in range(0, len(arr)):
        for idx in range(0, len(arr[0]))
          if min(x) == arr[x][idx]:
            choice = idx
        print(min(arr(x)) + backIter(arr,x,choice) + forIter(arr,x,choice))

        # I MESSDED THIS UP THEY ARE MATERIXIES