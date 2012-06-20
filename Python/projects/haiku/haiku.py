#First Attempt in gather response from hacker news


import json, urllib2, sys, re

#Define Functions

def create_syallables_dict(m):
    """Creates Syallables Dictionary
    """
    s = {}
    for x in range(m):
        y = str(x)
        s[y] = []

    return s

def hacker_news_fetch():
    """Connects to Hacker News and fetches data
    """
    hacker_news_api_url = 'http://api.ihackernews.com/page'
    response = json.load(urllib2.urlopen(hacker_news_api_url))
    hacker_news_process_response(response)


def hacker_news_process_response(response):
    """Creats a list of words from all the titles of hacker news articles
    """
    global clean_word_bank
    global clean_string
    global re_pattern
    
    #iterate over items then titles and split all the words to 
    items = response['items']
    for article in items:
        for title in article['title'].split():
            striped_word = title.strip(clean_string)
            """Adding more cleaning up to words"""
            match = re.search(re_pattern, striped_word)
            if not match:
                encoded_word = striped_word.encode('ascii', 'ignore')
                cleaned_word_bank.append(encoded_word)
            else:
                continue

def rhyme_brain_fetch(word):
    """Makes api call to rhyme brain
    """
    print 'This is the current word '+word
    rhyme_brain_api_url = 'http://rhymebrain.com/talk?function=getWordInfo&word='+word
    response = json.load(urllib2.urlopen(rhyme_brain_api_url))
    rhyme_brain_process_response(response)


def rhyme_brain_process_response(response):
    """Processes the rhyme brian response
    """
    global sylb
    sylb[response['syllables']].append(response['word'])
    

def shuffle_pop_additive(additive):
    """Shuffle through the additives and pop a random one to pass to another function
    """
    shuffle(additive)

    line = shuffle_pop_word(additive)
    return line 

def shuffle_pop_word(additive):
    """Iterate over additives, pop word into array
    """
    global sylb

    line = []
    popped_additive = additive.pop()

    for x in popped_additive:
        if sylb[x]:
            break 



#CONSTANTS
ADDITIVES = {'5':[list('11111'), list('1112'), list('23'), list('113'), list('14'), list('5')],
'7':[list('62'), list('52'), list('511'), list('43'), list('421'), list('4111'), list('331'), list('322'), list('31111'), list('2221')]}


#define global vars


cleaned_word_bank = list()
clean_string = "().,?!|"
sylb = create_syallables_dict(7)
re_pattern = '[0-9]|-|:|;|\'|\"|&'


#start function chain

hacker_news_fetch()

print cleaned_word_bank

#starts chain 
for word in cleaned_word_bank:
    rhyme_brain_fetch(word)

print sylb






















"""
Test Works!
ten_words = raw_word_bank[:10]
print ten_words

for word in ten_words:
    rhyme_brain_fetch(word)


print sylb
"""


"""
# make connection and pull response 
response = json.load(urllib2.urlopen(hacker_news_url))

# iterate over response and split title strings into word bank         
items = response['items']
for x in items:
    for y in x['title'].split():
        #append to word bank
        #add clean string here
        wb.append(y.strip(clean_string))

print wb
print len(wb)
# send requests to rhyme brain and constructs syllable dict

for x in wb:
    rbr = json.load(urllib2.urlopen(rhyme_brain_api+x))
    sylb[rbr['syllables']].append(rbr['word'])


print sylb
"""



