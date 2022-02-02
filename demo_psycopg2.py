#!/usr/bin/env python3

import psycopg2
import datetime

posted = datetime.datetime(2022, 2, 2, 0, 25, 59, 256973, tzinfo=datetime.timezone.utc)

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
    # django does:
    #   INSERT INTO "tztestapp_post" ("posted")
    #   VALUES ('2022-02-02T00:25:59.256973+00:00'::timestamptz)
    #   RETURNING "tztestapp_post"."id";
    #   args=(datetime.datetime(2022, 2, 2, 0, 25, 59, 256973, tzinfo=datetime.timezone.utc),)
    cursor.execute("INSERT INTO psycopg2_post (posted) VALUES(%s::timestamptz);", (posted,))
    # django does:
    #   SELECT "tztestapp_post"."id", "tztestapp_post"."posted"
    #   FROM "tztestapp_post"
    #   WHERE "tztestapp_post"."id" = 3 LIMIT 21;
    #   args=(3,);
    cursor.execute("SELECT posted FROM psycopg2_post;")
    posted_db = cursor.fetchone()[0]

print(posted)
print(posted_db)
