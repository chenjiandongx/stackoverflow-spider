import json
import pymysql

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="0303", db="chenx", charset="utf8")
cur = conn.cursor()

with open(r"e:\python\stackoverflow\data\data2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    def insert_db(s_links, s_views, s_votes, s_answers, s_tags, s_questions):
        """" Insert data to database """

        sql = "insert into stackoverflow(s_links, s_views, s_votes, s_answers, s_tags, s_questions) " \
              "values(%s, %s, %s, %s, %s, %s)"
        value = (s_links, s_views, s_votes, s_answers, s_tags, s_questions)
        cur.execute(sql, value)
        conn.commit()
        print("Insert s_links: " + s_links)

    for _, value in enumerate(data):
        s_links = value['links']
        s_views = value['views']
        s_votes = value['votes']
        s_answers = value['answers']
        s_tags = " ".join(value['tags'])
        s_questions = value['questions']
        try:
            insert_db(s_links, s_views, s_votes, s_answers, s_tags, s_questions)
        except Exception as e:
            print(e)
