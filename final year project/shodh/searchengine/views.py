# Create your views here.
from django.shortcuts import render
import json
import correct
from correct import correct
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from searchengine.models import url_list
import no_rank_search
import sqlite3
import rank
import os,time
from datetime import datetime
q=''
queries=[]
id=0
ignorewords=['the','of','to','and','or','a','by','an','in','is','it','what','how','when','where','out','on','if','then','whose','have','has','was','were']
from difflib import SequenceMatcher

def similar(a,b):
	return SequenceMatcher(None,a,b).ratio()

def search_form(request):
	return render(request, 'search_form.html')
    
def title(soup):
		url_title=soup.title.string
		return url_title
		
def search(request):
	global q,queries,ignorewords
	if 'term' in request.GET and request.GET['term']:
		q = str(request.GET['term'])
		q=q.strip()
		q=q.lower()
		temp=q.split(' ')
		temp=list(set(temp) - set(ignorewords))
		q1=' '.join(temp)
		searcher=no_rank_search.searcher('E:/BEPROJECT/shodh/databases/search.db')
		webpages=searcher.webpages(q)
		ranker=rank.ranker('E:\BEPROJECT\shodh\databases\search.db')
		ranker.get_expert_score(q1,webpages)
		webpages=ranker.get_edge_score(q1,webpages)
		clauses = ' '.join(['WHEN id=%s THEN %s' % (pk, i) for i, pk in enumerate(webpages)])  
		ordering = 'CASE %s END' % clauses  
		urls = url_list.objects.filter(pk__in=webpages).extra(select={'ordering': ordering}, order_by=('ordering',))		
		con=sqlite3.connect('E:/BEPROJECT/shodh/databases/search.db')
		p=con.execute("select query from searchengine_query_score")
		queries=p.fetchall()
		queries=[list(item) for item in queries]
		queries=[item for sublist in queries for item in sublist]
		queries=[str(item) for item in queries]
		if q in queries:
			queries.remove(q)
		if q1 in queries:
			queries.remove(q1)
		simi=[]
		
		for i in range(0,len(queries)):
			simi.append(similar(q,queries[i]))
		queries=[x for (y,x) in sorted(zip(simi,queries))]
		queries=queries[-8:]
		que={}
		for i in range(0,len(queries)):
			a='?term='+queries[i].replace(' ','+')
			que[queries[i]]=a
		temp=q.split(' ')
		temp=[correct(x) for x in temp]
		cquery=' '.join(temp)
		tquery='/search/?term='+'+'.join(temp)
		if cquery==q:
			cquery=''
		return render(request, 'search_results.html',{'urls': urls,'query': q,'cquery':cquery,'ques':que,'queries':queries,'tquery':tquery})
	else:
		return render(request, 'search_form.html', {'error': True})
		
def thanks(request):
	score=1
	global id
	if(request.GET.get('submit_click')):
		con=sqlite3.connect('E:/BEPROJECT/shodh/databases/search.db')
		p=con.execute("select query from searchengine_query_score where query='%s'" %(q))
		queries=p.fetchall()
		if queries==[]:
			p=con.execute("select max(id) from searchengine_query_score")
			id=p.fetchone()[0]
			if id==None:
				p=con.execute("insert into searchengine_query_score values(1,'%s',1)" %(q))
				con.commit()
			else:
				p=con.execute("select max(id) from searchengine_query_score")
				id=p.fetchone()[0]
				id=id+1
				p=con.execute("insert into searchengine_query_score values(%d,'%s',1)" %(id,q))
				con.commit()
		else:
			p=con.execute("select score from searchengine_query_score where query='%s'" %(q))
			score=p.fetchone()[0]
			score=score+1
			p=con.execute("update searchengine_query_score set score=%d where query='%s'" %(score,q))
			con.commit()
		return render(request,'thanks.html')

def display(request,id):
	con=sqlite3.connect('E:/BEPROJECT/shodh/databases/search.db')
	id=int(id)
	p=con.execute("select url_name from searchengine_url_list where url_id=%d" %(id))
	p=str(p.fetchone()[0])
	p=p[8:]
	if True:
		return render(request,p)
		
def autosuggest(request):
	results=[]
	if request.is_ajax():
		q=request.GET.get('term','')
		urlt=url_list.objects.filter(url_title__startswith=q)
		for item in urlt:
			results.append(item.url_title)
		data=json.dumps(results)
	mimetype='application/json'
	return HttpResponse(data,mimetype)