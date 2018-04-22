import urllib2
from bs4 import *
import sqlite3
from urlparse import urljoin
import re
expert_score=[]
exclude=['co','uk','in','com','edu','net','pk','org']

class ranker:
	def __init__(self,dbname):
		self.con=sqlite3.connect(dbname)
		
	def __del__(self):
		self.con.close()
		
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
			anchor.append(anc.contents[0])
		return anchor
		
	def fullnessfactor_keyphrase(self,q,title):
		keywords=q.split(' ')
		keywords=filter(None,keywords)
		title=title.lower().strip()
		title=str(title)
		title_words=title.split(' ')
		word=list(set(title_words) - set(keywords))
		len_word=len(word)
		if len(word)<=2 and len(word)>=1:
			return 1
		elif len(word)==0:
			return 0
		else:
			result=1-float((len_word-2))/len(title_words)
			return result
	
	def fullnessfactor(self,q,page):
		title=16
		heading=6
		anchor=1
		c=urllib2.urlopen(page)
		soup=BeautifulSoup(c.read())
		url_title=self.title(soup)
		head=self.heading(soup)
		anchor=self.anchortext(soup)
		m_title=self.fullnessfactor_keyphrase(q,url_title)
		head=filter(None,head)
		head=[str(item).lower() for item in head]
		m_head=[]
		for i in range(0,len(head)):
			temp=self.fullnessfactor_keyphrase(q,head[i])
			m_head.append(temp)
		anchor=filter(None,anchor)
		anchor=[str(item).lower() for item in anchor]
		m_anchor=[]
		for i in range(0,len(anchor)):
			temp=self.fullnessfactor_keyphrase(q,anchor[i])
			m_anchor.append(temp)
		m_title=16*m_title 
		m_head=[m_head[i] * heading for i in range(len(m_head))]
		fullness_factor_score=m_title+sum(m_head)+sum(m_anchor) #This is where expert_score is calculated
		return fullness_factor_score
		
	def get_expert_score(self,q,webpages):
		global expert_score
		for webpage in webpages:
			url=self.con.execute("select url_name from searchengine_url_list where url_id=%d" % (webpage))
			url_name=url.fetchone()
			expert_score.append(self.fullnessfactor(q,url_name[0]))

        def no_of_key_phrases(self,keyword,target):
                summation=0
                c=urllib2.urlopen(target)
		soup=BeautifulSoup(c.read())
		url_title=self.title(soup)
		head=self.heading(soup)
		anchor=self.anchortext(soup)
                url_title=url_title.lower().strip()
		url_title=str(url_title)
		title_words=url_title.split(' ')
		if keyword in title_words:
                        summation=summation+1
                head=filter(None,head)
		head=[str(item).lower() for item in head]
		for i in range(0,len(head)):
                        temp_head=head[i]
                        temp_head=temp_head.split(' ')
                        temp_head=filter(None,temp_head)
                        if keyword in temp_head:
                                summation=summation+1
                anchor=filter(None,anchor)
		anchor=[str(item).lower() for item in anchor]
		for i in range(0,len(anchor)):
                        temp_anc=anchor[i]
                        temp_anc=temp_anc.split(' ')
                        temp_anc=filter(None,temp_anc)
                        if keyword in temp_anc:
                                summation=summation+1
		return summation
		
        def edge_score(self,expert,target,q,webpages):
                global edge_score
                idn=self.con.execute("select url_id from searchengine_url_list where url_name='%s'" % (expert))
                expert_id=list(idn.fetchone())
                ind=webpages.index(expert_id[0])
                summation=0
                keywords=q.split(' ')
		keywords=filter(None,keywords)
                for keyword in keywords:
                        summation=summation+self.no_of_key_phrases(keyword,target)
                edge_score=expert_score[ind]*summation
                return edge_score
			
	def get_edge_score(self,q,webpages):
		edge_score=0
		temp=[]
		temp_list=[]
		index=0
		k=0
		m=0
		temp_webpage=list(webpages)
		temp_webpage.insert(0,0)
		matrix=[temp_webpage]
		aff_matrix=[]
		targ_exam=[]
		for webpage in webpages:
			temp_list.append(webpage)
			to=self.con.execute("select to_id from searchengine_link where from_id=%d" % (webpage))
			to_id=list(to.fetchall())
			temp=[list(to_id[i]) for i in range(len(to_id))]
			temp=sum(temp,[])
			link=list(set(temp)&set(webpages))
			if not link:
                                for i in range(len(webpages)):
                                               temp_list.append(0)
                        else:
                                for i in range(len(webpages)):
                                               temp_list.append(0)
                                for i in range(len(link)):
                                               exp=self.con.execute("select url_name from searchengine_url_list where url_id=%d" % (webpage))
                                               expert_url=list(exp.fetchone())
                                               tar=self.con.execute("select url_name from searchengine_url_list where url_id=%d" % (link[i]))
                                               target_url=list(tar.fetchone())
                                               edge_score=self.edge_score(str(expert_url[0]),str(target_url[0]),q,webpages)
                                               if link[i] in matrix[0]:
                                                       index=matrix[0].index(link[i])
                                                       temp_list[index]=edge_score
                        matrix.append(temp_list)
			temp_list=[]
			
		for i in range(1,len(matrix)):
			m=1
			k=1
			for j in range(len(matrix)):  
					k=k+1
					if (k<len(matrix)):
						exp1=matrix[m][0]
						exp2=matrix[k][0]
						exp=self.con.execute("select url_name from searchengine_url_list where url_id=%d" % (exp1))
						expert_url1=list(exp.fetchone())
						exp=self.con.execute("select url_name from searchengine_url_list where url_id=%d" % (exp2))
						expert_url2=list(exp.fetchone())
						a=expert_url1[0].split('.')
						b=expert_url2[0].split('.')											   
						aff=list(set(a) & set(b))
						if len(aff)>2:
							if (matrix[m][i]>matrix[k][i]):
								matrix[k][i]=0
							else:
								matrix[m][i]=0
								m=k
								m=m-1
		for x in zip(*matrix[1:]):
			targ_exam.append(sum(x))
		if targ_exam!=[]:	
			targ_exam.pop(0)
		#targ_exam=self.wordf(q,targ_exam,webpages)
		sort=[x for (y,x) in sorted(zip(targ_exam,webpages))]
		sort=sort[::-1]
		return sort

	def wordf(self,q,targ,webp):
		q=q.split(' ')
		count=0
		occur=0
		for i in range(0,len(webp)):
			for j in range(0,len(q)):
				p=self.con.execute("select no_of_occur from searchengine_word_list where url_id=%d and word='%s'" %(webp[i],q[j]))
				word=p.fetchone()
				if word!=None:
					count=count+p.fetchone()[0]
			occur=1-(count/100.00)
			targ[i]=targ[i]*occur
			count=0
		return targ