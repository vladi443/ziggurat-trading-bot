import yfinance as yf
import data_scanner as scanner
import user_commands as commands
import time
import global_vars as var

from datetime import datetime

def main():

	current_time=datetime.now()
	current_time_formatted=current_time.strftime("%d/%m/%Y %H:%M:%S")
	
	print("\n[ZIGGURAT SYSTEMS TRADING BOT]")
	print("["+current_time_formatted+"]")
	print("Type ?help for list of commands.")
	
	while var.active:
		user_input=input("> ")
		commands.check_user_input(user_input)
		
main()