import urllib2
from bs4 import *
import sqlite3
from nltk.corpus import wordnet as wn
import nltk.corpus as corpus
import itertools as IT
from itertools import product
import flatten
import en
from difflib import SequenceMatcher
ignorewords=['the','of','to','and','or','a','by','an','in','is','it','what','how','when','where','out','on','if','then','whose','have','has','was','were']


class searcher:
	def __init__(self,dbname):
		self.con=sqlite3.connect(dbname)
		
	def __del__(self):
		self.con.close()
		
	def similar(self,a,b):
		return SequenceMatcher(None,a,b).ratio()
		
	def webpages(self,q):
		new_mean=[]
		dict={}
		webpages=[]
		temp=[]
		keywords=q.split(' ')
		keywords=filter(None,keywords)
		length=len(keywords)
		global ignorewords
		for i in range(0,len(keywords)):
		  if keywords[i] not in ignorewords:	
			syn=wn.synsets(keywords[i])
			dict[keywords[i]]=''
			meanings=[s.lemmas[0].name for s in syn]
			meanings=[str(item).lower() for item in meanings]
			if en.is_noun(keywords[i]):
				meanings.append(en.noun.plural(keywords[i]))
			if en.is_verb(keywords[i]):
				meanings.append(en.verb.past(keywords[i]))
				meanings.append(en.verb.past_participle(keywords[i]))
				meanings.append(en.verb.present(keywords[i]))
			for item in meanings:
				if self.similar(item,keywords[i])!=1:
					new_mean.append(item)
			if new_mean==[]:
				dict[keywords[i]]=''
				poss=[(k,v) if v else (k,) for k,v in dict.items()]
				temp.append(list(product(*poss)))
			else:
				new_mean=list(set(new_mean)) 
				for j in range(0,len(new_mean)):
					dict[keywords[i]]=new_mean[j] 
					poss=[(k,v) if v else (k,) for k,v in dict.items()]
					temp.append(list(product(*poss)))
			new_mean=[]
		  else:
			length=length-1
		temp=[item for sublist in temp for item in sublist]
		for item in temp:
			if len(item)==length:
				new_mean.append(item)
		new_mean=list(set(new_mean))
		for i in range(0,len(new_mean)):
			if i==0:
				webpages=self.set_of_webpages(new_mean[i])
				#print i,' ',webpages,new_mean[i]
			else:
				temp=self.set_of_webpages(new_mean[i])
				#print i,' ',temp,new_mean[i]
				webpages=list(set(webpages) | set(temp))
		
		return webpages
		
	def set_of_webpages(self,keywords):	
		pages_set=[]		
		for i in range(0,len(keywords)):
			p=self.con.execute("select pages from words where word='%s'" % (keywords[i]))
			pages=p.fetchone()
			if pages!=None:
				temp_pages=pages[0].split(',')
				if i==0:
					pages_set=pages[0].split(',')
				else:
					pages_set=list(set(pages_set) & set(temp_pages))
			else:
				temp_pages=[]
				pages_set=list(set(pages_set) & set(temp_pages))
			
		pages_set=map(int,pages_set)
		return pages_set
