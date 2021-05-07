#!/usr/bin/env python
# coding: utf-8

# In[1]:


#p(absent^friday)=0.03
probabilityAbsAndFri=0.03
#p(friday)=0.2
probabilityFri=0.2
#using Bayes Theorem
#p(a/f)=p(a^f)/p(f)
res=(probabilityAbsAndFri/probabilityFri)
print(res*100)


# In[ ]:




