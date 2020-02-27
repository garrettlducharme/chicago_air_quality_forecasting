def get_data_by_county(email, key, param, bdate, edate, state, county):
    """
    Obtains data from the AQS api for a given parameter at the provided monitoring site.
    Dates must be in the same year, and in the format YYYYmmdd.
    A maximum of 5 parameters can be provided.
    
    """
    url_head = 'https://aqs.epa.gov/data/api/sampleData/byCounty?'
    url = url_head + '&'.join(['email='+email, 'key='+key, 'param='+param, 
                               'bdate='+bdate, 'edate='+edate, 'state='+state, 
                               'county='+county])
    resp = requests.get(url)
    
    return resp

def get_data_by_site(email, key, param, bdate, edate, state, county, site):
    """
    Obtains data from the AQS api for a given parameter at the provided monitoring site.
    Dates must be in the same year, and in the format YYYYmmdd.
    A maximum of 5 parameters can be provided.
    
    """
    url_head = 'https://aqs.epa.gov/data/api/sampleData/bySite?'
    url = url_head + '&'.join(['email='+email, 'key='+key, 'param='+param, 
                               'bdate='+bdate, 'edate='+edate, 'state='+state, 
                               'county='+county, 'site='+site])
    resp = requests.get(url)
    
    return resp