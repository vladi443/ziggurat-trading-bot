import yfinance as yf
import time
import json

from pathlib import Path
from datetime import datetime

def get_user_data():

	user_data_path=Path("user_data.json")
	
	if user_data_path.is_file():
		with open('user_data.json') as user_data_json:
			user_data = json.load(user_data_json)
		return user_data
		
	else:
		create_user_data()
		return 0
		
def create_user_data():

	print("User data file missing ... \nCreating new User data file ...\n")
	
	user_data_object=open("user_data.json", "w")
	user_data_object.close()
	stock_id=0
	stock_data={}
	
	print("Enter stock data below, type ?done when finished.")
		
	while True:
		stock_name=input("SYMBOL: ")
		if stock_name.lower()=="?done":
			break
			
		stock_quantity=input("QUANTITY: ")
		if stock_quantity.lower()=="?done":
			break
		
		stock_initial_value=input("INITIAL VALUE: ")
		if stock_initial_value.lower()=="?done":
			break
			
		stock_data[stock_id] = [stock_name, stock_quantity, stock_initial_value]
		stock_id+=1
	
	print("Saving user data ...")
	
	with open('user_data.json', 'w') as convert_user_data:
		convert_user_data.write(json.dumps(stock_data))
		
	print("User data saved!")
	
def live_track(list_stocks):
	print("Live Tracking Stocks Information:\n")
	print("STOCK : INITIAL PRICE")
	print("---------------------")
	
	stock_ticker_list=[]
	stock_current_price_list=[]
	
	for value in list_stocks:
		stock_ticker=yf.Ticker(value.upper()).info
		stock_ticker_list.append(stock_ticker)
		stock_current_price_list.append(int(stock_ticker["currentPrice"]))
		print(value+" : $"+str(stock_ticker["currentPrice"]))
		
	print("\nTracking Stocks ...\n")
	
	while True:
		current_time=time.perf_counter()
		while time.perf_counter()-current_time<0.5:
			pass
		
		for ticker_index in range(len(stock_ticker_list)):
			stock_ticker_list[ticker_index]=yf.Ticker(list_stocks[ticker_index].upper()).info
			if int(stock_current_price_list[ticker_index])!=int(stock_ticker_list[ticker_index]["currentPrice"]):
				print("WARNING: Price change detected for "+str(list_stocks[ticker_index])+" : ")
				print(str(stock_current_price_list[ticker_index]), str(stock_ticker_list[ticker_index]["currentPrice"]))
				print("\t"+str(stock_current_price_list[ticker_index]-stock_ticker_list[ticker_index]["currentPrice"]))
				print("\t"+str(stock_ticker_list[ticker_index]["currentPrice"]))
				stock_current_price_list[ticker_index]=stock_ticker_list[ticker_index]["currentPrice"]
			
		
			
		
		
		