from video_to_frame import video_to_frame
from find_face_landmark import find_face_landmark

# Cut mp4 in frames and stores in folder "image"
video_to_frame('406410027.mp4', './/image//')

# find the landmark from the folder "image" then stores coordinates in *.txt
find_face_landmark('.//image//', '27_landmarks.txt') 
