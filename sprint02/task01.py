// https://softserve.academy/mod/quiz/review.php?attempt=249044&cmid=3721
def double_string(data):
    counter = 0
    for i in range(len(data)):
        if len(data[i]) % 2 == 0:
            if data.count(data[i][:len(data[i])]) > 0 or \
                    (data[i][:int(len(data[i])/2)] in data and data[i][int(len(data[i])/2) + 1:] in data):
                counter += 1
    return counter - 2
