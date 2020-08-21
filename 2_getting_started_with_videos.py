import cv2

# Read existing video file ---> 'name.avi'
# cap is an instance (object) of class VideoCapture
# For Capturing video -------------------------------------
cap = cv2.VideoCapture(0) # Our Device is at  0 by default, for other video camera change to 1,2,3 etc
# using cap, we can read few properties of video captured !
# 1st Prop. --> If video is opened or not?
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# For saving video----------------------------------------
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# (name of output file, four cc code -->used to specify video codec, FPS, size of capturing)
# out is instance of class VideoWriter
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

print(cap.isOpened())
while(cap.isOpened()): # False,if filepath or index (VideoCapture(0)) is wrong!
    # # Capture frame-by-frame
    ret, frame = cap.read() #returns true if frame is available
    # ret --> if frame is saved, True else False
    # frame --> it saves/captures the frame

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if ret == True:  # If frame is available

        # Our operations on the frame come here--------------------
        # 2nd Prop. --> Using 'PROP ID'
        # Frame height and width
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #PROP_NO. 3
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #PROP_NO. 4

        out.write(frame)  #write a frame into a file

         # convert frame to GrayScale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame', frame)  # shows frame in a window

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()


# For reading frame by frame/creating Capture Video  --> VideoCapture Class
# For saving video --> VideoWriter class