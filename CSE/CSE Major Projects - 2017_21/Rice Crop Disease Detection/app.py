from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


import os, sys, glob, re

app = Flask(__name__)

model_path = "rice.h5"



classes = {0:"bacterial_leaf_blight:-{ About bacterial_leaf_blight disease }",1:"blast:-{ about blast disease} ",2:"brownspot:-{ about brownspot disease }"}

def model_predict(image_path):
    print("Predicted")
    image = load_img(image_path,target_size=(224,224))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    model = load_model(model_path)
    result = np.argmax(model.predict(image))
    prediction = classes[result]
    
    
    if result == 0:
        print("bacterial_leaf_blight.html")
        
        return "bacterial_leaf_blight","bacterial_leaf_blight.html"
    elif result == 1:
        print("blast.html")
        
        return "blast", "blast.html"
    elif result == 2:
        print("brownspot.html")     
               
        return "brownspot" , "brownspot.html"
    


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/predict',methods=['GET','POST'])
def predict():
    print("Entered")
    if request.method == 'POST':
        print("Entered here")
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = model_predict(file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    


if __name__ == '__main__':
    app.run(debug=True,threaded=False)
    
