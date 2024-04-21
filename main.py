import re
import os
import uuid
import shutil
import urllib.request
from openai import OpenAI

css_file = '/home/mat/Obsidian/.obsidian/snippets/nice_bg_translucency.css'
pic_dump = '/home/mat/Pictures/obs_bg_pics/'
client = OpenAI()

def update_css(image_path, css_file=css_file):
    # Pattern to find the existing image URL
    pattern = re.compile(r'url\((.*?)\)')
    print("updating css")

    with open(css_file, 'r+') as file:
        content = file.read()
        # Replace the old URL with the new one
        new_content = pattern.sub(f"url('{image_path}')", content)
        file.seek(0)
        file.write(new_content)
        file.truncate()

def make_img():
    print("making image")
    style_prompt = "Can you generate a picture that would look good with white text on the front of that would be used as the background of a text editor? Something interesting and pleasing to look at but not too catchy to always grab your attention? Just background passive beauty with the following ideas or attributes: "
    res = client.images.generate(
        model = "dall-e-3",
        prompt = style_prompt + "magificent street creatures",
        size = "1792x1024",
        quality = "standard",
        n = 1
    )
    
    url = res.data[0].url
    name = pic_dump + str(uuid.uuid4().hex) + ".jpg"
    urllib.request.urlretrieve(url, name)
    return name


img = make_img()
update_css(img)


## gen image
    ## store it // ~/Pictures/obs_bg_pics
    ## check if repo exists, if not create it 
## update css file
## (13:41:26) -- 

## alright, `python3 -m http.server` gives us the bg pic in obs. 
## Next I need to figure out how to manage the server. 
