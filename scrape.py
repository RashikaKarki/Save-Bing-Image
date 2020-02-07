from bs4 import BeautifulSoup
import requests 
from PIL import Image
import os
from io import BytesIO
import re

#Main function with all the functionality
def scrape_image():
    search=input("Search for:")
    params={"q":search}
    r=requests.get("https://www.bing.com/images/search",params=params)

    soup=BeautifulSoup(r.text,"html.parser")
    bimg = re.compile("mm.bing.net")
    links = soup.find_all("img", {"src": bimg})
    try:
        #creating folder to store images
        path = os.path.join("./",search) 
        os.mkdir(path)
        i=0
        for item in links:
            i+=1
            try:
                img_obj=requests.get(item.attrs["src"])
                img=Image.open(BytesIO(img_obj.content))
                #storing the images in the new folder
                img.save("./"+search+"/"+search+str(i)+"."+img.format)
            except:
                print("Could not download this image")
    except:
        print("Could not create folder check if folder already exists")




while True:
    answer=input("Do you want to scrape image? (Y/N)")
    if answer=="Y" or answer=="y" :
        scrape_image()
    elif answer=="N" or answer=="n" :
        print("Come Back Soon")
        break
    else: 
        print("Invalid Answer")
