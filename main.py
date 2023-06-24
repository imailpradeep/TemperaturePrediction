
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load the training data with temperatures from 1-1-2016 to 1-1-2023
df = pd.read_excel('temperature.xlsx', parse_dates=['ds'])
'''
# verification of dataframe df
print(df.head())
print(type(df['ds']))
print(df.dtypes)
'''
# Create a Prophet model
model = Prophet()

# Fit the model to the training data
model.fit(df)

# Create a future dataframe for 180 days till 30-6-2023 starting from 1-1-2016
future = model.make_future_dataframe(periods=180)

# Predict the future temperature
forecast = model.predict(future)

# Save the future dataframe to csv file
forecast.to_csv('PredictOutput.csv')

# Print or plot the forecast
#print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
#print(forecast.count(axis=0))
fig1 = model.plot(forecast)
plt.show()

# Read the meteorological data
True_temperature = pd.read_excel('TrueTemperature.xlsx', parse_dates=['date'])

# copy only predicted tail part of forecast dataframe to output so as to compare it later with the meteorological data
output = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(181)

'''
print(output)
print(output.count(axis=0))
print(True_temperature)
print(True_temperature.count(axis=0))
'''

# Plot the dataframe
plt.plot(output['ds'], output['yhat'], label='Predicted Temperature')
plt.plot(True_temperature['date'], True_temperature['tavg'], label='Recorded Temperature')
plt.plot(output['ds'], output['yhat_lower'], label='Predicted Low')
plt.plot(output['ds'], output['yhat_upper'], label='Predicted High')
plt.legend(loc="upper left")
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.show()
