#Creating a LIST for conversations   
coversation_ids=[]
for conversation in conversations[:-1]:
    _conversation=conversation.split(" +++$+++ ")[-1][1:-1].replace("'","").replace(" ","")
    coversation_ids.append(_conversation.split(","))
