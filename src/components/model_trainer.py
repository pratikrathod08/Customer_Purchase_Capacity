import os
import sys
import pandas as pd
import numpy as np
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
import warnings
warnings.filterwarnings("ignore")

from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass
from src.utils import knee_locator , model_evaluation, save_object


@dataclass
class ModelTrainingconfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainingconfig()

    def initiate_model_training(self,processed_data):
        try:
            logging.info('Model training initiated')

            df=pd.DataFrame(processed_data)
            logging.info(f"Processed df fot find knee and silhoutte score : {df.head()}")

            ## reduction in dimentionality of data
            # pca = PCA(n_components=3)
            # pca.fit(processed_data)
            # pca_df=pd.DataFrame(pca.transform(processed_data),columns=['col1','col2','col3'])
            # logging.info(f"Dimentionality reducted of data : {pca_df.head()}")

            ## knee finding

            knee,silhouette_dict =knee_locator(df)

            logging.info(f"Knee located : {knee}")
            logging.info(f"silhoutte score with no of clusters {silhouette_dict}")
            print(f"Knee : {knee}")
            print(f"silhouette score : {silhouette_dict}")

            ## model training
            ## We will go with maximum silhoutte score which is from 5 cluster

            kmeans = KMeans(n_clusters=5,init="k-means++")

            clusters = kmeans.fit_predict(df)
            df['clusters'] = clusters
            processed_clustered_data = pd.concat([pd.DataFrame(df),pd.Series(clusters)],axis=1,ignore_index=True)
            logging.info("Clusters created")

            ## evaluation of classification model

            accuracy_dict,DecisionTreeConfusionMetrix,SVMConfusionMetrix = model_evaluation(processed_clustered_data)

            logging.info(f"accuracy score for model classification : \n{accuracy_dict}")
            logging.info(f"Confusion metrix of Decision Tree : \n{DecisionTreeConfusionMetrix}")
            logging.info(f"Confusion Metrix SVM : \n{SVMConfusionMetrix}")

            print(f"Accuracy of classification model : {accuracy_dict}")

            ## save model 

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=kmeans
                )

        except Exception as e:
            logging.info("exception during model training")
            raise CustomException(e,sys)