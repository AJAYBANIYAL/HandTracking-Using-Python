import cv2
import mediapipe as mp
import time

#1 this code opens the VideoCapture
#cap =cv2.VideoCapture(1)

#while True:
    #success, img = cap.read()


    #cv2.imshow("image", img)
    #cv2.waitKey(1)


cap =cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
#line draw function by google to much maths involved
mpDraw =mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(imageRGB)
    #print(results.multi_hand_landmarks)
#code for two hand detection handLms is one hand here
    if results.multi_hand_landmarks:
      for handLms in results.multi_hand_landmarks:
          #index no
          for id,lm in enumerate(handLms.landmark):
            #print(id,lm)
            h,w,c=img.shape
            cx , cy = int(lm.x*w),int(lm.y*h)
            print(id,cx,cy)
            if id ==0:
                cv2.circle(img , (cx , cy) , 25 , (255,8,255), cv2.FILLED)

          mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)




    cTime= time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(18,70),cv2.FONT_HERSHEY_PLAIN ,3 ,(255,8,255),3)


    cv2.imshow("image", img)
    cv2.waitKey(1)
