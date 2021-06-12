from distancein import social_distancing_config as config
from distancein.detection import detect_people
from distancein.mailer import Mailer
from scipy.spatial import distance as dist
import numpy as np
import argparse
import imutils
import cv2
import os
import streamlit as st
import datetime
import wget

st.title("COVID-19 Social Distance Monitoring System")
st.subheader('A GUI Based Social Distancing Detector')

#cuda = st.selectbox('NVIDIA CUDA GPU should be used?', ('True', 'False'))
MIN_CONF = st.slider('Minimum probability To Filter Weak Detections', 0.0, 1.0, 0.3)
NMS_THRESH = st.slider('Non-Maxima suppression Threshold', 0.0, 1.0, 0.3)
st.subheader('Test the model with vedio for Detection')
option = st.selectbox('Choose your option',
                      ('Demo1', 'Demo2', 'Demo3','Demo4','Demo5'))

MIN_CONF = float(MIN_CONF)
NMS_THRESH = float(NMS_THRESH)

MIN_DISTANCE = 50
#USE_GPU = bool(cuda)

# load the COCO class labels our YOLO model was trained on
labelsPath = os.path.sep.join([config.MODEL_PATH, "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")

# paths to the YOLO weights and model configuration
weightsPath = os.path.sep.join([config.MODEL_PATH, "yolov3.weights"])
configPath = os.path.sep.join([config.MODEL_PATH, "yolov3.cfg"])

net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

if st.button('Start'):

    st.info("[INFO] loading YOLO from disk...")
    st.info("[INFO] accessing video stream...")
    if option == "Demo1":
        vs = cv2.VideoCapture('input.mp4')
    elif option == "Demo2":
        vs = cv2.VideoCapture('input2.mp4')
    elif option == "Demo3":
        vs = cv2.VideoCapture('input3.mp4')
    elif option == "Demo4":
        vs = cv2.VideoCapture('input4.mp4')
    elif option == "Demo5":
        vs = cv2.VideoCapture('input5.mp4')
    writer = None

    image_placeholder = st.empty()

    while True:

        (grabbed, frame) = vs.read()

        if not grabbed:
            break

        frame = imutils.resize(frame, width=700)
        results = detect_people(frame, net, ln,
                                personIdx=LABELS.index("person"))

        serious = set()


        if len(results) >= 2:

            centroids = np.array([r[2] for r in results])
            D = dist.cdist(centroids, centroids, metric="euclidean")

            for i in range(0, D.shape[0]):
                for j in range(i + 1, D.shape[1]):

                    if D[i, j] < MIN_DISTANCE:
                        serious.add(i)
                        serious.add(j)

        for (i, (prob, bbox, centroid)) in enumerate(results):

            (startX, startY, endX, endY) = bbox
            (cX, cY) = centroid
            color = (0, 255, 0)

            if i in serious:
                color = (0, 0, 255)

            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
            cv2.circle(frame, (cX, cY), 5, color, 1)

        font = cv2.FONT_HERSHEY_SIMPLEX

        Threshold = "Threshold limit: {}".format(config.Threshold)
        cv2.putText(frame, Threshold, (470, frame.shape[0] - 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.60, (255, 0, 0), 2)
        text = "Social Distancing Violations: {}".format(len(serious))
        cv2.putText(frame, text, (10, frame.shape[0] - 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 255), 3)
#----------------------------------------------alert-------------
        if len(serious) >= config.Threshold:
            cv2.putText(frame, "-ALERT: Violations over limit-", (10, frame.shape[0] - 80),
                        cv2.FONT_HERSHEY_COMPLEX, 0.60, (0, 0, 255), 2)
            if config.ALERT:

                st.info("[INFO] Sending mail...")

                Mailer().send(config.MAIL)
                st.info('[INFO] Mail sent')

                #-------------------
        display = 1
        if display > 0:
            image_placeholder.image(
                frame, caption='Live Social Distancing Monitor Running..!', channels="BGR")

        if writer is not None:
            writer.write(frame)

st.success("STAY HOME STAY SAFE")
