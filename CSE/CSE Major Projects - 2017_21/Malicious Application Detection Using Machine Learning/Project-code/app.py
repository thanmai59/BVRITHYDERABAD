import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

dataset = pd.read_csv('android.csv')

dataset_X = dataset.iloc[:,[1,2,3,4, 5,6,7,8,9, 10,11,12,13,14,15]].values


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict( final_features )

    if prediction == 1:
        pred = "Malicious Application"
    elif prediction == 0:
        pred = "Benign Application."
    output = pred

    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
