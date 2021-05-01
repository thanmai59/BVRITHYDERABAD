#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3


# In[3]:


con=sqlite3.connect('exp2.db')
cur=con.cursor()
con=sqlite3.connect('test.db')
print("opened database successfully")


# In[7]:


con.execute('''CREATE TABLE COMPANY3
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE  INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);''')
print("Table created successfully!")


# In[8]:


con.execute("INSERT INTO COMPANY3 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

con.execute("INSERT INTO COMPANY3 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

con.execute("INSERT INTO COMPANY3 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

con.execute("INSERT INTO COMPANY3 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

con.commit()
print ("Records created successfully");


# In[10]:


for row in con.execute('select * from COMPANY3'):
        print(row)


# In[11]:


con.commit()


# In[13]:


con.close()


# In[ ]:




