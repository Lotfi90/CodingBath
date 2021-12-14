def sum67(nums):
  stop=0
  i=0
  c=0
  while i<len(nums) :
    if nums[i]==6 and stop==0:
      stop=1
    elif nums[i]==7 and stop==1:
      stop=0
    elif stop==0:
      c+=nums[i]
    i+=1
  return(c)
