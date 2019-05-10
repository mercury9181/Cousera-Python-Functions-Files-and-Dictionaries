
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_pos(x):
    c=0
    words=x.split()
    for word in words:
        word= strip_punctuation(word)
        if word in positive_words:
            c=c+1
    return c

def get_neg(x):
    c=0
    words=x.split()
    for word in words:
        word= strip_punctuation(word)
        if word in negative_words:
            c=c+1
    return c

def strip_punctuation(s):
    for x in s:
        if x in punctuation_chars:
            s = s.replace(x, "")
    return s

outfile = open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')


fileconnection = open("project_twitter_data.csv", 'r')

lines = fileconnection.readlines()
print(lines)
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    
    vals = row.strip().split(',')
    row_string = '{},{},{},{},{}'.format(vals[1],vals[2],get_pos(vals[0]),get_neg(vals[0]),get_pos(vals[0])-get_neg(vals[0]))
    outfile.write(row_string)
    outfile.write('\n')


outfile.close()

