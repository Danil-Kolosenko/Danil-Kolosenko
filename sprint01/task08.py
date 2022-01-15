// https://softserve.academy/mod/quiz/review.php?attempt=248124&cmid=4030&page=7#
  
  def studying_hours(a):
    counter = 0
    lst = []
    for i in range(len(a)-1):
        if a[i] <= a[i+1]:
            counter += 1
        else:
            lst.append(counter)
            counter = 0
    lst.append(counter)
    return max(lst) + 1
