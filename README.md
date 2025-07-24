# Wine-Quality-Prediction

## Workflow
1. Update config.yaml : Instead of hardcoding values (like file paths, URLs, etc.) into your Python scripts, you define them here in config.yaml.

2. Update schema.yaml

3. Update params.yaml

4. Update the entity : This defines a typed, immutable config object (a blueprint) that your code will use to access configuration values in a clean and type-safe way.

5. Update the configuration manager in src config: The ConfigurationManager class acts as a central hub to:
Read configuration files (config.yaml, params.yaml, schema.yaml)
Create required directories
Return structured config objects (like DataIngestionConfig) to the pipeline

6. Update the components:  This is where your project actually downloads and prepares the raw data — a crucial first step in any ML workflow.
7. Update the pipeline
8. Update the main.py
9. Update the app.py