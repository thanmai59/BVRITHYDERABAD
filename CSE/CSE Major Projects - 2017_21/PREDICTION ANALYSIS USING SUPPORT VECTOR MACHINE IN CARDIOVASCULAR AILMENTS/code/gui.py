import tkinter
from tkinter import Label, Entry, LabelFrame,Button
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def takeInput():
    inputValues = []
    inputValues.append(male.get())
    inputValues.append(age.get())
    inputValues.append(currentSmoker.get())
    inputValues.append(BPMeds.get())
    inputValues.append(prevalentStroke.get())
    inputValues.append(prevalentHyp.get())
    inputValues.append(diabetes.get())
    inputValues.append(totChol.get())
    inputValues.append(sysBP.get())
    inputValues.append(diaBP.get())
    inputValues.append(BMI.get())
    inputValues.append(heartRate.get())
    inputValues.append(glucose.get())
    print(inputValues)

    print("\n")
    final_Result = svc_model.predict([inputValues])
    print(final_Result)

    substituteWindow = tkinter.Tk()
    substituteWindow.geometry('640x480-8-200')
    substituteWindow.title("RESULT PREDICTION")

    substituteWindow.columnconfigure(0, weight=1)
    substituteWindow.columnconfigure(1, weight=1)
    substituteWindow.columnconfigure(2, weight=2)
    substituteWindow.columnconfigure(3, weight=2)
    substituteWindow.rowconfigure(0, weight=0)
    substituteWindow.rowconfigure(1, weight=0)
    substituteWindow.rowconfigure(2, weight=0)
    substituteWindow.rowconfigure(3, weight=1)
    substituteWindow.rowconfigure(4, weight=1)
    substituteWindow.rowconfigure(5, weight=1)
    substituteWindow.rowconfigure(6, weight=1)
    substituteWindow.rowconfigure(7, weight=1)
    substituteWindow.rowconfigure(8, weight=10)

    if final_Result[0] == 1:

        label1 = Label(substituteWindow, text="HEART DISEASE PREDICTED", font=('Impact', -35), bg='#ff8000')
        label1.grid(row=3, column=0, columnspan=6)

        label2 = Label(substituteWindow, text="PLEASE VISIT NEAREST CARDIOLOGIST AT THE EARLIEST", font=('Impact', -20), fg='white', bg='red')
        label2.grid(row=5, column=0, columnspan=5)
    else:
        label1 = Label(substituteWindow, text="NO PREDICTION OF HEART DISEASES", font=('Impact', -35), bg='#ff8000')
        label1.grid(row=3, column=0, columnspan=6)

        label2 = Label(substituteWindow, text="Do not forget to exercise daily.", font=('Impact', -20), fg='white', bg='green')
        label2.grid(row=5, column=0, columnspan=5)

    substituteWindow.mainloop()


def gr():

    data1 = {'Algorithm': ['SVM', 'SGD','LR'],
             'Accuracy': [85.61,85.14,85.49]
        }
    df1 = DataFrame(data1, columns=['Algorithm', 'Accuracy'])

    root = tkinter.Tk()
    root.geometry('640x480-8-200')
    root['padx'] = 20
    root.title("Graph")

    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    df1 = df1[['Algorithm', 'Accuracy']].groupby('Algorithm').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Comparison Between Algorithms')
    ax1.set_ylim(83, 86)

    root.mainloop()
data = pd.read_csv("data.csv")
# education can not have relation with CHD.
data.drop(['education'], axis=1, inplace=True)
for value in ['cigsPerDay','BPMeds', 'totChol','BMI','glucose','heartRate']:
    data[value].fillna(round(data[value].mean()), inplace= True)
data= data[data['totChol']<600.0]
data = data[data['sysBP']<295.0]
data=data.drop('cigsPerDay',axis=1)
X = data.values[:,0:-1]
Y = data.values[:,-1]

# Feature scaling for normalization of data in range(0, 1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
Y= Y.astype(int)
# Separate output column as Y and rest as X
Y = data['TenYearCHD']
X = data.drop(['TenYearCHD'], axis = 1)

# Splitting data to train and test

from sklearn.model_selection import train_test_split
#Split the data into test and train
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=10)
from sklearn.svm import SVC

svc_model= SVC(kernel="rbf",gamma=0.1,C= 80)
svc_model.fit(X_train,Y_train)



mainWindow = tkinter.Tk()
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 20
mainWindow.title("Prediction analysis using support vector machine in cardiovascular ailments")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=2)
mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)
mainWindow.rowconfigure(7, weight=1)
mainWindow.rowconfigure(8, weight=10)

label1 = Label(mainWindow, text="HEART DISEASE PREDICTION MODEL", font=('Impact', -35), bg='#ff8000')
label1.grid(row=0, column=0, columnspan=6)

label2 = Label(mainWindow, text="Enter the details carefully", font=('Impact', -25), fg='white', bg='#ff0000')
label2.grid(row=2, column=0, columnspan=5)

# frame for the feature inputs

# frame for the feature inputs
maleFrame = LabelFrame(mainWindow, text="Gender(Male-1/Female-0)")
maleFrame.grid(row=3, column=0)
maleFrame.config(font=("Courier", -15))
male = Entry(maleFrame)
male.grid(row=3, column=3, sticky='nw')

ageFrame = LabelFrame(mainWindow, text="Age(10-100 yrs)")
ageFrame.grid(row=3, column=1)
ageFrame.config(font=("Courier", -15))
age = Entry(ageFrame)
age.grid(row=3, column=3, sticky='nw')


currentSmokerFrame = LabelFrame(mainWindow, text="Smoking Habit(yes-1/no-0)")
currentSmokerFrame.grid(row=3, column=2)
currentSmokerFrame.config(font=("Courier", -15))
currentSmoker = Entry(currentSmokerFrame)
currentSmoker.grid(row=3, column=3, sticky='nw')

BPMedsFrame = LabelFrame(mainWindow, text="BP Medication(yes-1/no-0)")
BPMedsFrame.grid(row=4, column=0)
BPMedsFrame.config(font=("Courier", -15))
BPMeds = Entry(BPMedsFrame)
BPMeds.grid(row=3, column=3, sticky='nw')

prevalentStrokeFrame = LabelFrame(mainWindow, text="PrevalentStroke(yes-1/no-0)")
prevalentStrokeFrame.grid(row=4, column=1)
prevalentStrokeFrame.config(font=("Courier", -15))
prevalentStroke= Entry(prevalentStrokeFrame)
prevalentStroke.grid(row=3, column=3, sticky='nw')

prevalentHypFrame = LabelFrame(mainWindow, text="PrevalentHyperTension(yes-1/no-0)")
prevalentHypFrame.grid(row=4, column=2)
prevalentHypFrame.config(font=("Courier", -15))
prevalentHyp = Entry(prevalentHypFrame)
prevalentHyp.grid(row=3, column=3, sticky='nw')

diabetesFrame = LabelFrame(mainWindow, text="Diabetes(yes-1/no-0)")
diabetesFrame.grid(row=5, column=0)
diabetesFrame.config(font=("Courier", -15))
diabetes = Entry(diabetesFrame)
diabetes.grid(row=3, column=3, sticky='nw')

totCholFrame = LabelFrame(mainWindow, text="TotalCholesterol(100-600)")
totCholFrame.grid(row=5, column=1)
totCholFrame.config(font=("Courier", -15))
totChol = Entry(totCholFrame)
totChol.grid(row=3, column=3, sticky='nw')

sysBPFrame = LabelFrame(mainWindow, text="SystolicBloodPressure(83-295)")
sysBPFrame.grid(row=5, column=2)
sysBPFrame.config(font=("Courier", -15))
sysBP = Entry(sysBPFrame)
sysBP.grid(row=3, column=3, sticky='nw')

diaBPFrame = LabelFrame(mainWindow, text="DiastolicBloodPressure(48-142)")
diaBPFrame.grid(row=6, column=0)
diaBPFrame.config(font=("Courier", -15))
diaBP = Entry(diaBPFrame)
diaBP.grid(row=3, column=3, sticky='nw')

BMIFrame = LabelFrame(mainWindow, text=" BMI(15-56)")
BMIFrame.grid(row=6, column=1)
BMIFrame.config(font=("Courier", -15))
BMI = Entry(BMIFrame)
BMI.grid(row=3, column=3, sticky='nw')

heartRateFrame = LabelFrame(mainWindow, text="HeartRate(44-143)")
heartRateFrame.grid(row=6, column=2)
heartRateFrame.config(font=("Courier", -15))
heartRate = Entry(heartRateFrame)
heartRate.grid(row=3, column=3, sticky='nw')

glucoseFrame = LabelFrame(mainWindow, text="Glucose(40-394)")
glucoseFrame.grid(row=7, column=0)
glucoseFrame.config(font=("Courier", -15))
glucose = Entry(glucoseFrame)
glucose.grid(row=3, column=3, sticky='nw')

analyseButton = Button(mainWindow, text="PREDICT",
                       font=('Impact', -25), bg='green', command=takeInput)
analyseButton.grid(row=8, column=0, columnspan=5)

analyseButton = Button(mainWindow, text="PLOT",
                       font=('Impact', -25), bg='green', command=gr)
analyseButton.grid(row=9, column=0, columnspan=10)
mainWindow.mainloop()
