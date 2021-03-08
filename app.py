from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/history/IDR/USD/T')
soup = BeautifulSoup(url_get.content,"html.parser")

table = soup.find('div', attrs={'class':'table-responsive'})
tr = tbody.find_all('tr')
temp = [] #initiating a tuple

for i in range(3,10):
    row = table.find_all('tr')[i]
    
    #get date
    date = row.find_all('td')[0].text
    date = date.strip() #for removing the excess whitespace
    
    #get day
    day = row.find_all('td')[1].text
    day = day.strip() #for removing the excess whitespace
    
    #get rate
    rate = row.find_all('td')[2].text
    rate = rate.strip() #for removing the excess whitespace
#insert the scrapping process here
    
    temp.append((date,day,rate))

temp = temp[::-1]

#change into dataframe
exchange = pd.DataFrame(temp, columns = ('date','day','rate'))

#insert data wrangling here
ca

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'USD {exchange["rate"].mean().round(2)}'

	# generate plot
	ax = card_data.plot(figsize = (20,9))
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]


	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)
