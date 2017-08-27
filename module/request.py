import requests
import json
import os
import sys

print('Enter Instagram account:')
account=input()
url='https://www.instagram.com/'+account+'/media/'

r=requests.get(url)
text=r.json()
print(text)
form=json.dumps(text, indent=4, sort_keys=4)

pars=text['items']

if text['more_available']!=True:
    print('Access denied')
    sys.exit()
else:
    print('Waiting for loading...')

img_path ='..\\'+account+'\\img\\'
path='..\\newdir1'
video_path ='..\\'+account+'\\video\\'
os.makedirs(img_path, exist_ok=True)
os.makedirs(video_path, exist_ok=True)

for i in pars:
    img_link=i['images']['standard_resolution']['url']
    if img_link!=None:
        get_img=requests.get(img_link)
        fname='..\\'+account+'\\img\\'+i['code']+'.png'
        file=open(fname,"wb+")
        file.write(get_img.content)
        file.close()
    video_link=(i['alt_media_url'])
    if video_link!=None:
        get_video=requests.get(video_link, stream=True)
        fname='..\\'+account+'\\video\\'+i['code']+'.mp4'
        file1=open(fname, "wb")
        for chunk in get_video.iter_content(chunk_size=512):
            if chunk:
                file1.write(chunk)

print('Loading is completed!')
