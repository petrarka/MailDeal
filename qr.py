import qrcode
import img2gif

def intToByteArray(integer):
    if isinstance(integer, int) :
        uint16_max = 65536
        if not integer <= uint16_max:
            integer = uint16_max
        return bytearray([(integer << 8) >> 8, integer >> 8])

a=[]
f=0
inp=input('vedi:')
while len(inp)>0:
    if len(inp)<=798:
        a.append(inp)
        inp=''
        print(len(inp))

    else:
        print('1')
        a.append(inp[:798])
        inp=inp[798:]
        len(inp)

z=0
while len(a)!=z:
    qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
    )
    a[z]= bytearray(a[z], encoding='UTF-8')+intToByteArray(z+1)
    print(a[z])
    a[z]=a[z].decode('UTF-8')
    print(a[z])
    qr.add_data(a[z])
    qr.make(fit=True)

    img = qr.make_image()
    img.save('qr'+str(z)+'.png')
    qr=''
    z=z+1


