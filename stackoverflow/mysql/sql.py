import json
import pymysql

conn = pymysql.connect(host = "localhost",port = 3306,user = "root",passwd = "0303",db = "chenx",charset="utf8")
cur = conn.cursor()

with open(r"e:\python\stackoverflow\data2.json","r",encoding="utf-8") as f:
    data = json.load(f)

    def insert_db(s_links, s_views, s_votes, s_answers, s_tags, s_questions):
        """" Insert data to database """

        sql = "insert into stackoverflow(s_links, s_views, s_votes, s_answers, s_tags, s_questions) " \
              "values(%s, %s, %s, %s, %s, %s)"
        value = (s_links, s_views, s_votes, s_answers, s_tags, s_questions)
        cur.execute(sql, value)
        conn.commit()
        print(s_links + " Done")
        print("Insert s_links: " + s_links)

    for i in range(len(data)):
        s_links = data[i]['links']
        s_views = data[i]['views']
        s_votes = data[i]['votes']
        s_answers = data[i]['answers']
        s_tags = " ".join(data[i]['tags'])
        s_questions = data[i]['questions']
        try:
            insert_db(s_links, s_views, s_votes, s_answers, s_tags, s_questions)
        except Exception as e :
            print(e)
