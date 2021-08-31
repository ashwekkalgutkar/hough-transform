#!/usr/bin/env python
# coding: utf-8

# <h>HOUGH TRANSFORM</h>

# In[17]:


import cv2
from matplotlib import pyplot as plt
import numpy as np


# In[18]:


img=cv2.imread("sudoku1.png")
#gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gussian
gaussian_img=cv2.GaussianBlur(gray,(3,3),0)


# In[19]:


#plt.imshow(img)
#plt.show()


# In[36]:


edges=cv2.Canny(gaussian_img,10,40)
plt.figure(figsize=(10,5))
plt.subplot(2,2,1)
plt.imshow(edges)


# In[37]:


lines=cv2.HoughLinesP(edges,1,np.pi/100,50)
#print(lines)


# In[38]:


for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("hough transform",img)
cv2.imshow("canny",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




