# ModernDataAnalyticsProject


## INTRODUCTION 
The Oude Markt in Leuven has a high concentration of bars and clubs, making it the center of nightlife in Leuven. The crowdedness of the area is likely to impact people's decision to visit the Oude Markt. Ideally, people would like to know during the day whether it will be crowded at night, so they can plan accordingly.

In this project, we developed a proof of concept solution to forecast the crowdedness of the Oude Markt based on real-time noise and weather information. We assumed that crowdedness correlates with street noise, and since we had access to street noise and weather data in the proximity of Oude Markt, we created a model to forecast street noise levels 6 hours into the future.

This Git repository contains the notebooks required to preprocess the data in a parallelized fashion (Final_optimization.ipynb), explore the data (EDA.ipynb), and build a prediction model (MDA_models_notebook.ipynb). The repository is connected to a separate application repository written in Plotly Dash. The application is used to visualize the predictions of the model for a 24-hour period and summarize them in two possible states relative to the daily average: 'Calmer than usual' and 'Busier than usual'. Please visit https://github.com/linaske/ModernDataAnalyticsProjectApp/tree/master for the application repository.

## PREREQUISITES 

To successfully run the individual notebooks, please make sure that the following packages are present in your environment:

Python version 3.6.8
dask (2021.03.0)
ydata-profiling (3.1.0)
coiled (0.0.38)
matplotlib (3.3.4)
numba (0.57.0)
numpy (1.23.5)
pandas (1.1.5)
scikit-learn (1.2.2)
seaborn (0.11.2)
shap (0.41.0)
statsmodels (0.14.0)
tqdm (4.65.0)
xgboost (1.7.4)

To ensure the reproducibility of our code, we have encapsulated our entire data processing pipeline within a Docker container. You can retrieve the Docker container using the instructions provided in the section below.


##  RUNNING DOCKER CONTAINER

To optimize the runtime, we have shared intermediate files from the entire pipeline for your convenience. You can access these files by downloading them from https://drive.google.com/drive/folders/1ujkE1BN7HhospF830oSXqnLcnlWRoSJs?usp=drive_link. In your code, you can read these files at the specified points, allowing you to bypass computationally intensive steps. To utilize the files, you should download them and mount the directory when initializing your container.

## INPUT FILES
Data needed to start running the individual notebooks is the zipped .csv files containing the noise data and weather data dowloaded from https://rdr.kuleuven.be/dataset.xhtml?persistentId=doi:10.48804/SSRN3F . Weather data files used in the project are following: LC_2022Q1.csv, LC_2022Q2.csv,LC_2022Q3.csv and LC_2022Q4.csv. 

## NOTEBOOKS FORMAT

### Final_optimization.ipynb Notebook

### EDA.ipynb Notebook
### MDA_models_notebook.ipynb



