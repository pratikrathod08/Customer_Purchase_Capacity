import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

import matplotlib.pyplot as plt
from io import BytesIO
import base64

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



def data_convert(data):
    try:
        new_dict = {}
        for key, value in data.items():
            if type(value) == list:
                if type(value[0]) == tuple:    
                    if value[0][0].isnumeric():
                        value_0 = [float(value[0][0])]
                    else: 
                        value_0 = [value[0][0]]
                    new_dict[key] = value_0
                else:
                    new_dict[key] = value[0]
        return new_dict

    except Exception as e:
        logging.info("error occure during data conversion")
        raise CustomException(e, sys)

# def pca(data):
#     try:
#         pca = PCA(n_components=3)
#         pca.fit(data)
#         pca_df=pd.DataFrame(pca.transform(data),columns=['col1','col2','col3'])
#         return pca_df
#     except Exception as e:
#         logging.info("exception occure during dimentionality reduction")
#         raise CustomException(e, sys)

def capacity(data):
    if int(data) == 0:
        return "Excelent"
    elif int(data) == 1:
        return "Very Good"
    elif int(data) == 2:
        return "Good"
    elif int(data) == 3:
        return "Worst"
    else:
        return "Fair"

def visualize():
    # features = ['Customer_Age','Education_Level','Income_Category','Card_Category','Credit_Limit','Months_Inactive_Count','Avg_Open_To_Buy','Total_Revolving_Bal','Total_Trans_Amt','Total_Trans_Ct','Avg_Utilization_Ratio']
    
    Clusters = ['Cluster 0','Cluster 1','Cluster 2','Cluster 3',"Cluster 4"]
    rank = [100,80,60,20,40]

    ## plot 1
    fig1, ax1 = plt.subplots()
    ax1.bar(Clusters,rank,color = ["Blue","Green","skyblue","Red","Orange"])
    ax1.set_xlabel("Clusters")
    ax1.set_ylabel("Customer Capacity In Percentage ")
    ax1.set_title("Cluster wise customer purchase capacity ")


    ## save plot 

    buffer1 = BytesIO()
    plt.savefig(buffer1, format="png")
    buffer1.seek(0)
    plot1 = base64.b64encode(buffer1.getvalue()).decode("utf-8")
    # plot1.close()

    return plot1
