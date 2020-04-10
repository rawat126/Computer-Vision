# Installing necessary Libraries
# pip install python-opencv
# import Libraries
import cv2
import os
from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog
import time

# Blur/Anonyomize effect function.....
# arguments
# img : the input image cropped face array
# blur_pixel_size : the size according to blur pixel
def convert_face_blur(img,blur_pixel_size=17):

    rows,columns = img.shape[0],img.shape[1]

    # BGR Plane extraction from face-cropped image 
    blue_plane = img[:,:,0]
    green_plane = img[:,:,1]
    red_plane = img[:,:,2]

    # Anonyomize effect algorithum
    # appilied plane-by-plane
    for i in range(0,rows,blur_pixel_size):
        for j in range(0,columns,blur_pixel_size):
            blue_plane[i:i+blur_pixel_size,j:j+blur_pixel_size] = cv2.blur(blue_plane[i:i+blur_pixel_size,j:j+blur_pixel_size],(blur_pixel_size,blur_pixel_size))
            green_plane[i:i+blur_pixel_size,j:j+blur_pixel_size] = cv2.blur(green_plane[i:i+blur_pixel_size,j:j+blur_pixel_size],(blur_pixel_size,blur_pixel_size))
            red_plane[i:i+blur_pixel_size,j:j+blur_pixel_size] = cv2.blur(red_plane[i:i+blur_pixel_size,j:j+blur_pixel_size],(blur_pixel_size,blur_pixel_size))

    # Merging BGR planes after anonyomization
    img = cv2.merge([blue_plane,green_plane,red_plane])
    return(img)


# For selection of Face coordinates in an image
# arguments
# root : root window of GUI Panel
# classifier : Haarcascade Classifier for face coordinates
def for_image(root,classifier):

    img_name = filedialog.askopenfilename(title='Select image file',)
    img = cv2.imread(img_name)
    #print(img)
    coordinates = classifier.detectMultiScale(img)
    print(coordinates)
    x1,y1,x2,y2 = coordinates[0]
    x2 = x1+x2
    y2 = y1+y2

    img1 = img

    blur_image = convert_face_blur(img[y1:y2,x1:x2])
    img1[y1:y2,x1:x2] = 255
    img1[y1:y2,x1:x2]=blur_image
    #print(img1[y1:y2,x1:x2].shape)
    #print(blur_image.shape)
    cv2.imshow('Output Image',img1)

    time.sleep(0.53)
    d = msg.askquestion('Save image','Do You want to save the image')
    
    # saving image inside Directory
    if(d.lower()=='yes'):
        op = filedialog.asksaveasfilename(title='Select Directory')
        cv2.imwrite(op,img1)
        msg.showinfo('saved','File saved sucessfully')
    else:
        pass


# For selection of Face coordinates in Live Video Frame
# arguments
# classifier : Haarcascade Classifier for face coordinates
def for_video(classifier):
    # reading VideoCamera by web-cam
    global cam
    cam = cv2.VideoCapture(0)

    while(True):
        
        _,image = cam.read()  
        faces = classifier.detectMultiScale(image)
        print(image)
        for coordinates in faces:
            print(coordinates)
            x1,y1,x2,y2 = coordinates
            x2 = x1+x2
            y2 = y1+y2

            #cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)
            blur_image = convert_face_blur(image[y1:y2,x1:x2],22)
            image[y1:y2,x1:x2] = 255
            image[y1:y2,x1:x2]=blur_image
        
        cv2.imshow('Output Frame',image)
        if cv2.waitKey(1)==27:
            break
        
    # Destroy all frames after execution...
    cam.release()
    cv2.destroyAllWindows()

#Using HaarCascade xml file for face location coordinates....
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Initialize default cam variable.....
cam = None

# Creating Basic GUI for General Input/Output... 
root = Tk()
root.title('Face Blur')
root.geometry('700x400')

l1 = Label(root,text='         Hide Your Face        ',font=('Times new Roman',47,'underline'),fg='black')
l1.place(x=8,y=14)
b1 = Button(root,text='   Image  ',font=('Times new Roman',23),command=lambda:for_image(root,classifier),bg='light blue',bd=7)
b1.place(x=247,y=139)
b2 = Button(root,text='Live Video',font=('Times new Roman',23),command=lambda:for_video(classifier),bg='light blue',bd=7)
b2.place(x=237,y=255)

root.mainloop()
