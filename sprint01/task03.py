// https://softserve.academy/mod/quiz/review.php?attempt=248124&cmid=4030&page=2#
  
 def isPalindrome(str):
    dict1 = {}
    lst = []
    k = 0
    one = 0
    for i in range(len(str)):
        lst.append(str[i])

    for i in range(len(lst)):
        dict1[lst[i]] = lst.count(lst[i])

    for i in dict1:
        if dict1[i] % 2 != 0:
            k += 1
        else:
            pass
        if dict1[i] == 1:
            k -= 1
            one += 1
        if one > 1 or k > 1 or (one == 1 and k == 1):
            return False
    return True
