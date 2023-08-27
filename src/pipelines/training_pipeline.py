import os
import sys
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    obj = DataIngestion()
    raw_data_path = obj.initiate_data_ingestion()
    print(raw_data_path)
    print(type(raw_data_path))

    data_transformation = DataTransformation()
    processed_data=data_transformation.initiate_data_transformation(raw_data_path=raw_data_path)
    print(type(processed_data))




