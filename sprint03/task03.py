import re

def create_account(user_name: str, password: str, secret_words: list):
    if not re.search(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*([@#$*%^!&+=_])).{6,}$', password):
        raise ValueError()

    def check(pas: str, sec_w: list):
        count = 0
        count2 = 0
        sec_w.sort()
        secret_words.sort()
        if pas == password and len(sec_w) == len(secret_words):
            for i in sec_w:
                if i not in secret_words:
                    count += 1
            for i in secret_words:
                if i not in sec_w:
                    count2 += 1
        else:
            return False

        if count > 1 or count2 > 1:
            return False
        else:
            return True

    return check
