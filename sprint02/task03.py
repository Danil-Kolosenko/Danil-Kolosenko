// https://softserve.academy/mod/quiz/review.php?attempt=249044&cmid=3721
  def figure_perimetr(data):
    coordinates = []
    for i in range(len(data)):
        if data[i].isdigit():
            coordinates.append(int(data[i]))
    LB_RB = (((coordinates[0] - coordinates[2]) ** 2) + ((coordinates[1] - coordinates[1]) ** 2)) ** 0.5
    RB_RT = (((coordinates[2] - coordinates[6]) ** 2) + ((coordinates[1] - coordinates[7]) ** 2)) ** 0.5
    LT_RT = (((coordinates[4] - coordinates[6]) ** 2) + ((coordinates[5] - coordinates[7]) ** 2)) ** 0.5
    LT_LB = (((coordinates[4] - coordinates[0]) ** 2) + ((coordinates[5] - coordinates[1]) ** 2)) ** 0.5
    return LB_RB + RB_RT + LT_RT + LT_LB
