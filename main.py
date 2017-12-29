from accounts import Account

if __name__ == "__main__":
    myAccount = Account('database/HL.npy')
    myAccount.clear_database()
    myAccount.read_database()
    result = 'Y'
    while(result == 'Y' or result == 'y'):
	store = raw_input('Store: ')
	time = raw_input('Time: ')
	myAccount.add_receipt(store, time)
	save_bool = raw_input('Save(Y/n): ')
	if save_bool == 'y' or save_bool == 'Y':
	    myAccount.save_database()
	    myAccount.read_database()
	result = raw_input('Another bill? (Y/n): ')
    # myAccount.read_database()
    # print myAccount
    myAccount.return_total()
    # myAccount.clear_database()
    # myAccount.save_database()
