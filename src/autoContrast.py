# import cv2
# import numpy as np

# # Open a typical 24 bit color image. For this kind of image there are
# # 8 bits (0 to 255) per color channel
# img = cv2.imread('C:\\Users\\invnarla\\Desktop\\devdevelop\\CaseImages\\Capturestart.jpg')  # mandrill reference image from USC SIPI
# #img = cv2.resize(img, (1000,600), 0, 0, cv2.INTER_AREA)

# def apply_contrast(input_img, contrast = 0):
#     buf = input_img.copy()
#     if( contrast < 2):
#         contrast = 2
#     elif( contrast > 98):
#         contrast = 98

#     f = 255 * (contrast / 100)
#     alpha_c = 255/f

#     print("\n ".join(['contrast:',str(contrast),'alpha_c:',str(alpha_c)]))
#     adjusted = input_img.copy()
#     cv2.convertScaleAbs(buf, adjusted, alpha=alpha_c, beta = 1)
#     print('out')
#     return adjusted

# clist = [100, 80, 60, 40, 20, 0] # list of brightness values

# for i, c in enumerate(clist):
#     b = 100 - c
#     outimage = apply_contrast(img, c)
#     var1 ='C:\\Users\\invnarla\\Desktop\\devdevelop\\CaseImages\\new\\Capture-'
#     var2 = '.png'
#     varnew = " ".join([var1,str(c), var2])
#     cv2.imwrite(varnew, outimage)
import sys
import cv2
import numpy as np
import urllib.request

# Download the image and store as a numpy array.
# Apply contrast to numpy array


def url_to_image(url):
    print("url_to_image")
    resp = urllib.request.urlopen(url)
    nparrayimage = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(nparrayimage, cv2.IMREAD_COLOR)
    return image


# def buffer_to_image(buffer):
#     jpg_as_np = np.frombuffer(buffer, dtype=np.uint8)
#     img = cv2.imdecode(jpg_as_np, flags=1)
#     return img


def apply_contrast(input_img, brightness):
    print("apply_contrast")
    contrast = 100 - brightness
    buf = input_img.copy()
    if(contrast < 2):
        contrast = 2.8
    elif(contrast > 98):
        contrast = 98
    f = 255 * (contrast / 100)
    alpha_c = 255/f
    adjusted = input_img.copy()
    cv2.convertScaleAbs(buf, adjusted, alpha=alpha_c)
    print("buf")
    print(adjusted)
    return adjusted


# def apply_contrast_to_bufferData(input_img, brightness):
#     contrast = 100 - brightness
#     buf = input_img.copy()
#     if(contrast < 2):
#         contrast = 2.8
#     elif(contrast > 98):
#         contrast = 98
#     f = 255 * (contrast / 100)
#     alpha_c = 255/f
#     adjusted = input_img.copy()
#     cv2.convertScaleAbs(buf, adjusted, alpha=alpha_c)
#     return adjusted


# clist = [100, 80, 60, 40, 20, 0]  # list of brightness values
# for i, c in enumerate(clist):
#     imgurl = sys.argv[1]
#     brightness = sys.argv[2]
#     print(brightness)
#     img = url_to_image(imgurl)
#     # img = cv2.imread('C:\\Users\\invnarla\\Desktop\\devdevelop\\CaseImages\\Capturestart.jpg')
#     outimage = apply_contrast(img, int(brightness))
#     var1 = 'C:\\Users\\invnarla\\Desktop\\devdevelop\\CaseImages\\new\\Capture-'
#     var2 = '.png'
#     varnew = "".join([var1, str(c), var2])
#     cv2.imwrite(varnew, outimage)

print("applycontrast process started")
imgurl = sys.argv[1]
print(imgurl)
brightness = sys.argv[2]
print(brightness)
img = url_to_image(imgurl)
print(img)
outimage = apply_contrast(img, int(brightness))
print(outimage)
