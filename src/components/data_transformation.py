from sklearn.impute import SimpleImputer           ## Handling missing values
from sklearn.preprocessing import StandardScaler   ## Handling feature scalling
from sklearn.preprocessing import OrdinalEncoder   ## For encoding categorical data
from sklearn.pipeline import Pipeline              ## To Create pipeline 
from sklearn.compose import ColumnTransformer      ## To merge all columns 

import pandas as pd
import numpy as np
from dataclasses import dataclass
import sys, os

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object



## data transformation config

@dataclass
class DataTransformationconfig:
    preprocessor_obj_path = os.path.join('artifacts','preprocessor.pkl')

## data ingestionconfig class


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationconfig()

    def get_data_transformation_object(self):
        try:
            logging.info("Data Transformation initiated ")


            ## define which column should ordinal transform and which should be scaled
            ## segregation of numerical and categorical columns

            # categorical_cols=df.select_dtypes(include='object').columns
            # numerical_cols = df.select_dtypes(exclude='object').columns

            categorical_cols = ['Attrition_Flag', 'Gender', 'Education_Level', 'Marital_Status',
                'Income_Category', 'Card_Category']
            numerical_cols = ['Customer_Age', 'Dependent_count', 'Months_on_book',
                'Total_Relationship_Count', 'Months_Inactive_Count', 'Contacts_Count',
                'Credit_Limit', 'Total_Revolving_Bal', 'Avg_Open_To_Buy',
                'Total_Trans_Amt', 'Total_Trans_Ct']

            ## define custom ranking for each column for ordinal transformation

            Attrition_Flag_categories=['Attrited Customer','Existing Customer']
            Gender_categories=['F','M']
            Education_Level_categories=['Uneducated','High School','College','Graduate','Post-Graduate','Doctorate']
            Marital_Status_categories=['Divorced','Single','Married']
            Income_Category_categories=['Unknown','Less than $40K','$40K - $60K','$60K - $80K','$80K - $120K','$120K +']
            Card_Category_categories=['Blue', 'Silver','Gold','Platinum']

            ## Pipeline creation 
            ## Numeric pipeline

            num_pipeline=Pipeline(
            steps=[
                ('scaler',StandardScaler())
            ])

            ## categorical pipeline

            cat_pipeline = Pipeline(
            steps=[
                ('ordinalencoder',OrdinalEncoder(categories=[Attrition_Flag_categories,Gender_categories,Education_Level_categories,Marital_Status_categories,Income_Category_categories,Card_Category_categories])),
                ('scaler',StandardScaler())
            ])

            ## preprocessor

            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
                
            ])

            return preprocessor

            logging.info("pipeline created")


        except Exception as e:
            logging.info("exception occure during get data transformation object.")
            raise CustomException(e, sys)

    def initiate_data_transformation(self,raw_data_path):
        try:
            
            raw_df = pd.read_csv(raw_data_path)

            ## removed insignificant column for prediction
            
            raw_df=raw_df.drop(labels=['Client_Id','Avg_Utilization_Ratio'],axis=1)

            # raw_df.drop(labels='Client_Id',axis=1,inplace=True)

            logging.info('Reading of data completed')
            logging.info(f"Raw data head : {raw_df.head().to_string()}")

            logging.info("Obtaining preprocessor object")

            preprocessor_obj = self.get_data_transformation_object()

            ## apply transforamtion 

            preprocessed_data = pd.DataFrame(preprocessor_obj.fit_transform(raw_df),columns=list(raw_df.columns))

            logging.info("Data preprocessing completed")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_path,
                obj=preprocessor_obj)

            return(
                preprocessed_data
            )  


        except Exception as e:
            logging.info('Exception occure during transformation')
            raise CustomException(e, sys)

