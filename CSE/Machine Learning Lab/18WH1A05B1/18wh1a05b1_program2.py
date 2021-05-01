#!/usr/bin/env python
# coding: utf-8

# In[23]:


#!pip install db-sqlite3
import sqlite3


# In[24]:


conn=sqlite3.connect('18wh1a05b1_program2.db')
cur=conn.cursor()
#conn = sqlite3.connect('test.db')
print ("Opened database successfully");


# In[28]:


conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY   NOT NULL,
         NAME           TEXT   NOT NULL, 
         AGE            INT    NOT NULL ,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully");


# In[29]:


conn.execute("INSERT INTO  COMPANY (ID,NAME,AGE,ADDRESS,SALARY)        VALUES (1, 'Paul', 32, 'California', 20000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)        VALUES (2, 'Allen', 25, 'Texas', 15000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)        VALUES (3, 'Teddy', 23, 'Norway', 20000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)        VALUES (4, 'Mark', 25, 'Rich-mond', 65000.00)");
conn.commit()
print ("Records created successfully");


# In[31]:


for row in conn.execute('select * from COMPANY'):
    print(row)


# In[32]:


conn.commit()


# In[33]:


conn.close()


# In[ ]:




