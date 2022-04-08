#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PyPDF2 import PdfFileReader
from PIL import Image

image_1 = Image.open(
    r'C:\Users\harsh\Documents\My DOCS\proof\2nd sem Marksheet.jpeg')

img_1 = image_1.convert('RGB')

img_1.save(r'C:\Users\harsh\Documents\My DOCS\proof\2nd sem Marksheet.pdf')


# In[ ]:





# In[ ]:




