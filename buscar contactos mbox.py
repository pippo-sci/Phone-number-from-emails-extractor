# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:55:42 2018

@author: Felipe
"""

import mailbox
from email.header import decode_header
import re

mbox = mailbox.mbox('C:/Users/Felipe/Desktop/Scrap m21/Todo el correo, incluido Spam y Papelera-001.mbox')

def getbody(message): #getting plain text 'email body'
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


mbox = mailbox.mbox('C:/Users/Felipe/Desktop/Scrap m21/Todo el correo, incluido Spam y Papelera-001.mbox')
regex = re.compile('()[0-9]{4}')
asunto = []
origen = []
texto = []
exp = decode_header(mbox[9025]['subject'])[0][1]


for message in mbox:   
    if message['subject'] is not None:
        sub, code = decode_header(message['subject'])[0]
    else:
        sub = 'vacio'
        code = None
    if code is not None:
        if code == exp:
            subject = sub.decode('utf-8')
        else:
            subject = sub.decode(code)
    else:
        subject = sub
    asunto.append(subject)
    origen.append(message['From'])
    txt = getbody(message)
    if txt is not None:
        texto.append(getbody(message).decode('latin-1'))
    else:
        texto.append('vacio')

import pandas as pd

df = pd.DataFrame({'asunto':asunto,'origen':origen,'texto':texto})
df2 =df[df['asunto'].str.contains('Alerta de Google')==False].copy()

df2.to_csv("correos paz.csv")

df2 = pd.read_csv("correos paz.csv")

""".str.contains("hello")
import nltk
from nltk.tokenize import word_tokenize

wt =[]
for w in asunto:
    if type(w) is not str:
        w = str(w)
    w2 = w.lower()
    w3 = word_tokenize(w2)
    wt.append(w3)

from itertools import chain

tw2= list(chain(*wt))
stop = nltk.corpus.stopwords.words('Spanish')
tw3 = [w for w in tw2 if w not in stop]


df= nltk.FreqDist(tw3)
"""

r='(\d+( |-)*)*\d{4}'

re.search(r,texto[22222])




for i in df2['texto']:
    if re.search(r,i):
        df2['']
    