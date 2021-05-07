#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install db-sqlite3


# In[2]:


import sqlite3


# In[5]:


con=sqlite3.connect('exp2.db')
cur=con.cursor()
con=sqlite3.connect('test.db')
print("opened database successfully")


# In[6]:


con.execute('''CREATE TABLE STUDENT(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50))''')
print("Table created successfully")


# In[9]:


con.execute("INSERT INTO STUDENT (ID,NAME,AGE,ADDRESS)VALUES(1,'SARASWATHI',21,'KOLLAPUR')");
con.execute("INSERT INTO STUDENT (ID,NAME,AGE,ADDRESS)VALUES(2,'SHAILAJA',22,'HYDERABAD')");
con.execute("INSERT INTO STUDENT (ID,NAME,AGE,ADDRESS)VALUES(3,'BHAGYA',23,'NAGARKURNOOL')");
con.commit()
print("Records inserted succesfully")


# In[11]:


for row in con.execute('select * from STUDENT'):
    print(row)


# In[12]:


con.commit()


# In[13]:


con.close()


# In[ ]:




