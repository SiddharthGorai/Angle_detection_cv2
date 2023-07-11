import cv2
import math

dots = []  # List containing coordinates of mouse clicks

def dist():
    a = ((dots[0][1] - dots[1][1])**2 + (dots[0][0] - dots[1][0])**2)**0.5    #dist b/w p1 and p2 
    b = ((dots[1][1] - dots[2][1])**2 + (dots[1][0] - dots[2][0])**2)**0.5    #dist b/w p2 and p3
    c = ((dots[0][1] - dots[2][1])**2 + (dots[0][0] - dots[2][0])**2)**0.5      #dist b/w p1 and p3

    return [a,b,c]
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:    
        cv2.circle(img,(x,y), 5,(0,0,255),-1)
        dot = (x,y)
        dots.append(dot)
        print(dots)

        if (len(dots) != 0):
            cv2.arrowedLine(img,dots[0],(x,y),(0,0,255),4)

        if (len(dots) == 3):
            a,b,c = dist()
            angle = math.acos((a**2 + c**2 - b**2)/(2*a*c))
            angle = int(math.degrees(angle))
            cv2.putText(img,str(angle),(dots[0][0]-30,dots[0][1]-30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
            print(angle)
            dots.clear()
    cv2.imshow('image',img)
        

img = cv2.imread("protractor.png")
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
cv2.imshow('image',img)
cv2.setMouseCallback('image', draw_circle)
cv2.waitKey(0)
cv2.destroyAllWindows()
