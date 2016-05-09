import sqlite3
conn = sqlite3.connect('so-dump.db')
c = conn.cursor()
d_h = ('DROP TABLE IF EXISTS high')
c.execute(d_h)


l_h = ('DROP TABLE IF EXISTS low')
c.execute(l_h)

# create a table with high quality questions
con = ('0', '1', '0','0')
c.execute('CREATE TABLE high AS\
          SELECT * FROM posts WHERE Score > ? AND\
          PostTypeID = ? AND\
          OwnerUserId > ? AND\
          AcceptedAnswerId > ? AND\
          ClosedDate IS NULL', con)


# create a table with low quality quesitons
con1 = ('0', '1', '', '0')
c.execute('CREATE TABLE low AS SELECT * FROM posts WHERE Score < ? AND\
          PostTypeID = ? AND\
          (OwnerUserId = ? OR\
          ClosedDate > ?)', con1)


conn.close()
