//https://softserve.academy/mod/quiz/review.php?attempt=249044&cmid=3721
  
import re

def max_population(lst):
    dict, list = {}, []
    for i in range(1, len(data) - 1):
        dict[i] = data[i].split(",")[1], int(data[i].split(",")[2])
        list.append(int(data[i].split(",")[2]))

    res = list.index(max(list)) + 1

    return dict.get(res)
