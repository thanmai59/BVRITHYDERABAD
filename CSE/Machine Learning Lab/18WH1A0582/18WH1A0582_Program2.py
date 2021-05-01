#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
conn = sqlite3.connect('exp-2')
cur = conn.cursor
print("Opened database successfully")


# In[12]:


conn.execute('''CREATE TABLE COMPANY1
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");


# In[13]:


conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully");


# In[14]:


for row in conn.execute('select * from COMPANY1'):
     print(row)


# In[15]:


conn.commit()


# In[16]:


conn.close()


# In[ ]:




