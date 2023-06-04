# ModernDataAnalyticsProject


## INTRODUCTION 
The Oude Markt in Leuven is known as the center of nightlife, with a high concentration of bars and clubs. People often want to know the crowdedness of the area in advance to plan their visit. To address this need, we developed a proof of concept solution to forecast the crowdedness of the Oude Markt based on real-time noise and weather information. Our model predicts street noise levels 6 hours into the future, as crowdedness is assumed to correlate with street noise.

This Git repository contains the notebooks required for data preprocessing in a parallelized fashion (Final_optimization.ipynb), data exploration (EDA.ipynb), and building the prediction model (MDA_models_notebook.ipynb). The repository is connected to a separate application repository written in Plotly Dash. The application visualizes the model's predictions for a 24-hour period and categorizes them as either 'Calmer than usual' or 'Busier than usual.'  Please visit https://github.com/linaske/ModernDataAnalyticsProjectApp/tree/master for the application repository.

## PREREQUISITES 
There are two ways to run the provided code:

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
3. To get the image run: `docker run -p 8888:8888 ivanaosredek/mda_noise_predict`
4. To get the image running and mount the data directory run: `docker run -p 8888:8888 -v /path/to/data/directory:/docker_project/data  ivanaosredek/mda_noise_predict`
5. To get the Jupyter Notebook running: `jupyter lab --no-browser --ip 0.0.0.0 --allow-root`
6. To optimize the runtime, we have shared intermediate files from the entire pipeline for your convenience. You can access these files by downloading them from https://drive.google.com/drive/folders/1ujkE1BN7HhospF830oSXqnLcnlWRoSJs?usp=drive_link. In your code, you can read these files at the specified points, allowing you to bypass computationally intensive steps. To utilize the files, you should download them and mount the directory when initializing your container.

## INPUT FILES
Data needed to start running the individual notebooks is the zipped .csv files containing the noise data and weather data dowloaded from https://rdr.kuleuven.be/dataset.xhtml?persistentId=doi:10.48804/SSRN3F . Weather data files used in the project are following: LC_2022Q1.csv, LC_2022Q2.csv,LC_2022Q3.csv and LC_2022Q4.csv. 

## NOTEBOOKS DESCRIPTION

### Final_optimization.ipynb Notebook

The Final_optimization notebook includes the following steps for data preprocessing: downloading noise and weather data using Dask, converting file formats, sampling noise data into 10 minute intervals to match weather data, adding time-related features, one hot encoding categorical variables, aligning timestamps with local CET timezone, and merging noise and weather data into one dataframe.

### EDA.ipynb Notebook

The data exploration notebook includes the following components: loading the dataset from the data loading notebook, examining missing data, creating a profile for exploratory data analysis (EDA), visualizing the average daily noise level in a week for each month and location, and displaying the average hourly noise level in a week for each location throughout the entire year.

### MDA_models_notebook.ipynb

The model evaluation and selection notebook comprises the following sections: loading the dataset configured in the data loading notebook, performing an 80-20 split for training and evaluation data, creating a feature matrix and target vector, constructing model pipelines for Ridge, HistGradientBoostingRegressor, and XGBoost algorithms, integrating the model pipelines into a model evaluation and selection pipeline, generating and plotting feature importances (Shapley) for the best model, evaluating the model on unseen data, visualizing predictions for the unseen data, creating intermediate data, and generating sample data for a dashboard application.

If you are running this notebook outside the Docker container, please be aware that it might encounter issues. The shap package relies on numpy 1.23.4, as it utilizes the deprecated np.int() function that is not available in newer numpy versions. 

