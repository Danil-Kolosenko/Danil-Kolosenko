//https://softserve.academy/mod/quiz/review.php?attempt=248124&cmid=4030&showall=0

def kthTerm(n, k):
    lst_res = []
    lst = []
    for i in range(10):
        lst_res.append(n**i)

        if i > 0:
            for j in range(len(lst)):
                lst_res.append(n**i+lst[j])

        if len(lst_res) > 100:
            break
        lst = []

        for i in lst_res:
            lst.append(i)
    return lst_res[k-1]
