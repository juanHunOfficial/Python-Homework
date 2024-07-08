def ArrayChallenge(arr):
  import statistics as stats
  #calc the mode
  theMode = stats.mode(arr)
  #calc the mean
  theMean = stats.mean(arr)

  if theMode == theMean:
    return 1
  else:
    return 0

# keep this function call here
print(ArrayChallenge(input()))