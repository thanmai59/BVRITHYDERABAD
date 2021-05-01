#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install db-sqlite3')
import sqlite3


# In[2]:


conn=sqlite3.connect('exp2.db')
cur=conn.cursor()
conn = sqlite3.connect('test.db')
print ("Opened database successfully");


# In[3]:


conn.execute('''CREATE TABLE COMPANY1
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");


# In[4]:


conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Deepthi', 20, 'Seoul', 60000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Sindhu', 23, 'Hyderabad', 45000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'John', 23, 'Busan', 25000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Suma', 35, 'New York ', 65000.00 )");

conn.commit()
print ("Records created successfully");


# In[5]:


for row in conn.execute('select * from COMPANY1'):
        print(row)
        


# In[6]:


conn.commit()


# In[7]:


conn.close()


# In[ ]:




