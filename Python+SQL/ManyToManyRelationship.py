
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

# creating the tables
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

# inserting records in above tables
cur.executescript("""
                    insert into User (name, email)
                    values ('Jane', 'jane@tsugi.org');

                    insert into User (name, email)
                    values ('Ed', 'ed@tsugi.org');

                    insert into User (name, email)
                    values ('Sue', 'sue@tsugi.org');

                    insert into Course (title)
                    values ("Python");

                    insert into Course (title)
                    values ("SQL");

                    insert into Course (title)
                    values ("Julia");
                    """
                    )

cur.executescript("""
                    INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
                    INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
                    INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

                    INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
                    INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

                    INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
                    INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);
                    """)

fetch_records = """
                SELECT User.name, Member.role, Course.title
                FROM User JOIN Member JOIN Course
                ON User.id = Member.user_id and Member.course_id = Course.id
                """

for record in cur.execute(fetch_records):
    print(record)    # tuple containing the records !


cur.close()
conn.close()
