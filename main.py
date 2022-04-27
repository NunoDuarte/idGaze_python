# activate anaconda environment:export PATH="/home/nduarte/anaconda3/bin:$PATH" && source activate pupilos || puupilos-10
# python3 main.py --buffer 68

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import sys
sys.path.insert(1, 'src/')

from object_tracking import Color
# from face_detector import FaceDetector as Face
#from face_detector_gpu import FaceGPU as Face
from gaze_behaviour import GazeBehaviour
from pupil_lsl_yarp import LSL

#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np
import cv2

# initialize packages
lsl = LSL()
#faceTracking = Face()
objtTracking = Color()
gazeTracking = GazeBehaviour(lsl.outlet)

# A window will open. To close, press 'q'.
i = 0
#with faceTracking.detection_graph.as_default():
with tf.Session() as sess:
    while cv2.waitKey(1) & 0xFF != ord('q'):
        topic, msg = lsl.recv_from_sub()

        if topic == 'frame.world' and i % 2 == 0:
            frame = np.frombuffer(msg['__raw_data__'][0], dtype=np.uint8).reshape(msg['height'], msg['width'], 3)

            if frame is not None:
                height, width, channels = frame.shape

                # object (color) detection          [G, R, B, Y, C]
                objts = objtTracking.tracking(frame, [1, 1, 1, 0, 1])

                # iCub face
                face = None
                #if i % 8 == 0:
                #    face = faceTracking.detect(frame, sess)

                # pupil
                sample = []
                sampling, timestamp = lsl.inlet.pull_chunk(timeout=0.0, max_samples=1024, dest_obj=None)
                if sampling:
                    sample_dic = sampling[0][0]
                    sample_split = sample_dic.split()

                    matching = [n for n, x in enumerate(sample_split) if "'norm_pos':" in x]
                    x = float(sample_split[matching[0]+1][1:-1])
                    y = float(sample_split[matching[0]+2][:-2])
                    sample = [[[], x, y]]
                    # print(sample)

                # sample, timestamp = lsl.inlet.pull_chunk()
                if sample:
                    # push to yarp port
                    gazeTracking.push(frame, sample, objts, face, width, height, lsl)

                # clear buffer of object for new frame
                objtTracking.all_objts = []

            cv2.imshow('frame', frame)
        i = i + 1

print(gazeTracking.gaze_sequence)
cv2.destroyAllWindows()
