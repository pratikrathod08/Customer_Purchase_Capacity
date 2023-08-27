import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans
from kneed import KneeLocator
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        logging.info("Exception occure during object saving: %s", e)
        raise CustomException(e, sys)

def knee_locator(df):
    try:
        wcss = []
        for k in range(1,11):
            kmeans = KMeans(n_clusters = k, init= "k-means++")
            kmeans.fit(df)
            wcss.append(kmeans.inertia_)

        k1 = KneeLocator(range(1,11),wcss,curve="convex",direction="decreasing")
        knee = k1.knee
        silhouette_coefficient = []
        silhouette_dict = dict()
        for k in range(2,11):
            kmeans = KMeans(n_clusters=k, init="k-means++")
            kmeans.fit(df)
            score= silhouette_score(df,kmeans.labels_)
            silhouette_coefficient.append(score)
            silhouette_dict[k]=score

        return knee , silhouette_dict

    except Exception as e:
        logging.info("exception occure during knee location and silhouette score find")
        raise CustomException(e, sys)

def model_evaluation(df):
    try:
        X=df.iloc[:,:-1]
        y=df.iloc[:,-1]

        ## split data
        X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=42)
        
        ## make object of classifiers
        classifier = DecisionTreeClassifier()
        classifier1 = SVC()
       
        ## Fit model for prediction
        classifier.fit(X_train,y_train)
        classifier1.fit(X_train,y_train)

        ## prediction done
        y_pred = classifier.predict(X_test)
        y_pred1 = classifier1.predict(X_test)

        ## testing of accuracy

        DecisionTreeAccuracy = accuracy_score(y_test, y_pred)
        DecisionTreeConfusionMetrix = confusion_matrix(y_test, y_pred)

        SVMAccuracy = accuracy_score(y_test, y_pred1)
        SVMConfusionMetrix = confusion_matrix(y_test, y_pred1)

        accuracy_dict ={
            "DecisionTreeAccuracy":DecisionTreeAccuracy,
            "SVMAccuracy":SVMAccuracy
            }

        return accuracy_dict,DecisionTreeConfusionMetrix,SVMConfusionMetrix

    except Exception as e:
        logging.info("Exception occured during model evaluation")
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging,info("Exception occure during object load")
        raise CustomException(e, sys)
