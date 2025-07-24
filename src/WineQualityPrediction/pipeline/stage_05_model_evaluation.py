from WineQualityPrediction.config.configuration import ConfigurationManager
from WineQualityPrediction.components.model_evaluation import ModelEvaluation
from WineQualityPrediction import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
         config = ConfigurationManager()
         model_evaluation_config = config.get_model_evaluation_config()
         model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
         model_evaluation_config.save_results()