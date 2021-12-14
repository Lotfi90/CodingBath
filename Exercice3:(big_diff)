def big_diff(nums):
  m=nums[0]
  M=nums[0]
  for i in range (0,len(nums)-1):
    if min(nums[i],nums[i+1])<m:
      m=min(nums[i],nums[i+1])
    if M<max(nums[i],nums[i+1]):
      M=max(nums[i],nums[i+1])
  return(M-m)
