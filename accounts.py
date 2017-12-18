"""
@developer: Harikrishnan Lakshmanan
@date: 17 Dec 17
"""

import numpy as np

class Receipt(object):
    def __init__(self, store, split_mode=1):
        """
        :param store: String indicating name of the store
        :param split_mode: There are two modes as of now namely,
        1 -> Self (Taken care of by the Account Owner)
        2 -> Split among friends (Takes the friends as input in a single string split by '(colon)')
        """
        self.__store = store
        self.__users = ['Hari']
        self.__split_mode = self.split_factory(split_mode)
        self.__split_among = len(self.__users)

    def get_users(self):
        return raw_input("Please give me the list of users excluding the owner in this format 'Kiran:Vishnu' : ")

    def return_users(self):
        return self.__users

    def split_factory(self, split_mode):
        """
        Ideally much more fancy stuff would be included as other modes. I don't have any foresight on what they are.
        Just a facility to include if in case anything pops up.
        :param split_mode:
        :return:
        """
        if split_mode == 2:
            users = self.get_users().split(':')
            for user in users:
                if user is not '':
                    self.__users.append(user)

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
                RuntimeWarning('Filename is not in string')
                return str(filename)
        else:
            RuntimeError('Filename is None.')

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

    def add_receipt(self, store):
        print 'Adding a receipt from ' + store + " ..."
        receipt = Receipt(store, 2)
        print receipt.return_users()
        return receipt


if __name__ == "__main__":
    myAccount = Account('database/HL.npy')
    myAccount.read_database()
    myAccount.add_receipt("Luckys")