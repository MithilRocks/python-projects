import urllib2
from bs4 import *
import sqlite3
from urlparse import urljoin
import re
# Create a list of words to ignore
ignorewords=['the','of','to','and','or','a','by','an','in','is','it','what','how','when','where','out','on','if','then','whose','have','has','was','were']
count=0
fromtolist=[]
class crawler:
# Initialize the crawler with the name of database
	def __init__(self,dbname):
		self.con=sqlite3.connect(dbname)

	def __del__(self):
		self.con.close()

	def dbcommit(self):
		self.con.commit()
		
	def word_page(self):
		page_string=''
		identity=1
		while True:
			w=self.con.execute("select word from searchengine_word_list where id=%d" % (identity))
			word=w.fetchone()
			if word==None:
				break
			else:
				tw=self.con.execute("select word from words where word='%s'" % (word[0]))
				temp_word=tw.fetchone()
				if temp_word==None:
					ident=self.con.execute("select url_id from searchengine_word_list where word='%s' and id=%d" % (word[0],identity))
					
					temp_ident=ident.fetchone()
					page_string=str(temp_ident[0])
					ins=self.con.execute("insert into words (word,pages) values ('%s','%s')" % (word[0],page_string))
					self.dbcommit()
				else:
					ident=self.con.execute("select url_id from searchengine_word_list where word='%s' and id=%d" % (word[0],identity))
					temp_ident=ident.fetchone()
					p=self.con.execute("select pages from words where word='%s'" % (word[0]))
					temp_pages=p.fetchone()
					page_string=str(temp_pages[0])+','+str(temp_ident[0])
					ins=self.con.execute("update words set pages='%s' where word='%s'" % (page_string,word[0]))
					self.dbcommit()
			identity=identity+1
			
			
# Auxilliary function for getting an entry id and adding
# it if it's not present
	def getentryid(self,table,field,value,url_t,url_te,createnew=True):
		global count
		cur=self.con.execute("select url_id from %s where %s='%s'" % (table,field,value))
		self.dbcommit()
		res=cur.fetchone()
		if res==None:
			count+=1
			url_t=str(url_t)
			temp=url_t[1:]
			cur=self.con.execute("insert into %s (url_id,url_name,url_title,url_text) values(%d,'%s','%s','%s')" % (table,count,value,temp,url_te))
			self.dbcommit()
			return cur.lastrowid
		else:
			return res[0]
			
	def title(self,soup):
		url_title=soup.title.string
		return url_title
		
	def heading(self,soup):
		header=[]
		for section in soup.find_all('h1'):
			temp=section.find_all(text=True)[0].split('.')
			for i in range(len(temp)):
				header+=re.split('[?,.;!]',temp[i])
		return header
		
	def anchortext(self,soup):
		anchor=[]
		for anc in soup.find_all('a',href=True):
			if anc.contents!=[]:
				anchor.append(anc.contents[0])
		return anchor
		
		
# Index an individual page
	def addtoindex(self,url,soup):
		occur=0
		header=0
		title=0
		anch=0
		flag_h=False
		flag_a=False
		
		text=self.gettextonly(soup)
		url_text=text.replace('\n',' ')
		url_text=url_text[:120]+'\n'+url_text[120:200]+'...'
		words=self.separatewords(text)
		words=[str(x) for x in words]
		url_title=self.title(soup)
		url_title=unicode(url_title)
		url_title=str(url_title)
		head=self.heading(soup)
		anchor=self.anchortext(soup)
		urlid=self.getentryid('searchengine_url_list','url_name',url,url_title,url_text)
		
		for j in range(len(words)):
		 if words[j] not in ignorewords:
			cur=self.con.execute("select url_id from searchengine_word_list where url_name='%s' and word='%s'" % (url,words[j]))
			res=cur.fetchone()
			if res==None:
				if words[j] in url_title.lower():
					title=1
				else:
					title=0
					
				for k in range(len(head)):
					head1=head[k]
					head2=head1.lower()
					if words[j] in head2.split():
						flag_h=True
					else:
						header=0
						
				for k in range(len(anchor)):
					anch1=anchor[k]
					anch2=anch1.lower()
					anch3=anch2.split(' ')
					if words[j] in anch3:
						flag_a=True
					else:
						anch=0
				if flag_h: 
					header=1		
				if flag_a:
					anch=1
				occur=words.count(words[j])
				cur=self.con.execute("insert into searchengine_word_list (url_id,url_name,word,no_of_occur,title,header,anchor) values (%d,'%s','%s',%d,%d,%d,%d)" % (urlid,url,words[j],occur,title,header,anch))
				flag_h=False
				flag_a=False
				
			else:
				if words[j] in url_title.lower():
					title=1
				else:
					title=0
					
				for k in range(len(head)):
					head1=head[k]
					head2=head1.lower()
					if words[j] in head2.split():
						flag_h=True
					else:
						header=0
						
				for k in range(len(anchor)):
					anch1=anchor[k]
					anch2=anch1.lower()
					anch3=anch2.split(' ')
					if words[j] in anch3:
						flag_a=True
					else:
						anch=0
				
				occur=words.count(words[j])
				if flag_h:
					header=1
					
				if flag_a:
					anch=1
					
				cur=self.con.execute("update searchengine_word_list set no_of_occur=%d,title=%d,header=%d,anchor=%d where url_name='%s' and word='%s'" % (occur,title,header,anch,url,words[j]))
				flag_h=False
				flag_a=False

		print '%d Indexing %s\n' % (urlid,url)
		
# Extract the text from an HTML page (no tags)
	def gettextonly(self,soup):
		v=soup.string
		if v==None:
			c=soup.contents
			resulttext=''
			for t in c:
				subtext=self.gettextonly(t)
				resulttext+=subtext+'\n'
			return resulttext
		else:
			return v.strip()
		
# Separate the words by any non-whitespace character
	def separatewords(self,text):
		splitter=re.compile('\\W*')
		return [s.lower() for s in splitter.split(text) if s!='']
		
# Return true if this url is already indexed
	def isindexed(self,url):
		u=self.con.execute("select url_id from searchengine_url_list where url_name='%s'" % (url))
		res=u.fetchone()
		if res==None:
			return False
		else:
		        return True
		
# Add a link between two pages
	def addlinkref(self,urlFrom,urlTo,linkText):
		u=self.con.execute("select url_id from searchengine_url_list where url_name='%s'" % (urlFrom))
		res_from=u.fetchone()
		v=self.con.execute("select url_id from searchengine_url_list where url_name='%s'" % (urlTo))
		res_to=v.fetchone()
		res_from_temp=res_from[0]
		res_to_temp=res_to[0]
		w=self.con.execute("insert into searchengine_link (from_id,to_id) values(%d,%d)" % (res_from_temp,res_to_temp))
		self.dbcommit()
				
# Starting with a list of pages, do a breadth
# first search to the given depth, indexing pages
# as we go

	def crawl(self,pages,depth=3):
		for i in range(depth):
			newpages=set()
			for page in pages:
				try:
					c=urllib2.urlopen(page)
				except:
					print "Could not open %s" % page
					continue
				soup=BeautifulSoup(c.read())
				if not self.isindexed(page):
					self.addtoindex(page,soup)

				links=soup('a')
				for link in links:
					if ('href' in dict(link.attrs)):
						url=urljoin(page,link['href'])
						if url.find("'")!=-1: continue
						url=url.split('#')[0] # remove location portion
						c1=urllib2.urlopen(url)
						soup1=BeautifulSoup(c1.read())
						if not self.isindexed(url):
							newpages.add(url)
							self.addtoindex(url,soup1)
						linkText=self.gettextonly(link)
						self.addlinkref(page,url,linkText)
				self.dbcommit()
			pages=newpages

class searcher:
	def __init__(self,dbname):
		self.con=sqlite3.connect(dbname)
		
	def __del__(self):
		self.con.close()
	
	def webpages(self,q):
		pages_set=[]
		keywords=q.split(' ')
		for i in range(0,len(keywords)):
			p=self.con.execute("select pages from words where word='%s'" % (keywords[i]))
			pages=p.fetchone()
			temp_pages=pages[0].split(',')
			if i==0:
				pages_set=pages[0].split(',')
			else:
				pages_set=list(set(pages_set) & set(temp_pages))
			
		pages_set=map(int,pages_set)
		return pages_set
