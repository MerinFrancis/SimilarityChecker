# -*- coding: utf-8 -*-


import sys  
import codecs  
import os  
import string

      
def stem(text):
        result = ""
    	rulesDict = None
        if rulesDict == None:
            rulesDict = LoadRules()
        words=text.split(" ")
        word_count=len(words)
        result_dict = dict()
        word_iter=0
        word=""
        while word_iter < word_count:
	    
            word = words[word_iter]
	    if('+' not in word):
			    word_length = len(word)
			    suffix_pos_itr = 2
			    word_stemmed=""
			    while suffix_pos_itr < word_length :
				suffix = word[suffix_pos_itr:word_length]
				if suffix in rulesDict:
				    word_stemmed= word[0:suffix_pos_itr] +  rulesDict[suffix]
				    break;
				suffix_pos_itr = suffix_pos_itr+1    
				   
			    if(word_stemmed==""):
				word_stemmed=word
			    result_dict[ word ] = word_stemmed
	    else:
		    
	            result_dict[ word ] = word
	    word_iter = word_iter+1
        return result_dict

def LoadRules():    
        #print "Loading the rules..."
        rules_dict = dict()
        line = []
        line_number = 0
        rule_number = 0
        rules_file = codecs. open('inflection.rules',encoding='utf-8', errors='ignore')
        while 1:
            line_number = line_number +1 
            text = unicode( rules_file.readline())
            if text == "":
                break
            if text[0] == '#': 
                continue  #this is a comment - ignore
            text = text.split("#")[0]   #remove the comment part of the line     
            line_number = line_number +1       
            line = text.strip()  # remove unwanted space
            if(line == ""):
                continue 
            if(len(line.split("=")) != 2):
                print "[Error] Syntax Error in the Rules. Line number: ",  line_number
                print "Line: "+ text
                continue 
            lhs = line.split("=")[0].strip()
            rhs = line.split("=")[1].strip()
            if(len(rhs)>0):
                if(lhs[0]=='"'):
                    lhs=lhs[1:len(lhs)] # if the string is "quoted"
                if(lhs[len(lhs)-1]=='"'):
                    lhs=lhs[0:len(lhs)-1] # if the string is "quoted"
            if(len(rhs)>0):
                if(rhs[0]=='"'):
                    rhs=rhs[1:len(rhs)]  # if the string is "quoted"
                if(rhs[len(rhs)-1]=='"'):
                    rhs=rhs[0:len(rhs)-1]     # if the string is "quoted"            
            rule_number=rule_number+1
            rules_dict[lhs]=rhs
            #print "[", rule_number ,"] " +lhs + " : " +rhs
        #print "Found ",rule_number, " rules."
        return rules_dict

