# WineQualityPrediction_with_MLflow

## Workflow

1. update config.yaml
2. update schema.yaml
<!-- schema is a file where we mention all the columns in our data w.r.t datatypes -->
3. update params.yaml
<!-- params consists of all the model parameter like alpha value incase of elastic net
instead of chaning the parameters in run time we change in param.yaml file -->
4. update the entity
<!-- entity file consists information of return type of the functions -->
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/augustin7766/WineQualityPrediction_with_MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=augustin7766 \
MLFLOW_TRACKING_PASSWORD=8a01ee4bec043666cf3ced22edc7d308526b4b42 \
python script.py

Run this to export as env variables:

```bash

# The below are the tracking URL's
# For windows OS use 'set' instead of 'export'
# performing the below commands in the terminal doesn't work instead we use package as shown in '05_model_evaluation.ipynb'

export MLFLOW_TRACKING_URI=https://dagshub.com/augustin7766/WineQualityPrediction_with_MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=augustin7766

export MLFLOW_TRACKING_PASSWORD=8a01ee4bec043666cf3ced22edc7d308526b4b42

```