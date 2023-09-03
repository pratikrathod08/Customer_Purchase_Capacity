import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from src.utils import load_object , data_convert 

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,feature):
        try:
            preprocessor_path= os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(feature)
            logging.info(f"Scaled data : {data_scaled}")

            prediction = model.predict(data_scaled)
            return prediction
            logging.info(f" prediction done result is : {prediction}")

        except Exception as e:
            logging.info("Exception occure during prediction")
            raise CustomException(e, sys)

class CustomData:
    def __init__(
        self,
        Client_Id,
        Attrition_Flag,
        Customer_Age,
        Gender,
        Dependent_count,
        Education_Level,
        Marital_Status,
        Income_Category,
        Card_Category,
        Months_on_book,
        Total_Relationship_Count,
        Months_Inactive_Count,
        Contacts_Count,
        Credit_Limit,
        Total_Revolving_Bal,
        Avg_Open_To_Buy,
        Total_Trans_Amt,
        Total_Trans_Ct,
        Avg_Utilization_Ratio
        ):
        self.Client_Id=Client_Id,
        self.Attrition_Flag=Attrition_Flag,
        self.Customer_Age=Customer_Age,
        self.Gender=Gender,
        self.Dependent_count=Dependent_count,
        self.Education_Level=Education_Level,
        self.Marital_Status=Marital_Status,
        self.Income_Category=Income_Category,
        self.Card_Category=Card_Category,
        self.Months_on_book=Months_on_book,
        self.Total_Relationship_Count=Total_Relationship_Count,
        self.Months_Inactive_Count=Months_Inactive_Count,
        self.Contacts_Count=Contacts_Count,
        self.Credit_Limit=Credit_Limit,
        self.Total_Revolving_Bal=Total_Revolving_Bal,
        self.Avg_Open_To_Buy=Avg_Open_To_Buy,
        self.Total_Trans_Amt=Total_Trans_Amt,
        self.Total_Trans_Ct=Total_Trans_Ct,
        self.Avg_Utilization_Ratio=Avg_Utilization_Ratio

        logging.info("custom data collected")

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict={
            "Client_Id":[self.Client_Id],
            "Attrition_Flag":[self.Attrition_Flag],
            "Customer_Age":[self.Customer_Age],
            "Gender":[self.Gender],
            "Dependent_count":[self.Dependent_count],
            "Education_Level":[self.Education_Level],
            "Marital_Status":[self.Marital_Status],
            "Income_Category":[self.Income_Category],
            "Card_Category":[self.Card_Category],
            "Months_on_book":[self.Months_on_book],
            "Total_Relationship_Count":[self.Total_Relationship_Count],
            "Months_Inactive_Count":[self.Months_Inactive_Count],
            "Contacts_Count":[self.Contacts_Count],
            "Credit_Limit":[self.Credit_Limit],
            "Total_Revolving_Bal":[self.Total_Revolving_Bal],
            "Avg_Open_To_Buy":[self.Avg_Open_To_Buy],
            "Total_Trans_Amt":[self.Total_Trans_Amt],
            "Total_Trans_Ct":[self.Total_Trans_Ct],
            "Avg_Utilization_Ratio":[self.Avg_Utilization_Ratio]

            }

            logging.info(f"custom data dict : {custom_data_input_dict}")
            new_dict = data_convert(custom_data_input_dict)
            logging.info(f"new dict created with converted data type : {new_dict}")
            df = pd.DataFrame(new_dict)
            logging.info("Dataframe Gathered")
            logging.info(f"new data dataframe : {df.head()}")
            return df

        except Exception as e:
            logging.info("Exception occure during getting data as dataframe")
            raise CustomException(e, sys)

