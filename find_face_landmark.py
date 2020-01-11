# Find face landmarks 
# To use the function:
#   "from find_face_landmark include find_face_landmark"
#   "find_face_landmark(coordinates_txt, image_folder)"
from imutils.video import VideoStream
from imutils import face_utils
import argparse
import imutils
import time
import dlib
import cv2
import os
import glob

# Load pretrained model's parameters
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    ".//cascades//shape_predictor_68_face_landmarks.dat")

def detect_face_landmarks(filename, coordinates_txt):
    # store x, y
    with open(coordinates_txt, 'a') as f:
        f.write(' [')

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        (x, y, w, h) = face_utils.rect_to_bb(face)

        for (x, y) in shape:
            # 圖像、圓心、半徑、顏色、第五個參數正數為線的粗細，負數則為填滿
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

            # Store the coordinates of (x, y)
            with open(coordinates_txt, 'a') as f:
                f.write(str(x) + ' ' + str(y) + ' ')
    
    with open(coordinates_txt, 'a') as f:
        f.write(']\n')

    cv2.imwrite(filename, img)
    

def find_face_landmark(image_folder, coordinates_txt):
    # init coordinates_txt
    with open(coordinates_txt, 'w') as f:
        f.write('')

    # Get all image files
    files = glob.iglob(image_folder + '*.jpg')
    for file in files:
        detect_face_landmarks(file, coordinates_txt)


def main():
    find_face_landmark('.//image//', '27_landmarks.txt')

if __name__ == "__main__":
    main()
