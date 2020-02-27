# chicago_air_quality_forecasting

### Problem Motivation

The southeast side of Chicago has been burdened with [poor air quality](https://www.epa.gov/il/environmental-issues-southeast-chicago) for a number of years. After numerous complaints from the residents, the EPA investigated this area in 2013 and found that many manufacturing and handling companies were not in compliance with the clean air act. In 2017, the company S.H. Bell , a monitoring station has been installed so that air quality can be monitored
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
