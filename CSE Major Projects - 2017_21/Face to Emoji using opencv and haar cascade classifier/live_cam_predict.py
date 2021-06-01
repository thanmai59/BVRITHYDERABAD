import cv2
import numpy as np
import glob
from keras.models import model_from_json
from keras.preprocessing import image

# Load model from JSON file
json_file = open('C:\\Users\\dell\\Desktop\\ftep\\fer.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# Load weights and them to model
model.load_weights('fer.h5')

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        break

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.1, 6, minSize=(150, 150))

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        roi_gray = gray_img[y:y + w, x:x + h]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255.0
       
        predictions = model.predict(img_pixels)
        max_index = int(np.argmax(predictions))
        
        emotions = ['neutral', 'happy', 'surprise', 'sadness', 'anger', 'disgust', 'fear']

        EMOTIONS = {'anger':'C:\\Users\\dell\\Desktop\\ftep\\emojis\\anger.png' , 'disgust':'C:\\Users\\dell\\Desktop\\ftep\\emojis\\disgust.png', 'fear':'C:\\Users\\dell\\Desktop\\ftep\\emojis\\fear.png', 'happy':'C:\\Users\\dell\\Desktop\\ftep\\emojis\\happy.png', 'neutral':'C:\\Users\\dell\\Desktop\\ftep\\emojis\\neutral.png','sadness':'C:\\Users\\dell\\Desktop\\ftep\\emojis\\sadness.png', 'surprise':'C:\\Users\\dell\\Desktop\\ftep\\emojis\\surprise.png'}

        pr = emotions[max_index]
        predicted_emotion = pr
        pimg = EMOTIONS[predicted_emotion]
        img1 = cv2.imread(pimg)
        cv2.putText(img, predicted_emotion,(int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
        resized_img = cv2.resize(img,(300, 300))
        img2 = cv2.resize(img1,(300, 300))
        Hori = np.concatenate((resized_img,img2),axis = 1)
        cv2.imshow('Facial Emotion Recognition', Hori)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
