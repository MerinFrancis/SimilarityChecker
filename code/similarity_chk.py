import os,sys,codecs,standardize
import urllib, simplejson
from flask import Flask, request, render_template, Response
from collections import defaultdict

STRINGS= [',', '.', '-', '"']

app = Flask(__name__)

@app.route('/')
def hello():    
    return render_template('home.html')


def ngrams(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
	output.append(input[i:i+n])
  return output

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

#file1=open('old.txt').read()
def similarity_chk(inputFile1,inputFile2):
	std_inpt1=standardize.standardize(inputFile1)
	file1=codecs.open(std_inpt1,encoding='utf-8', errors='ignore').read()
	std_inpt2=standardize.standardize(inputFile2)
	file2=codecs.open(std_inpt2,encoding='utf-8', errors='ignore').read()
	ngram1=ngrams(file1, 2) # [['a', 'b'], ['b', 'c'], ['c', 'd']]
	ngram2=ngrams(file2, 2)
	l1 = len(ngram1)
	l2 = len(ngram2)
	print "l1"
	print l1
	print "l2"
	print l2
	interList = [i for i in ngram1 if i in ngram2]
	unionList=ngram1+ngram2
	unionList=uniq(unionList)
	interList=uniq(interList)
	similar = len(interList)
	total = len(unionList)
	print "similar"
	print similar
	print "total"
	print total
	threshold = float (similar) / total
	print "resemblence score "
	print threshold
	return threshold

	


   
@app.route('/start')
def start():
    print "inside"
    inpt1 = request.args.get('inpt1')
    inpt2 = request.args.get('inpt2')
    threshold=similarity_chk(inpt1,inpt2)
    if threshold > 0.7 :
	    output = "The given documents are Similar"
    else:
	   output = "The given documents are Not Similar"
    print output
    json = simplejson.dumps({'data': output,'threshold' : threshold})
    resp = Response(json, status=200, mimetype='application/json')
    print resp
    return resp
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)

