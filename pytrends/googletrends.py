from pytrends.request import TrendReq


	
	

SearchList = ["Oracle", "MySQL", "SQL Server", "PostgreSQL", "MongoDB"]
pytrends = TrendReq()

# build the payload
pytrends.build_payload(SearchList, timeframe='today 5-y')
data  = pytrends.interest_by_region(resolution='COUNTRY')
print(data)
