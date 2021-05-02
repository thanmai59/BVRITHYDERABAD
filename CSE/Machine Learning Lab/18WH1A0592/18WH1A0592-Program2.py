#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install db-sqlite3')
import sqlite3


# In[2]:



conn=sqlite3.connect('exp2.db')
cur=conn.cursor()
conn=sqlite3.connect('test.db')
print('opened database successfully');


# In[3]:



conn.execute('''CREATE TABLE COMPANY2
            (ID INT PRIMARY KEY  NOT NULL,
            NAME            TEXT NOT NULL,
            AGE             INT  NOT NULL,
            ADDRESS         CHAR(50),
            SALARY          REAL);''')
print("Table created successfully");


# In[4]:



conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)            VALUES (1, 'paul',32,'california',20000.00)");
conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)            VALUES (2, 'Alien',25,'Texas',30000.00 )");
conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)            VALUES (3, 'Teddy',23,'Norway',30000.00 )");
conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)            VALUES (4, 'Mark',25,'Rich-Mond',15000.00 )");
conn.commit()
print('Records created successfully');


# In[5]:



for row in conn.execute('select * from COMPANY2'):
    print(row)


# In[6]:



conn.commit()


# In[7]:



conn.close()


# In[ ]:




