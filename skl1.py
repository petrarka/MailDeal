from PIL import Image
import os

p = 0

pol = []
while os.path.exists('qr' + str(p) + '.png'):
    pol.append(Image.open('qr' + str(p) + '.png'))
    p += 1
print(len(pol))
s = 0
p = 0
while len(pol) - 1 >= p:
    print('1232322')
    img = Image.new('RGB', (1050, 1050), )
    img.paste(pol[p], (0, 0))
    if len(pol) - 1 >= p + 1:
        print('445')
        img.paste(pol[p + 1], (525, 0))
        print('84')
    if len(pol) - 1 >= p + 2:
        print('48')
        img.paste(pol[p + 2], (0, 525))
    if len(pol) - 1 >= p + 3:
        print('44')
        img.paste(pol[p + 3], (525, 525))
    img.save('sk' + str(s) + '.jpeg', 'JPEG')
    img=0
    p += 4
    s += 1
    print('1')
