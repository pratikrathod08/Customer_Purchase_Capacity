import os
import sys
from src.logger import logging
from src.exception import CustomException

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## initialize data ingestion configuration

@dataclass
class DataIngestionconfig:

    raw_data_path:str = os.path.join('artifacts','raw.csv')

## create data ingestion class

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion method Started")

        try:
            df = pd.read_csv(os.path.join("notebooks/data","data_new.csv"))
            logging.info("Data read as pandas dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Raw data created ")

            logging.info("Ingestion of data is completed ")

            return (
                self.ingestion_config.raw_data_path
            )
            
        except Exception as e:
            logging.info(f"Exception occure during data ingestion : {str(e)}")
            raise CustomException(e, sys)


