import cv2

cap = cv2.VideoCapture(0) # need a webcam for this to work.  #replace filename

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Your VideoWriter Codec may vary
writer=cv2.VideoWriter('this_video.avi',cv2.VideoWriter_fourcc(*'XVID'),20,(width,height))

while True:
    ret,frame = cap.read()
    writer.write(frame)

    cv2.imshow('frame',frame)

    # hit the q key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
