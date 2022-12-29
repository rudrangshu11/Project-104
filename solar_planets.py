import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, 
            "Sun",
            (15,90),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (255,255,255))

cv2.putText(img, 
            "Mercury",
            (115,175),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img, 
            "Venus",
            (190,160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img, 
            "Earth",
            (285,160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img, 
            "Mars",
            (380,170),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img, 
            "Jupiter",
            (475,220),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (34, 32, 33))

cv2.putText(img, 
            "Saturn",
            (760,220),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (34, 32, 33))

cv2.putText(img, 
            "Uranus",
            (950,220),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (34, 32, 33))

cv2.putText(img, 
            "Neptune",
            (1100,220),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (217, 221, 220))

cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)