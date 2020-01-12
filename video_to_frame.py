# Cut video to frames
# To use the function:
#   "from video_to_frame include video_to_frame"
#   "video_to_frame(filename, result_path)"
import cv2
import os
import glob

# vidcap: video
# sec: fetch in rate
# count: just for filename


def getFrame(vidcap, sec, count, result_path):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite(result_path+str(count).zfill(4)+".jpg",
                    image)     # save frame as JPG file
    return hasFrames


def video_to_frame(filename, result_path):
    # create folder 'image'
    if not os.path.isdir(result_path):
        os.mkdir(result_path)

    vidcap = cv2.VideoCapture(filename)  # get video

    sec = 0
    frameRate = 1/24  # it will capture image in each 1/24 second
    count = 1
    success = getFrame(vidcap, sec, count, result_path)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(vidcap, sec, count, result_path)


def main():
    video_to_frame('406410027.mp4', './/27_ori_image//')
    print('video_to_frame Done.')


if __name__ == "__main__":
    main()
