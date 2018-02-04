#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from time import sleep
from picamera import PiCamera
import cv2 as cv


def main():
    camera = PiCamera()
    camera.start_preview()
    sleep(0.1)

    out_path = '/tmp/face_stream'
    if not os.path.exists(out_path):   
        os.mkdir(out_path)

    outfile = out_path + '/face.jpg'
    for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
        detect_face(filename, outfile)
        os.remove(filename)


def detect_face(infile, outfile):
    if not os.path.exists(infile):
        print("Please give input file!")
        return

    if not os.path.exists('haarcascade_frontalface_default.xml'):
        print("Please put haarcascade_frontalface_default.xml in current dir")
        return

    infile_path = os.path.abspath(infile)
    image = cv.imread(infile_path, 1)
    #gray = cv.imread(infile_path, 0)
    haarcascade_frontalface_path = os.path.abspath('haarcascade_frontalface_default.xml')
    face_cascade = cv.CascadeClassifier(haarcascade_frontalface_path)
    faces = face_cascade.detectMultiScale(image, 1.3, 5)

    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv.imwrite(outfile, image)


if __name__ == "__main__":
	main()

