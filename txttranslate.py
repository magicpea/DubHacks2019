# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# Translates some text into a the specified language
def translatetxt(text, target):
    translation = translate_client.translate(text, target_language=target)

    return text, translation['translatedText']

# Prints out the original text and then the translation
def printtranslation():
    print('Text: {}'.format(text))
    print('Translation: {}'.format(translation))


text, translation = translatetxt('Hello, World!', 'el')
printtranslation()

def savetext(translation):
    translatedtext = open('translatedtext.txt','w')
    translatedtext.write(translation)

savetext(translation)
''' 
Language Targets:
Arabic	Standard	ar	
Czech (Czech Republic)	Standard	cs
Danish (Denmark)	Standard	da
Dutch (Netherlands)	Standard	nl		
English (US)	WaveNet	en
Filipino (Philippines)	Standard	fil	
Finnish (Finland)	Standard	fi	
French (Canada)	Standard	fr	
German (Germany)	Standard	de	
Greek (Greece)	Standard	el
Hindi (India)	Standard	hi	
Hungarian (Hungary)	Standard	hu	
Indonesian (Indonesia)	Standard	id	
Italian (Italy)	Standard	it	
Japanese (Japan)	Standard	ja	
Korean (South Korea)	Standard	ko	
Mandarin Chinese	Standard	cmn	
Norwegian (Norway)	Standard	nb
Polish (Poland)	Standard	pl	
Portuguese (Brazil)	Standard	pt	
Russian (Russia)	Standard	ru	
Slovak (Slovakia)	Standard	sk
Spanish (Spain)	Standard	es
Swedish (Sweden)	Standard	sv
Turkish (Turkey)	Standard	tr
Ukrainian (Ukraine)	Standard	uk
Vietnamese (Vietnam)	Standard	vi	
'''

