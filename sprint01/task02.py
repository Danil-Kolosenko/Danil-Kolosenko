// https://softserve.academy/mod/quiz/review.php?attempt=248124&cmid=4030&page=1#
  
  def filterBible(scripture, book, chapter):
    res = []
    for i in range(len(scripture)):
        if book + chapter == scripture[i][:5]:
            res.append(scripture[i])
    return res
