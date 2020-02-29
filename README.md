# chicago_air_quality_forecasting

### Problem Motivation

The southeast side of Chicago has been burdened with [poor air quality](https://www.epa.gov/il/environmental-issues-southeast-chicago) for a number of years. After numerous complaints from the residents, the EPA investigated this area in 2013 and found that many manufacturing and handling companies were not in compliance with the clean air act. In 2017, the company S.H. Bell was required to install a monitoring site so that pollution levels could be measured over time. This pollution is measured as concentrations of particulate matter of less than 10 micrometers in diameter ($PM_{10}$). The particulate matter coming from this site is primarily made up of manganese, but also contains lead as well as other heavy metals and dusts. Both prolonged and acute exposure to manganese have been associated with [significant health risks](https://www.ncbi.nlm.nih.gov/books/NBK158868/). This area of Chicago faces significant socioeconomic problems, meaning that health problems from exposure to polluted air are more likely to go undiagnosed. The goal of this project will therefore be to forecast the $PM_{10}$ concentrations from this site in order to alert residents when levels are particularly bad. Because the stakes are so high, the solution must be highly accurate as well as timely.

#### Approaches to a Solution

At the end of the day, this all boils down to a multivariate time series forecasting problem. The primary question is: how far in advance do we want to be able to forecast? In an ideal world, 12-24 hours in advance would be great as it would leave a lot of time to warn residents. We also want to be able to update this model on an hourly basis. Because accuracy is so important, I'll be attempting to use recursive neural networks (RNNs) for forecasting. Long short-term memory (LSTM) models seem to be the default choice for this type of forecasting, but they have significant computational overhead. I plan on trying them out, but I instead want to focus on gated recurrent units (GRUs) because they're (1) much faster and (2) can seemingly provide similar levels of accuracy. If this is truly the case, GRUs seems like they would be much more suitable for a productionized model. 

#### Challenges

The raw data provided on the EPA website isn't the greatest in terms of quality. There are a fair amount of missing values, which can make time series forecasting difficult. There is also no standard way that missing values are encoded, so they were quite difficult to identify at times. A significant amount of time was spent working with the data and getting it into a usable format for modelling.

The outliers in this data also proved to be a significant challenge. We cannot simply throw them away in this problem due to the nature of the health problems that can be associated with very high manganese concentrations. I was expecting the GRU RNNs to be able to handle these, but it doesn't seem like we can predict them very well at the moment. An alternative formulation of this problem may be to instead label outliers and to then see how well we're able to classify them. I am currently entertaining this thought as a side project.


### Data Source

The raw data is publicly available on the EPA website: https://www.epa.gov/il/sh-bell-chicago-air-monitoring-data.

### Directory Tree

- data
 - aqi_api - Raw data obtained from the AQS API
 - sh_bell - Raw and cleaned/combined data from the S.H. Bell monitoring site
- models - hdf5 files for GRU and LSTM forecasting models
- notebooks - Notebooks used to do the majority of the work
 - data_cleaning.ipynb - Cleaning and combining S.H. Bell data
 - data_scraping.ipynb - Framework for scraping data from the EPA website
 - epa_aqs_api_calls.ipynb - API calls to the EPA AQS database (in progress)
 - gru_test.ipynb - GRU modelling
 - lstm_test.ipynb - LSTM modelling
 - visuals.ipynb - Data visualization and creation of figures for presentation
- presentation_figures - Figures used in my capstone project presentation
- non_technical_presentation.pptx - Capstone presentation powerpoint
- pm_modeler.py - Particulate matter forecasting class (in progress)
- README.md - This readme file

