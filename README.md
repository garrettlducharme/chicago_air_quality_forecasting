# chicago_air_quality_forecasting
The goal of this project will be to use past meteorological and 
particulate matter (PM) data to forecast future PM levels in Chicago. 
While this is currently done using various analytical models, there are 
no machine learning models that are being use for predictions. Ideally, 
predictions will be done on the hourly level so that potential alerts 
may be sent out to warn citizens of days with poor air quality. 
Forecasting will be done with a long short-term memory recursive neural 
network (LSTM RNN). The data will be obtained from the Environmental 
Protection Agency (EPA) Air Quality Service (AQS) API. This API contains 
fine-coarsed measurements of a variety of different air pollutants at 
monitoring sites all across the U.S. I've also obtained some data from 
the S.H Bell monitoring center in Chicago, which does not appear to be 
in the AQS API. A first step will be to forecast a given monitoring 
site's future measurements using only the past local meteorological and 
PM information. However, I suspect that the meteorological conditions of 
the surrounding sites may also play an important role in forecasting, so 
I will try to include them after first building a rudimentary model.

## To Do

-- Rudimentary LSTM RNN forecasting model for the S.H Bell Chicago 
monitoring site.

-- Use the AQS API to pull all relevant hourly data from the past three 
or so years from each monitoring site in Cook county.

-- Look at the pre-generated hourly csv files on the EPA air data page 
to see if there's anything that's useful for this project.
if there's an
