from WineQualityPrediction.config.configuration import ConfigurationManager
from WineQualityPrediction.components.model_trainer import ModelTrainer
from WineQualityPrediction import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager ()
        model_trainer_config = config.get_model_tranier_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()