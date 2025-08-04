import imageio.v3 as iio

filenames = ['gifpic_1.png', 'gifpic_2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('monke.gif', images, duration = 500, loop = 0)