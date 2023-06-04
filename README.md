# ModernDataAnalyticsProject


## INTRODUCTION 
The Oude Markt in Leuven is known as the center of nightlife, with a high concentration of bars and clubs. People often want to know the crowdedness of the area in advance to plan their visit. To address this need, we developed a proof of concept solution to forecast the crowdedness of the Oude Markt based on real-time noise and weather information. Our model predicts street noise levels 6 hours into the future, as crowdedness is assumed to correlate with street noise.

This Git repository contains the notebooks required for data preprocessing in a parallelized fashion (Final_optimization.ipynb), data exploration (EDA.ipynb), and building the prediction model (MDA_models_notebook.ipynb). The repository is connected to a separate application repository written in Plotly Dash. The application visualizes the model's predictions for a 24-hour period and categorizes them as either 'Calmer than usual' or 'Busier than usual.'  Please visit https://github.com/linaske/ModernDataAnalyticsProjectApp/tree/master for the application repository.

## PREREQUISITES 

1. Running notebooks individually: To successfully run the individual notebooks, ensure that the following packages are present in your environment:
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

2. Running with Docker: Docker can be used to run the code. Ensure that Docker is installed on your system. You can download Docker from https://www.docker.com/get-started. For detailed instructions, refer to the section below.


##  RUNNING DOCKER CONTAINER

1. To retrive the Docker container, please visit https://hub.docker.com/repositories/ivanaosredek. 
2. Pull the Docker image from Docker Hub using: `docker pull ivanaosredek/mda_noise_predict`
3. After the image is downloaded, you can run a container based on that image using: `docker run mda_noise_predict`
4. To optimize the runtime, we have shared intermediate files from the entire pipeline for your convenience. You can access these files by downloading them from https://drive.google.com/drive/folders/1ujkE1BN7HhospF830oSXqnLcnlWRoSJs?usp=drive_link. In your code, you can read these files at the specified points, allowing you to bypass computationally intensive steps. To utilize the files, you should download them and mount the directory when initializing your container.

## INPUT FILES
Data needed to start running the individual notebooks is the zipped .csv files containing the noise data and weather data dowloaded from https://rdr.kuleuven.be/dataset.xhtml?persistentId=doi:10.48804/SSRN3F . Weather data files used in the project are following: LC_2022Q1.csv, LC_2022Q2.csv,LC_2022Q3.csv and LC_2022Q4.csv. 

## NOTEBOOKS FORMAT

### Final_optimization.ipynb Notebook
### EDA.ipynb Notebook
### MDA_models_notebook.ipynb



