// https://softserve.academy/mod/quiz/review.php?attempt=248124&cmid=4030&page=3#
  
  def findPermutation(n, p, q):
    res = []
    for i in range(n):
        a = q[i]
        pr_i = q[i]
        res.append(p.index(pr_i))
    new_list = [x+1 for x in res]
    return new_list
