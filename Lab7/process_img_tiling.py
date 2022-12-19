import numpy as np
from PIL import Image
# import image
from numpy import asarray
import matplotlib.pyplot as plt
from keras.models import Model, load_model

print("start")
normal_generator = load_model(
    '/Users/aslikocak/Desktop/comp-graphs/Lab7/my_best_model.epoch89-loss0.02.hdf5')
print("stop")
webimg = Image.open('/Users/aslikocak/Desktop/comp-graphs/Lab7/texture.jpeg')
image = asarray(webimg)
plt.imshow(image)

img_size = 512
print("network input size", img_size)
width = image.shape[0]
height = image.shape[1]
print("width, height", width, height)
width_repeat = np.ceil(width / img_size)
height_repeat = np.ceil(height / img_size)
w_pad = img_size - (width % img_size)
h_pad = img_size - (height % img_size)
if (w_pad == img_size):
  w_pad = 0
if (h_pad == img_size):
  h_pad = 0
print("w_pad, h_pad", w_pad, h_pad)
print("width_repeat, height_repeat", width_repeat, height_repeat)
image = np.pad(image, [(0, w_pad), (0, h_pad), (0, 0)], mode='constant', constant_values=0)
normal = np.zeros(image.shape)
for i in range(int(width_repeat)):
  for j in range(int(height_repeat)):
    img = np.zeros((img_size, img_size, 3))
    img = image[i*512:(i+1)*512, j*512:(j+1)*512, :]
    img = img.astype(float)
    img = img.astype(float) / 255.0
    gen_img = normal_generator.predict(img.reshape(1, img_size, img_size, 3))
    normal[i*512:(i+1)*512, j*512:(j+1)*512, :] = gen_img.reshape(img_size,img_size,3)
normal_final = normal[0:width, 0:height, :]

# plt.imshow(normal_final.reshape(width, height, 3))
normal_final = normal_final.reshape(width, height, 3)
# normal_final *= (255.0/normal_final.max())
# print(normal_final.max(), normal_final.min())
normal_final = normal_final * 255
normal_final = normal_final.astype(np.uint8)
# print(normal_final.max(), normal_final.min())
img_out = Image.fromarray(normal_final)
img_out.save("/Users/aslikocak/Desktop/comp-graphs/Lab7/final.ppm")
