// https://softserve.academy/mod/quiz/review.php?attempt=248124&cmid=4030&page=6#
  
  def Cipher_Zeroes(N):
    points = 0
    for i in range(len(N)):
        if N[i] in "069":
            points += 1
        elif N[i] == "8":
            points += 2
        else:
            pass

    if points % 2 == 0 and points != 0:
        points -= 1
    elif points % 2 != 0:
        points += 1
    res = bin(points)
    return res[2:]
