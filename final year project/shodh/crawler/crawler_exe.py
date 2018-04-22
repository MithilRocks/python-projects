import crawler_prog
import sqlite3
import os
fn=os.path.dirname(os.getcwd())+'\\databases\\search.db'
con=sqlite3.connect(fn)
con.execute("delete from searchengine_url_list")
con.commit()
con.execute("vacuum")
con.commit()
con.execute("delete from searchengine_word_list")
con.commit()
con.execute("vacuum")
con.commit()
con.execute("delete from searchengine_link")
con.commit()
con.execute("vacuum")
con.commit()
con.execute("delete from words")
con.commit()
con.execute("vacuum")
con.commit()
con.execute("delete from searchengine_query_score")
con.commit()
con.execute("vacuum")
con.commit()
con.close()
pagelist=['file:///E:/BEPROJECT/websites_collection/New/www.actors.com/katewinslet.html','file:///E:/BEPROJECT/websites_collection/New/www.actors.in/katewinslet.html']
crawler=crawler_prog.crawler(fn)
crawler.crawl(pagelist)
crawler.word_page()
