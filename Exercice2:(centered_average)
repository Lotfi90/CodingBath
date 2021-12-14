def centered_average(nums):
  r=0
 
  mo=nums[len(nums)-1]
  m=nums[0]
  M=nums[0]
  for i in range (0,len(nums)-1):
    mo=mo+nums[i]
    if min(nums[i],nums[i+1])<m:
      m=min(nums[i],nums[i+1])
    if M<max(nums[i],nums[i+1]):
      M=max(nums[i],nums[i+1])
      
  r=(mo-m-M)//(len(nums)-2)
  return(r)
