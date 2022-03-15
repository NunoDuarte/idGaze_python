# activate anaconda environment:export PATH="/home/nduarte/anaconda3/bin:$PATH" && source activate pupilos
# python3 main.py --buffer 68

import numpy as np
import cv2
import imutils
import csv
import math
import warnings
import sys
import tensorflow.compat.v1 as tf # import tensorflow version 1
tf.disable_v2_behavior()
warnings.simplefilter(action='ignore', category=FutureWarning)
sys.path.insert(1, 'src/')

from object_tracking import Color
# from face_detector import FaceDetector as Face
from face_detector_gpu import FaceGPU as Face
from gaze_behaviour import GazeBehaviour

def findNearest(array, value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1], idx
    else:
        return array[idx], idx

# initialize packages
faceTracking = Face()
objtTracking = Color()
gazeTracking = GazeBehaviour()

# load test example
folder = 'test/'
cap = cv2.VideoCapture(folder + '/world_viz.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5) # 600
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5) # 337
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(filename+ '.avi', fourcc, 30.0, (width, height))

timestamps_gaze = list()
norm_pos_x = list()
norm_pos_y = list()

with open(folder + '/gaze_positions.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        timestamps_gaze.append(float(row['timestamp']))
        norm_pos_x.append(row['norm_pos_x'])
        norm_pos_y.append(row['norm_pos_y'])

timestamps = np.load(folder + '/world_viz_timestamps.npy')

i = 0
with faceTracking.detection_graph.as_default():
    with tf.Session(graph=faceTracking.detection_graph) as sess:
        while i < length:
            ret, frame = cap.read()

            if frame is not None:
                frame = imutils.resize(frame) #, width=600)
                height, width, channels = frame.shape
                
                # object (color) detection          [G, R, B, Y, C]
                objts = objtTracking.tracking(frame, [0, 1, 0, 0, 1])

                # iCub face
                face = faceTracking.detect(frame, sess)

                # pupil
                # calculate the nearest timestamp for the current frame
                time = timestamps[i]
                time_close, ind = findNearest(timestamps_gaze, float(time))
                # use the x, y position of the closest timestamp norm_pos_*
                sample = np.zeros([1,3])
                sample[0][0] = time_close
                sample[0][1] = norm_pos_x[ind]
                sample[0][2] = norm_pos_y[ind]
                if sample.any():
                    gazeTracking.push(frame, sample, objts, face, width, height, [])

                # clear buffer of object for new frame
                objtTracking.all_objts = []

                cv2.imshow('frame', frame)
                # write the flipped frame
                out.write(frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            # cv2.waitKey(0)
            i = i + 1

print(gazeTracking.gaze_sequence)
cap.release()
out.release()
cv2.destroyAllWindows()
