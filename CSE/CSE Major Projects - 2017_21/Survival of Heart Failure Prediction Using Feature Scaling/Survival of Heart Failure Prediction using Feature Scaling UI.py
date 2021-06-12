from tkinter import *
from tkinter import messagebox

import pandas as pd
from sklearn.model_selection import train_test_split

from prettytable import PrettyTable

from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

window = Tk()
window.title("Survival of Heart Failure Prediction using Feature Scaling")

options = [
    "Yes",
    "No",
]

label1 = Label(window, text = "Fill the form")
label1.place(x = 500, y = 20)

label2 = Label(window, text = "Enter the creatiene value")
label2.place(x = 550, y = 100)
creatiene = Entry(window, width = 20)
creatiene.place(x = 720, y = 100)

label3 = Label(window, text = "Enter the ejection value")
label3.place(x = 550, y = 150)
ejection = Entry(window, width = 20)
ejection.place(x = 720, y = 150)

label4 = Label(window, text = "Enter the sodium value")
label4.place(x = 550, y = 200)
sodium = Entry(window, width = 20)
sodium.place(x = 720, y = 200)

label5 = Label(window, text = "Enter the age of patient")
label5.place(x = 550, y = 250)
age = Entry(window, width = 20)
age.place(x = 720, y = 250)

label6 = Label(window, text = "Does the patient have anemia")
label6.place(x = 550, y = 300)
anemia = StringVar()
anemia.set("Yes")
drop_anemia = OptionMenu(window, anemia, *options)
drop_anemia.place(x = 720, y = 300);

label7 = Label(window, text = "Does the patient have BP")
label7.place(x = 550, y = 350)
BP = StringVar()
BP.set("Yes")
drop_bp = OptionMenu(window, BP, *options)
drop_bp.place(x = 720, y = 350);

label8 = Label(window, text = "Enter the follow-up time(days)")
label8.place(x = 550, y = 400)
time = Entry(window, width = 20)
time.place(x = 720, y = 400)

def validation():
    if(creatiene.get() == ""):
        messagebox.showwarning("Required", "Please fill creatiene value")
    elif(ejection.get() == ""):
        messagebox.showwarning("Required", "Please fill ejection value")
    elif(sodium.get() == ""):
        messagebox.showwarning("Required", "Please fill sodium value")
    elif(age.get() == ""):
        messagebox.showwarning("Required", "Enter patient age")
    elif(time.get() == ""):
        messagebox.showwarning("Required", "Please fill time")
    else:
        display()

def display():
    data = pd.read_csv('C:/Users/91949/Desktop/MAJOR PROJECT/S1Data.csv')
    creatiene_ = creatiene.get()
    ejection_ = ejection.get()
    sodium_ = sodium.get()
    age_ = age.get()
    anemia_ = anemia.get()
    if(anemia_ == "Yes"):
        anemia_ = 1
    else:
        anemia_ = 0
    bp = BP.get()
    if(bp == "Yes"):
        bp = 1
    else:
        bp = 0
    Time = time.get()
    input_values = [[Time, bp, anemia_, age_, ejection_, sodium_, creatiene_]]
    x = data[['TIME', 'BP', 'Anaemia', 'Age', 'Ejection.Fraction', 'Sodium', 'Creatinine']]
    y = data['Event']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    table = PrettyTable()
    table.field_names = ["Model", "Death event"]
    models = [
        RandomForestClassifier(n_estimators=17, max_depth=3),
        SVC(kernel='linear'),
        LogisticRegression(),
        DecisionTreeClassifier(),
        KNeighborsClassifier()
    ]
    survival_rate = 0
    for model in models:
        model.fit(x_train, y_train)
        y_res = model.predict(input_values)
        print(y_res[0])
        survival_rate = survival_rate + y_res[0]
        table.add_row([type(model).__name__, format(y_res)])
    danger_level = ["Very High Danger", "High Danger", "Considerable Danger", "Moderate Danger", "Minor Danger", "Little Danger"]
    messagebox.showinfo('Danger Level', danger_level[survival_rate])
Button(window, text = "Submit", command = validation).place(x = 550, y = 450)

window.mainloop()