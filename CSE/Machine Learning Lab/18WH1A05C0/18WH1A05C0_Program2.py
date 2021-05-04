#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install db-sqlite3
import sqlite3


# In[3]:


conn=sqlite3.connect('exp2.db')
cur=conn.cursor
conn=sqlite3.connect('test.db')
print("Opened database successfully")


# In[17]:


conn.execute('''CREATE TABLE COMPANY2
            (ID INT PRIMARY KEY    NOT NULL,
             NAME           TEXT   NOT NULL,
             AGE            INT    NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);''')
print("Table created Successfully");


# In[24]:


conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)      VALUES(1,'Paul',  32, 'California', 20000.00)");

conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)      VALUES(2,'Allen', 25, 'Texas', 15000.00)");

conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)      VALUES(3,'Teddy', 23, 'Norway', 20000.00)");

conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)      VALUES(4,'Mark', 25, 'India', 18000.00)");
conn.commit()
print("Records created successfully");


# In[25]:


for row in conn.execute('select * from COMPANY2'):
        print(row)


# In[ ]:




