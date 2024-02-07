
from src.WineQualityPrediction_with_MLflow.config.configuration import ConfigurationManager
from src.WineQualityPrediction_with_MLflow.components.data_transformation import DataTransformation
from src.WineQualityPrediction_with_MLflow import logger
from pathlib import Path



STAGE_NAME = 'Data Transformation Stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path('artifacts//data_validation//status.txt'), 'r') as f:
                status = f.read().split(" ")[-1]

            # Here we are only starting the data_transformation_pipeline only if the status is true from our status.txt file

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config = data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("Your dat schema is not valid")
            
        except Exception as e:
            print(e)


if __name__ == '__main__':
     try:
        logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<<")

     except Exception as e:
        logger.exception(e)
        raise e