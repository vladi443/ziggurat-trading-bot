import yfinance as yf
from datetime import datetime

def calculate_historical_trends():

	print("allowed time frames: ")
	print("1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo, 1y, 2y, max")
	input_period=input("enter data period: ")
	input_interval=input("enter period interval: ")
	
	stock_history=stock_ticker_dict.history(period=input_period, interval=input_interval).to_dict()
	
	stock_close_entry=0
	stock_close_sum=0
	stock_times_up=0
	stock_times_down=-1
	stock_low=2560000000
	stock_high=0

	for key in stock_history:
		for sub_key in stock_history[key]:
			if key=="Close":
				stock_close_sum+=stock_history[key][sub_key]
				stock_close_entry+=1
				if stock_history[key][sub_key]>stock_high:
					stock_high=stock_history[key][sub_key]
					stock_times_up+=1
				if stock_history[key][sub_key]<stock_low:
					stock_low=stock_history[key][sub_key]
					stock_times_down+=1
			else:
				continue
				
	current_time=datetime.now()
	current_time_formatted=current_time.strftime("%d/%m/%Y %H:%M:%S")

	print("\n[REPORT GENERATED "+current_time_formatted+"]")
	print("-------")
	print("trends for data in the last "+input_period.upper()+" in intervals of "+input_interval.upper()+": ")
	print("\tLOW: "+str(stock_low))
	print("\tHIGH: "+str(stock_high))
	print("\tNEGATIVE TURNS: "+str(stock_times_down))
	print("\tPOSITIVE TURNS: "+str(stock_times_up))
	print("\tCURRENT: "+str(stock_ticker["currentPrice"]))
	print("-------")
	print("external stock data: ")
	print("\tTARGET PRICE HIGH: "+str(stock_ticker["targetHighPrice"]))
	print("\tTARGET PRICE LOW: "+str(stock_ticker["targetLowPrice"]))
	print("\tSTOCK RECOMMENDATION: "+str(stock_ticker["recommendationKey"]))
	print("-------")
	
def live_data_tracking():

	initial_price=stock_ticker["currentPrice"]
	live_price=initial_price
	
	print("Tracking Stock Information: ")
	print("\tSYMBOL: "+stock_symbol)
	print("\tINITIAL PRICE: "+str(stock_ticker["currentPrice"])+"\n")
	print("Tracking ...")
	
	while True:
		if stock_ticker["currentPrice"]!=initial_price:
			print("[WARNING] Price Change Detected: "+str(initial_price-stock_ticker["currentPrice"]))
			
			live_price=stock_ticker["currentPrice"]
			
			print("[] Overall Price Change: "+str(initial_price-live_price))
			print("[] Current Price: "+stock_ticker["currentPrice"])
	
def additional_information():
	print("\n"+str(sorted(stock_ticker.keys()))+"\n")
	
stock_symbol=input("enter stock symbol: ")
stock_symbol=stock_symbol.upper()
stock_ticker_dict=yf.Ticker(stock_symbol)
stock_ticker=yf.Ticker(stock_symbol).info

current_time=datetime.now()
current_time_formatted=current_time.strftime("%d/%m/%Y %H:%M:%S")

print("[ZIGGURAT SYSTEMS TRADING BOT]")
print("["+current_time_formatted+"]")
print("[  MENU  ]")
print("1. Historical Data Analysis")
print("2. Live Data Tracking and Analysis")
print("3. Additional Information and Documentation")
print("4. Exit")
user_input=int(input("[]: "))

if user_input==1:
	calculate_historical_trends()
elif user_input==2:
	live_data_tracking()
elif user_input==3:
	additional_information()
elif user_input==4:
	print("Cleaning up ... ")
else:
	print("[ERROR] Invalid Input")