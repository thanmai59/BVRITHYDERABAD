#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install db-sqlite3')


# In[2]:


import sqlite3


# In[3]:


conn = sqlite3.connect("test.db")
cur=conn.cursor()
print("Database opened successfully")


# In[4]:


conn.execute('''CREATE TABLE COMPANY
(ID  INT  PRIMARY KEY   NOT NULL,
NAME            TEXT  NOT NULL,
AGE             INT   NOT NULL,
ADDRESS        CHAR(50),
SALARY         REAL);''')
print("Table created successfully");


# In[16]:


conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)      VALUES (1, 'Paul', 32, 'California', 200000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)      VALUES (2, 'Allen', 22, 'Texas', 150000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)      VALUES (3, 'Teddy', 23, 'Norway', 200000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)      VALUES (4, 'Mark', 25, 'Rich-Mond', 650000.00 )");

conn.commit()
print ("Records created successfully");


# In[18]:


for row in conn.execute('select * from COMPANY'):
    print(row)


# In[ ]:




