#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install db-sqlite3
import sqlite3


# In[2]:


conn = sqlite3.connect('exp2.db')
cur = conn.cursor()
conn = sqlite3.connect('test.db')
print("Opened database successfully");
                       


# In[4]:


conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY NOT NULL,
            NAME    TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS   CHAR(50),
            SALARY  REAL);''')
print("Table created successfully");             


# In[5]:


conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)      VALUES(1,'Paul' , 32, 'California',20000.00) ");
conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)      VALUES(2,'Alien' ,25, 'Texas',15000.00) ");
conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)      VALUES(3,'Teddy' , 23, 'Norway',20000.00) ");
conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)      VALUES(4,'Mark' , 25, 'Rich-Mond',65000.00) ");
conn.commit()
print("Records created successfully");


# In[9]:


for row in conn.execute('select * from COMPANY'):
        print(row)


# In[10]:


conn.commit()


# In[11]:


conn.close()


# In[ ]:




