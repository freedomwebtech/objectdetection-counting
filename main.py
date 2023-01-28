import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear    
stream = CamGear(source='https://www.youtube.com/watch?v=En_3pkxIJRM', stream_mode = True, logging=True).start() # YouTube Video URL as input
count=0
while True:
    frame = stream.read()
    count += 1
    if count % 6 != 0:
        continue
 
    frame=cv2.resize(frame,(1020,600))
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
stream.release()
cv2.destroyAllWindows()

