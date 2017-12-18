"""
@developer: Harikrishnan Lakshmanan
@date: 17 Dec 17
"""

import numpy as np
from receipts import Receipt

class Account(object):
    def __init__(self, filename):
        self.__filename = self.set_filename(filename)
        self.__database = None
        self.open_database()

    def set_filename(self, filename):
        if filename is not None:
            if type(filename) == str:
                return filename
            else:
                print 'Filename is not in string'
                return str(filename)
        else:
            raise RuntimeError('Filename is None.')

    def open_database(self):
        self.__database = np.load(self.__filename).item()

    def save_database(self):
        np.save(self.__filename, self.__database)

    def read_database(self):
        if self.__database is not None:
            print self.__database
        else:
            self.open_database()
            print self.__database

    def add_receipt(self, store, datetime):
        print 'Adding a receipt from ' + store + " ..."
        receipt = Receipt(store, datetime, 2)
        receipt.add_items()
        bill_database = receipt.get_database()
        bill_database['Store'] = store
        self.__database[datetime] = bill_database

    def get_total(self, user):
        return user.values()

    def return_total(self):
        print ''
        for key in self.__database.keys():
            print 'Store:', self.__database[key]['Store']
            print 'Time:', key
            for user in self.__database[key].keys():
                if user is not 'Store':
                    print user, ":", sum(self.get_total(self.__database[key][user]))


    def clear_database(self):
        self.__database = {}

    def __repr__(self):
        print ''
        for key in self.__database.keys():
            print 'Store:', self.__database[key]['Store']
            print 'Time:', key
            for user in self.__database[key].keys():
                if user is not 'Store':
                    print user
                    for product in self.__database[key][user].keys():
                        print '-', product, ':', self.__database[key][user][product]
        return ''

if __name__ == "__main__":
    myAccount = Account('database/HL.npy')
    myAccount.read_database()
    myAccount.add_receipt("Luckys", '10-Dec-2017, 10:30:00 PM')
    # myAccount.read_database()
    print myAccount
    myAccount.return_total()
    # myAccount.clear_database()
    # myAccount.save_database()