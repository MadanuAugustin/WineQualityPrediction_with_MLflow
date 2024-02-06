from src.WineQualityPrediction_with_MLflow import logger
# from src.WineQualityPrediction_with_MLflow import logger
from src.WineQualityPrediction_with_MLflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# we can import logger in either way
# since we have written logging inside the constructor file of WineQualityPrediction_with_MLflow folder we don't have to mention src folder

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f">>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx===============x")

except Exception as e:
            logger.exception(e)
            raise e