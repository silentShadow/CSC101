'''\
Rev: 1
Author: silentshadow
Description: feed investment portfolio data into pandas
Reference: http://www.ibm.com/developerworks/cloud/library/cl-datascienceincloud/
'''

import pandas.io.data as web
import matplotlib.pyplot as plt
from pandas import DataFrame


data_feed = {}
symbols = [ 'AAPL', 'FB', 'TSLA', 'GOOG' ]

for ticker in symbols:
    data_feed[ ticker] = web.get_data_yahoo( ticker, '03/1/2016','04/1/2016')
    
price = DataFrame( { tic: data[ 'Adj Close'] 
    for tic, data in data_feed.items() })
    
volume = DataFrame({ tic: data[ 'Volume']
    for tic, data in data_feed.items()})
    
returns = price.pct_change()

returns.sum().plot( kind='bar', title="% Return For Year")
plt.show()