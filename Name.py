from email.mime import Image
import cv2

img = Image.open('solar-system.jpg')
img.show()
print()

cv2.putText(img,

         "Sun"
         (20,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()

cv2.putText(img,

         "Mercury"
         (60,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()

cv2.putText(img,

         "Venus"
         (100,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()

cv2.putText(img,

         "Earth"
         (140,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()

cv2.putText(img,

         "Mars"
         (180,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()

cv2.putText(img,

         "Jupiter"
         (220,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()

cv2.putText(img,

         "Saturn"
         (260,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()

cv2.putText(img,

         "Uranus"
         (300,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()

cv2.putText(img,

         "Neptune"
         (340,300),
         cv2.FONT_HERSHEY_COMPLEX,
         0.5,
         (255,255,255)
         )
print()





  

cv2.destroyAllWindows()