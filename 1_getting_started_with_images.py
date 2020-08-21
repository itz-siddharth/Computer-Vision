import cv2

img = cv2.imread('lena.jpg', -1)

print(img)  # prints Matrix

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF    # returns the code of the pressed key
# (measured in milliseconds)
# 0 is the special value that means “forever”
# It returns the code of the pressed key or -1 if no key was pressed before the specified time had elapsed.

if k == 27: # ESC Key ASCII value = 27
    cv2.destroyAllWindows()
elif k == ord('s'): # if key 's' is pressed
    cv2.imwrite('lena_copy.png',img)  # save a copy of img
    cv2.destroyAllWindows()  # destroy all windows
