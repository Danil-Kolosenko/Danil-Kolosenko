import random

def randomWord(lst):
    if len(lst) != 0:
        while True:
            random.shuffle(lst)
            for i in range(len(lst)):
                yield lst[i]
    else:
        yield None
