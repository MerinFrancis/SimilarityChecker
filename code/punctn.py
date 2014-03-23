
import os,sys,codecs,string
def punctnRem(text): 

		for punct in string.punctuation:
			text = text.replace(punct," ")
			words = text.encode('utf-8').split()

		for dig in string.digits:
			text = text.replace(dig," ")
			words = text.encode('utf-8').split()


		return words






