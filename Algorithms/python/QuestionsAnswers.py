##Mapping Questions and Answers
Questions=[]
Answers=[]
for conversation in conversation_ids:
    for i in range(len(conversation)-1):
        Questions.append(id2line[conversation[i]])
        Answers.append(id2line[conversation[i+1]])
