import os
import sys

from flask import Flask, request, Response, render_template, jsonify

import matplotlib.pyplot as plt
from io import BytesIO
import base64

from src.pipelines.prediction_pipeline import CustomData,PredictionPipeline
from src.logger import logging
from src.exception import CustomException
from src.utils import capacity , visualize

from pymongo.mongo_client import MongoClient

import warnings
warnings.filterwarnings("ignore")

application = Flask(__name__)

app = application

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        logging.info("Get request received forwarded to home page ")
        return render_template("form.html")

    else:
        logging.info("Post request received go to prediction")
        try:
            data = CustomData(
            Client_Id=request.form.get("Client_Id"),
            Attrition_Flag=request.form.get("Attrition_Flag"),
            Customer_Age=request.form.get("Customer_Age"),
            Gender=request.form.get("Gender"),
            Dependent_count=request.form.get("Dependent_count"),
            Education_Level=request.form.get("Education_Level"),
            Marital_Status=request.form.get("Marital_Status"),
            Income_Category=request.form.get("Income_Category"),
            Card_Category=request.form.get("Card_Category"),
            Months_on_book=request.form.get("Months_on_book"),
            Total_Relationship_Count=request.form.get("Total_Relationship_Count"),
            Months_Inactive_Count=request.form.get("Months_Inactive_Count"),
            Contacts_Count=request.form.get("Contacts_Count"),
            Credit_Limit=request.form.get("Credit_Limit"),
            Total_Revolving_Bal=request.form.get("Total_Revolving_Bal"),
            Avg_Open_To_Buy=request.form.get("Avg_Open_To_Buy"),
            Total_Trans_Amt=request.form.get("Total_Trans_Amt"),
            Total_Trans_Ct=request.form.get("Total_Trans_Ct"),
            Avg_Utilization_Ratio=request.form.get("Avg_Utilization_Ratio")
            )

            logging.info("custom data collected")

            final_new_data = data.get_data_as_dataframe()
            logging.info("data converted into dataframe")
            predict_pipeline = PredictionPipeline()
            pred = predict_pipeline.predict(final_new_data)
            logging.info("prediction completed on new data")
            logging.info(f"Prediction : {pred}")
            cap = capacity(pred[0])
            logging.info(f"Customer Capacity : {cap}")
            plot = visualize()
            logging.info(f"Make plot for understand result ")

            data_dict = final_new_data.to_dict('list')
            data_dict['Result'] = str(pred)
            data_dict['Capacity'] = cap
            logging.info(f"New Data With Prediction : {data_dict}")

            uri = "mongodb+srv://08Pratik:08Pratik@cluster0.vd8ss6z.mongodb.net/?retryWrites=true&w=majority"
            # Create a new client and connect to the server
            client = MongoClient(uri)
            DB = client['Customer_Purchase_Capacity']
            coll = DB['Prediction']
            coll.insert_one(data_dict)
            logging.info("Data successfully Uploaded on mongodb atlas")

            return render_template("result.html",plot1=plot , cls = pred[0],review=cap)


        except Exception as e:
            logging.info("Exception occure during post method")
            raise CustomException(e,sys)

        


if __name__ =="__main__":
    app.run(host="0.0.0.0",port=8080)
