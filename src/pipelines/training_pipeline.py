import os
import sys
from src.logger import logging
from src.exception import CustomException

import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":

    logging.info("Training pipeline started")
    obj = DataIngestion()
    raw_data_path = obj.initiate_data_ingestion()
    logging.info("Data ingestion done for training pipeline")

    data_transformation = DataTransformation()
    processed_data=data_transformation.initiate_data_transformation(raw_data_path=raw_data_path)
    logging.info("Data transformation done for training pipeline")

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(processed_data)
    logging.info("Model trainer completed for training pipeline")

    logging.info("Training pipeline completed")






