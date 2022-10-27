import global_vars as var
import data_scanner as scanner

def check_user_input(user_input):
	user_input_list=user_input.split()
	match user_input_list[0].lower():
		case "?quit":
			var.active=False
		case "?help":
			list_commands()
		case "?list":
			stock_dict=scanner.get_user_data()
			if stock_dict!=int(0):
				print("ID : STOCK | QUANTITY | INITIAL PRICE")
				print("-------------------------------------")
				for key in stock_dict:
					print(str(key)+" : "+str(stock_dict[key]))
		case "?analyze":
			print("Error: function not yet implemented.")
		case "?track":
			if len(user_input_list)>1:
				if user_input_list[1].lower()=="all":
					stock_dict=scanner.get_user_data()
					stock_list=[]
					for key in stock_dict:
						stock_list.append(stock_dict[key][0].upper())
					scanner.live_track(stock_list)
				else:
					stock_list=[]
					for ind in range(1, len(user_input_list)):
						stock_list.append(user_input_list[ind])
					scanner.live_track(stock_list)
			else:
				print("Invalid parameters for command ?track")
		case "?updatedata":
			print("Error: function not yet implemented.")
		case "?earnings":
			print("Error: function not yet implemented.")
		case _:
			print("Error: Unknown command!")
			
def list_commands():
	print("?list \n\t- returns a list of current saved stock data")
	
	print("?analyze <SYMBOL/ALL> <TIME_PERIOD> <TIME_FRAME>")
	print("\t- analyzes past trends of selected stock in the given")
	print("\ttime period and time frame, acceptable parameters are:")
	print("\t1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo, 1y, 2y, max")
	
	print("?track <SYMBOL/ALL> \n\t- live tracks changes in price of selected stock.")
	
	print("?updatedata \n\t- allows you to modify the user data file.")
	
	print("?earnings \n\t- displays current net earnings based on current stock")
	print("\tprice and initial stock price and quality as declared in user data file.")
	
	print("?help \n\t-displays list of current available commands.")
	
	print("?quit \n\t-save data and quit the program.")
	
		