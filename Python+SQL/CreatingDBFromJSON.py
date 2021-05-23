
import json
import sqlite3


conn = sqlite3.connect(r"D:\Applied AI\Datasets and DB\py4eDB-M2M_Relationship.db")
cur = conn.cursor()

print("Many-To-Many Relationship!\n")
# first lets drop all the tables that we want to create, if they exists already!
cur.executescript("""
                    DROP table if exists User;
                    DROP table if exists member;
                    DROP table if exists course;

                    """
                    )

cur.executescript("""
                    Create table User(
                    "id" integer primary key AUTOINCREMENT not null unique,
                    "name" TEXT,
                    "email" text
                    );

                    Create table Course(
                    "id" integer primary key AUTOINCREMENT not null unique,
                    "title" text
                    );

                    CREATE TABLE Member (
                    "user_id" INTEGER,
                    "course_id" INTEGER,
	                "role" INTEGER,
                    PRIMARY KEY ("user_id", "course_id")
                    )
                    """
                    )

with open(r"D:\PythonProgram\FileHandling\roster_data.json", 'r') as fh:
    filecontent = fh.read()
    json = json.loads(filecontent)

    for record in json:
        name, title, role = record
        cur.execute("""
                    INSERT OR IGNORE INTO User (name)
                    values(?)
                    """,(name,)
                    )

        cur.execute("""
                    INSERT OR IGNORE INTO Course (title)
                    values(?)
                    """,(title,)
                    )

        cur.execute("select id from User where name = ?", (name,))
        user_id = cur.fetchone()[0]
        cur.execute("select id from Course where title = ?", (title,))
        course_id = cur.fetchone()[0]


        cur.execute("""
                    INSERT OR REPLACE INTO Member (user_id, course_id, role)
                    values(?, ?, ?)
                    """,(user_id, course_id, role)
                    )

conn.commit()

testing = cur.execute("""
                           SELECT User.name,Course.title, Member.role FROM
                           User JOIN Member JOIN Course

                           ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

                           """)

for row in testing:
    print("{} | {} | {}".format(row[0], row[1], row[2]))

# cur.execute("""
#                     SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM User JOIN Member JOIN Course
#                     ON User.id = Member.user_id AND Member.course_id = Course.id
#                     ORDER BY X LIMIT 1;
#
#                     """  )
#
# print(cur.fetchone()[0])

cur.close()
conn.close()
#print("DB Disconnected!")
