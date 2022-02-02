#!/usr/bin/env python3

import psycopg2
import datetime

import zoneinfo

posted = datetime.datetime(2022, 2, 2, 18, 30, tzinfo=zoneinfo.ZoneInfo("Europe/Berlin"))

conn = psycopg2.connect(
    host="127.0.0.1",
    port=65431,
    dbname="marvin",
    user="marvin",
    password="store-a-list-of-domains",
)

with conn.cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS psycopg2_post (posted timestamp with time zone)")
    cursor.execute("TRUNCATE TABLE psycopg2_post;")
    cursor.execute("INSERT INTO psycopg2_post (posted) VALUES(%s::timestamptz)", (posted,))
    cursor.execute("SELECT posted::timestamptz FROM psycopg2_post")
    posted_db = cursor.fetchone()[0]

print(posted)
print(posted_db)
