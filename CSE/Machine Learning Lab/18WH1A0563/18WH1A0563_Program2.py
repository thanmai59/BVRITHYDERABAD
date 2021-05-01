#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install db.sqlite3
import sqlite3


# In[4]:


conn=sqlite3.connect('prg2.db')
cur=conn.cursor()
conn = sqlite3.connect('test.db')
print("Opened database successfully");


# In[5]:


conn.execute('''CREATE TABLE COMPANY1
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");


# In[6]:


conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Jai', 21, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Nani', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'vish', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Prnvi', 24, 'Sweden ', 65000.00 )");

conn.commit()
print ("Records created successfully");


# In[7]:


for row in conn.execute('select * from COMPANY1'):
        print(row)


# In[8]:


conn.commit()


# In[9]:


conn.close()

