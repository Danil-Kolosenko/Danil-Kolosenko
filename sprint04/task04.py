class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark

class Student:
    def __init__(self):
        self.test_dict = {}


    @property
    def tests_taken(self):
        if not self.test_dict:
            return "No tests taken"
        else:
            return self.test_dict

    def take_test(self, testpaper, answ: list):
        corr = 0
        incorr = 0
        for i in range(len(answ)):
            for j in range(len(testpaper.markscheme)):
                if answ[i] == testpaper.markscheme[j]:
                    corr += 1
                else:
                    incorr += 1
        koef = int(((corr) / len(answ)) * 100 + 0.5)
        pass_mark1 = int(testpaper.pass_mark[:-1])
        if koef >= pass_mark1:
            self.test_dict[testpaper.subject] = f"Passed! ({koef}%)"
        else:
            self.test_dict[testpaper.subject] = f"Failed! ({koef}%)"
