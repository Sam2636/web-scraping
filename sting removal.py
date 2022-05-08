def clean_str(string):
    string = re.sub(r"\\", "", string)    
    string = re.sub(r"\'", "", string)    
    string = re.sub(r"\"", "", string)    
    return string.strip().lower()

texts = [];labels = []

for i in range(df.message.shape[0]):
    text = BeautifulSoup(df.message[i])
    texts.append(clean_str(str(text.get_text().encode())))

for i in df['class']:
    labels.append(i)