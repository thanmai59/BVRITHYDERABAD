#Importing necessary libraries

from numpy import exp
from matplotlib import pyplot as plt
import numpy as np
import cv2
import pywt

from google.colab import drive
drive.mount('/content/drive')

#Loading dataset, Grayscale conversion and Adaptive histogram equalization

enhanced_images = []
for i in range(1, 90) :
    img_path = r'/content/drive/MyDrive/Dataset/image'
    if i < 10 :
        img_path = img_path + "00" + str(i) + ".png"
    else :
        img_path = img_path + "0" + str(i) + ".png"

    img = cv2.imread(img_path) #matrix of pixels in image
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale conversion
    equalized_img = cv2.equalizeHist(grayscale_img) #adaptive histogram equalization
    enhanced_images.append(np.array(equalized_img).flatten())

#Dimensions of the images

print("Dimensions of original image : ")
print(np.shape(img))
print("Dimensions of grayscale image : ")
print(np.shape(grayscale_img))
print("Dimensions of histogram equalized image : ")
print(np.shape(equalized_img))
print("Dimensions of flattened image : ")
print(np.shape(np.array(equalized_img).flatten()))
print("Dimensions of enhanced : ")
print(np.shape(enhanced_images))
print("No. of elements in enhanced : ")
print(len(enhanced_images))

#Visualizing a random image from the dataset

random_image_path = '/content/drive/MyDrive/Dataset/image079.png'
random_image = cv2.imread(random_image_path)
grayscale_img = cv2.cvtColor(random_image, cv2.COLOR_BGR2GRAY)
print("Grayscale image : ")
plt.imshow(grayscale_img, cmap='gray')
plt.show()
equalized_img = cv2.equalizeHist(grayscale_img)
print("AHE image : ")
plt.imshow(equalized_img, cmap='gray')
plt.show()

#Discrete wavelet transform

dwt_images = []
for equalized_img in enhanced_images :
    equalized_img = equalized_img.reshape((1152,1500))
    coeffs = pywt.dwt2(equalized_img, 'haar') #coeffs - (approximation coeff, details coeff) -> (cA, (cH, cV, cD))
    wavelet_transformed = pywt.idwt2(coeffs, 'haar') #Inverse discrete wavelet transform
    dwt_images.append(np.array(wavelet_transformed).flatten())

#Visualizing the random image after dwt

print("DWT image : ")
plt.imshow(dwt_images[78].reshape((1152,1500)),cmap='gray')
plt.show()

#Visualizing the random image's coefficient matrices returned by dwt

original = enhanced_images[78].reshape((1152, 1500))
# Wavelet transform of image, and plot approximation and details
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(original, 'bior1.3')
LL, (LH, HL, HH) = coeffs2
fig = plt.figure(figsize=(12, 3))
for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(1, 4, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

fig.tight_layout()
plt.show()

#Feature extraction using Gabor filters

def createGaborFilterBank() :
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 16) : #varying angles
        kernel = cv2.getGaborKernel((ksize, ksize), 6, theta, 12, 0.37, 0, ktype = cv2.CV_32F) #creates a kernel
        kernel /= 1.5 * kernel.sum() #normalizing the kernel
        filters.append(kernel)
    return filters #returns the list of 16 kernels of size 31 x 31

def applyFilters(image, kernels) :
    images = np.array([cv2.filter2D(image, -1, k) for k in kernels])
    return np.max(images, 0) #returns the filtered image

gaborKernel_images = []
for wavelet_transformed_1d in dwt_images : #89 images after dwt
    wavelet_transformed_2d = wavelet_transformed_1d.reshape((1152,1500))
    filtered_image = applyFilters(wavelet_transformed_2d, createGaborFilterBank()) #apply gabor filters to each image
    gaborKernel_images.append(np.array(filtered_image).flatten())
   
#Visualizing the random image after applying gabor filters

print("Image after applying gabor filter : ")
plt.imshow(gaborKernel_images[78].reshape((1152,1500)), cmap = 'gray')
plt.show()

#Visualizing the filter bank

filterBank = createGaborFilterBank()
for kernel in filterBank :
  plt.imshow(kernel.reshape((31, 31)))
  plt.show()

#Visualizing the convoluted images

randomImage_dwt = dwt_images[78].reshape((1152,1500))
for kernel in createGaborFilterBank() :
  filtered_image = cv2.filter2D(randomImage_dwt, -1, kernel)
  plt.imshow(filtered_image, cmap = 'gray')
  plt.show()

#Defining labels for the dataset

DR_labels = np.ones(89)
DR_labels[1] = DR_labels[5] = DR_labels[7] = DR_labels[17] = DR_labels[6] = 0 #These images are marked as healthy eye images in the dataset

#Splitting the dataset into Train and test images into different ratios; 70 : 30, 60 : 40, 80 : 20

from sklearn.model_selection import train_test_split
X_train_70, X_test_30, y_train_70, y_test_30 = train_test_split(gaborKernel_images, DR_labels, test_size = 0.3)
X_train_60, X_test_40, y_train_60, y_test_40 = train_test_split(gaborKernel_images, DR_labels, test_size = 0.4)
X_train_80, X_test_20, y_train_80, y_test_20 = train_test_split(gaborKernel_images, DR_labels, test_size = 0.2)

#Classification using Support Vector Machine

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
clf = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
 
def svmClassification(train, test, labelsTrain, labelsTest, clf) :
  clf.fit(train, labelsTrain)
  pred_labels = clf.predict(test)
  accuracy = accuracy_score(labelsTest, pred_labels)
  return accuracy

print(svmClassification(X_train_60, X_test_40, y_train_60, y_test_40, clf)) #94.4%
print(svmClassification(X_train_70, X_test_30, y_train_70, y_test_30, clf)) #96.2%
print(svmClassification(X_train_80, X_test_20, y_train_80, y_test_20, clf)) #88.8%

#Classification using K-Nearest Neighbors Classifier

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors = 3)

def knnClassification(train, test, labelsTrain, labelsTest, clf) :
  clf.fit(train, labelsTrain)
  p = clf.predict(test)
  accuracy = accuracy_score(labelsTest, p)
  return accuracy

print(knnClassification(X_train_60, X_test_40, y_train_60, y_test_40, neigh)) #88.8%
print(knnClassification(X_train_70, X_test_30, y_train_70, y_test_30, neigh)) #92.5%
print(knnClassification(X_train_80, X_test_20, y_train_80, y_test_20, neigh)) #94.4%

#Classification using RandomForest Classifier

from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
rfc = RandomForestClassifier(n_estimators = 25, random_state = 0)

def rfClassification(train, test, labelsTrain, labelsTest, clf) :
  clf.fit(train, labelsTrain)
  p = clf.predict(test)
  accuracy = accuracy_score(labelsTest, p)
  return accuracy

print(rfClassification(X_train_60, X_test_40, y_train_60, y_test_40, rfc)) #91.6%
print(rfClassification(X_train_70, X_test_30, y_train_70, y_test_30, rfc)) #96.2%
print(rfClassification(X_train_80, X_test_20, y_train_80, y_test_20, rfc)) #94.4%

