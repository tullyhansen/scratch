from StringIO import StringIO
from PIL import Image
import requests

# original code by foozmeat

response = requests.get("http://pbs.twimg.com/profile_images/460740982498013184/wIPwMwru_normal.png")
im1 = Image.open(StringIO(response.content)).convert('RGB')
im1 = im1.convert('P', palette=Image.ADAPTIVE, colors=255)
colors = im1.getcolors()
sorted_colors = sorted(colors, key=lambda tup: tup[0], reverse=True)

print sorted_colors[0][1]