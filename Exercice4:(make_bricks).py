def make_bricks(small, big, goal):
  q=(goal//5)*5
  bigg=big*5
  r=goal-min(q,bigg)
  if r<=small:
    return True
  return False
