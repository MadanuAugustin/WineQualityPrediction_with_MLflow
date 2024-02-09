from src.WineQualityPrediction_with_MLflow import logger
# from src.WineQualityPrediction_with_MLflow import logger
from src.WineQualityPrediction_with_MLflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.WineQualityPrediction_with_MLflow.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.WineQualityPrediction_with_MLflow.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.WineQualityPrediction_with_MLflow.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.WineQualityPrediction_with_MLflow.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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



STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<< \n\n")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME =    'Data Transformation Stage'

try:
     logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<")
     data_ingestion = DataTransformationTrainingPipeline()
     data_ingestion.main()
     logger.info(f" >>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<")

except Exception as e:
     logger.exception(e)
     raise e


STAGE_NAME = 'Model Trainer Stage'

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")

except Exception as e:
     logger.exception(e)
     raise e



STAGE_NAME = 'Model Evaluation stage'

try:
     logger.info(f'>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<')
     data_ingestion = ModelEvaluationTrainingPipeline()
     data_ingestion.main()
     logger.info(f'>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<')

except Exception as e:
     logger.exception(e)
     raise e


