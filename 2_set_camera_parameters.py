# SET WIDTH & HEIGHT
# DATE TIME ON LIVE VIDEO
import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #PROP_NO. 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #PROP_NO. 4

# cap.set(cv2.CAP_PROP_FRAME_WIDTH,1208)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
#cap.set(3,1208)
#cap.set(4,720)

#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()
