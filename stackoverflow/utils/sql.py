#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="0303",
    db="chenx",
    charset="utf8")

cur = conn.cursor()


PATH = os.path.join("..", "..", "result.json")
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

    def create_table():
        sql = """
            create table stackoverflow_info(
                s_links int(11) not null primary key,
                s_views int(11),
                s_votes int(11),
                s_answers int(11),
                s_tags text,
                s_questions text
            );
            
            """
        cur.execute(sql)

    def insert_db(*args):
        sql = "insert into stackoverflow_info(" \
              "s_links, s_views, s_votes, s_answers, s_tags, s_questions) " \
              "values(%s, %s, %s, %s, %s, %s)"
        cur.execute(sql, args)

    # create_table()
    for index, item in enumerate(data):
        try:
            insert_db(
                item['links'],
                item['views'],
                item['votes'][0],
                item['answers'][0],
                " ".join(item['tags']),
                " ".join(item['questions']))
            index += 1
            if index % 1000 == 0:
                conn.commit()
        except Exception as e:
            print(e)
    conn.close()
