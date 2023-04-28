## MDA assignment: Time-related feature engineering using HistGradientBoostingRegressor (sklearn)
## applied to laeq data (per second) of La Filosofia, February 2022

#import packages
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.model_selection import cross_validate


#load data
df = pd.read_csv("E:\MDA 2023\Full noise data\Feb\csv_results_42_255443_mp-06-parkstraat-2-la-filosovia.csv",delimiter=';')

#drop id variables and other measures
df = df[['result_timestamp','laeq']]

# Convert the datetime column to a Pandas datetime object
df['result_timestamp'] = pd.to_datetime(df['result_timestamp'])

# Extract hour-in-the-day feature
df['hour'] = df['result_timestamp'].dt.hour.astype('int64')

# Extract day-in-the-week feature
df['weekday'] = df['result_timestamp'].dt.dayofweek.astype('int64')

# Extract day-in-the-month feature
df['day_of_month'] = df['result_timestamp'].dt.day.astype('int64')

# Extract month-in-the-year feature
df['month'] = df['result_timestamp'].dt.month.astype('int64')

#drop original datetime column
df = df.drop("result_timestamp", axis='columns')

#plot of noise over average week
fig, ax = plt.subplots(figsize=(12, 4))
average_week_noise = df.groupby(["weekday", "hour"])["laeq"].mean()
average_week_noise.plot(ax=ax)
_ = ax.set(
    title="Noise during the average week",
    xticks=[i * 24 for i in range(7)],
    xticklabels=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    xlabel="Time of the week",
    ylabel="Laeq",
)

fig.savefig("Noise_average_week_feb.png")

#convert noise to relative noise (or relative crowdedness)
y = df["laeq"] / df["laeq"].max()

X = df.drop("laeq", axis="columns")

#create time-sensitive split for cross-validation
ts_cv = TimeSeriesSplit(
    n_splits=5,
    gap=48,
    max_train_size=10000,
    test_size=1000,
)

#inspect splits
all_splits = list(ts_cv.split(X, y))
train_0, test_0 = all_splits[0]
X.iloc[test_0]
X.iloc[train_0]

train_4, test_4 = all_splits[4]
X.iloc[test_4]
X.iloc[train_4]

#run histogram gradient boosting model
def evaluate(model, X, y, cv):
    cv_results = cross_validate(
        model,
        X,
        y,
        cv=cv,
        scoring=["neg_mean_absolute_error", "neg_root_mean_squared_error"],
    )
    mae = -cv_results["test_neg_mean_absolute_error"]
    rmse = -cv_results["test_neg_root_mean_squared_error"]
    print(
        f"Mean Absolute Error:     {mae.mean():.3f} +/- {mae.std():.3f}\n"
        f"Root Mean Squared Error: {rmse.mean():.3f} +/- {rmse.std():.3f}"
    )

gbrt_pipeline = make_pipeline(HistGradientBoostingRegressor()).set_output(transform="pandas")

evaluate(gbrt_pipeline, X, y, cv=ts_cv)
