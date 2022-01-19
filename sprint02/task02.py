// https://softserve.academy/mod/quiz/review.php?attempt=249044&cmid=3721
  def morse_number(num):
    morse = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        }
    res = []
    for i in range(len(num)):
        res.append(morse.get(num[i]))
    return " ".join(res)
