from pdf2image import convert_from_path
from PIL import Image 
import numpy as np
import sys

if len(sys.argv) < 2:
    sys.exit('No argument specified.')

pages = convert_from_path(sys.argv[1])

if pages is None:
    sys.exit('Could not read file.')
    
new_pages = []
for page in pages:
    data = np.array(page)
    cond = (np.logical_and(data < (235,235,235), data > (229,229,229)))
    data[(cond).all(axis = -1)] = (255,0,255)
    img2 = Image.fromarray(data, mode='RGB')
    new_pages.append(img2)
    #img2.show()

img2.save("out.pdf", "PDF", resolution=100.0, save_all=True, append_images=new_pages)
