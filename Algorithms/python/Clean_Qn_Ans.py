#Cleaning Questions
Clean_questions=[]
for question in Questions:
    _question1=clean_text(question)
    Clean_questions.append(_question1)
    
#Cleaning Answers
Clean_answers=[]
for answer in Answers:
    _answer1=clean_text(answer)
    Clean_answers.append(_answer1)
