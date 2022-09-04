import cv2

img = cv2.imread('./planets.jpg')

#Adding text for celestial bodies
cv2.putText(img,
'Sun',
(20, 300),
cv2.FONT_HERSHEY_COMPLEX,
1,
(300, 300, 300)
)

cv2.putText(img,
'Mercury',
(120, 200),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(300, 300, 300)
)

cv2.putText(img,
'Venus',
(190, 260),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(300, 300, 300)
)

cv2.putText(img,
'Earth',
(280, 270),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(300, 300, 300)
)

cv2.putText(img,
'Mars',
(390, 255),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(300, 300, 300)
)

cv2.putText(img,
'Jupiter',
(530, 350),
cv2.FONT_HERSHEY_COMPLEX,
0.8,
(300, 300, 300)
)

cv2.putText(img,
'Saturn',
(780, 320),
cv2.FONT_HERSHEY_COMPLEX,
0.72,
(300, 300, 300)
)

cv2.putText(img,
'Uranus',
(960, 290),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(300, 300, 300)
)

cv2.putText(img,
'Neptune',
(1100, 290),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(300, 300, 300)
)

cv2.imshow('Solar system', img)
cv2.waitKey(0)