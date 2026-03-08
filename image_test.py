from PIL import Image
import time
img = Image.open("./images/hydra.jpg", mode = 'r')
img.show()
time.sleep(5)