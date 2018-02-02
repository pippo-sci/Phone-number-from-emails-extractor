# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:55:42 2018

@author: Pippo Ramos
"""

import mailbox
from email.header import decode_header
import re

# function to getting plain text 'email body'
def getbody(message): 
    body = None
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    elif message.get_content_type() == 'text/plain':
        body = message.get_payload(decode=True)
    return body


mbox = mailbox.mbox('~/Todo el correo, incluido Spam y Papelera-001.mbox')

#get lists with subject, from and body text from emails

subject = []
from = []
text = []
exp = decode_header(mbox[9025]['subject'])[0][1] # Getting 'unkown-8bit' error to avoid it from a sample

for message in mbox:   
    if message['subject'] is not None:
        sub, code = decode_header(message['subject'])[0]
    else:
        sub = 'empty'
        code = None
    if code is not None:
        if code == exp:
            subject0 = sub.decode('utf-8')
        else:
            subject0 = sub.decode(code)
    else:
        subject = sub
    subject.append(subject0)
    from.append(message['From'])
    txt = getbody(message)
    if txt is not None:
        text.append(getbody(message).decode('latin-1'))
    else:
        text.append('empty')

# Turn the data into dataframe to analyse it 

import pandas as pd

df = pd.DataFrame({'asunto':asunto,'origen':origen,'texto':texto})
df2 =df[df['asunto'].str.contains('Alerta de Google')==False].copy()

#save process in csv file
df2.to_csv("correos.csv")
#df2 = pd.read_csv("correos.csv")

# Lets count most frequent words in subject
import nltk
from nltk.tokenize import word_tokenize
from itertools import chain

wt =[]
for w in asunto:
    if type(w) is not str:
        w = str(w)
    w2 = w.lower()
    w3 = word_tokenize(w2)
    wt.append(w3)

tw2= list(chain(*wt))
stop = nltk.corpus.stopwords.words('Spanish')
tw3 = [w for w in tw2 if w not in stop]

df= nltk.FreqDist(tw3)

print(df.most_common())

#Found the two words before any phone number

r='(\d+( |-)*)*\d{4}' #regex to locate phone numbers in most common formats in the emails


re.search(r,texto[22222])

for i in df2['texto']:
    if re.search(r,i):
        df2['']
    
