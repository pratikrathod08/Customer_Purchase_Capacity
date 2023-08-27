import os
import sys

from flask import Flask, request, Response, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData,PredictionPipeline
from src.logger import logging
from src.exception import CustomException

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
            Client_Id=float(request.form.get("Client_Id")),
            Attrition_Flag=str(request.form.get("Attrition_Flag")),
            Customer_Age=float(request.form.get("Customer_Age")),
            Gender=str(request.form.get("Gender")),
            Dependent_count=float(request.form.get("Dependent_count")),
            Education_Level=str(request.form.get("Education_Level")),
            Marital_Status=str(request.form.get("Marital_Status")),
            Income_Category=str(request.form.get("Income_Category")),
            Card_Category=str(request.form.get("Card_Category")),
            Months_on_book=float(request.form.get("Months_on_book")),
            Total_Relationship_Count=float(request.form.get("Total_Relationship_Count")),
            Months_Inactive_Count=float(request.form.get("Months_Inactive_Count")),
            Contacts_Count=float(request.form.get("Contacts_Count")),
            Credit_Limit=float(request.form.get("Credit_Limit")),
            Total_Revolving_Bal=float(request.form.get("Total_Revolving_Bal")),
            Avg_Open_To_Buy=float(request.form.get("Avg_Open_To_Buy")),
            Total_Trans_Amt=float(request.form.get("Total_Trans_Amt")),
            Total_Trans_Ct=float(request.form.get("Total_Trans_Ct")),
            Avg_Utilization_Ratio=float(request.form.get("Avg_Utilization_Ratio"))
            )

            final_new_data = data.get_data_as_dataframe()
            predict_pipeline = PredictionPipeline()
            pred = predict_pipeline.predict(final_new_data)
            print(pred)

            return render_template("form.html",final_result=pred)


        except Exception as e:
            logging.info("Exception occure during post method")
            raise CustomException(e,sys)






if __name__ =="__main__":
    app.run(host="0.0.0.0")
