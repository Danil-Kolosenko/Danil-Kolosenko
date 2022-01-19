// https://softserve.academy/mod/quiz/review.php?attempt=249044&cmid=3721
  def pretty_message(data):
    pattern = r'(\w+?)\1+'
    return re.sub(pattern, r'\1', data)
