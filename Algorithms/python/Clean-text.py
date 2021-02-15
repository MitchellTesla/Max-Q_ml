##Cleaning the text
def clean_text(text):
    text=text.lower()
    text=re.sub(r"he's","he is", text)
    text=re.sub(r"she's","she is",text)
    text=re.sub(r"i'm","i am",text)
    text=re.sub(r"that's","that is",text)
    text=re.sub(r"what's","what is",text)
    text=re.sub(r"where's","where is",text)
    text=re.sub(r"\'ll"," will",text)
    text=re.sub(r"\'ve"," have",text)
    text=re.sub(r"\'re"," are",text)
    text=re.sub(r"\'d"," would",text)
    text=re.sub(r"won't"," will not",text)
    text=re.sub(r"can't"," cannot",text)
    text=re.sub(r"[-()\"#/@;:<>{}+=~|.?,]","",text)
    return text
