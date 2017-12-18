class Receipt(object):
    def __init__(self, store, datetime, split_mode=1):
        """
        :param store: String indicating name of the store
        :param split_mode: There are two modes as of now namely,
        1 -> Self (Taken care of by the Account Owner)
        2 -> Split among friends (Takes the friends as input in a single string split by '(colon)')
        """
        self.__bill_database = {}
        self.__store = store
        self.__time = datetime
        self.__users = ['Hari']
        self.__split_mode = self.split_factory(split_mode)
        self.__split_among = len(self.__users)
        self.__split_strategy = [1.]
        self._stop = False

    def get_users(self):
        return raw_input("Please give me the list of users excluding the owner in this format 'Kiran:Vishnu' : ")

    def return_users(self):
        return self.__users

    def update_bill_database(self):
        for user in self.__users:
            self.__bill_database[user] = {}

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
        self.update_bill_database()

    def get_split_strategy(self):
        split_strategy = raw_input("Please give me the split strategy in decimals (should add up to 1), like (0.5:0.5) : ")
        split_strategy = split_strategy.split(':')
        for percentage in split_strategy:
            if percentage is not '':
                self.__split_strategy.append(float(percentage))

        if sum(self.__split_strategy) != 1.:
            print 'Should total to 1. Aborting ...'
            self.get_split_strategy()
        else:
            return

    def adjust_numbers(self):
        # TODO: If the sum in split strategy does not sum upto 1, it adjusts the numbers among everyone equally to sum it upto 1.
        pass

    def store_product_rates(self):
        # TODO: Store rate of item per lbs. Just for fun and review in future. Not good for anything other than that.
        pass

    def add_item(self, product, quantity, amount, split='equal'):
        if split != 'equal':
            self.get_split_strategy()
        else:
            self.__split_strategy = [1./self.__split_among]*self.__split_among
        self.adjust_numbers()
        self.store_product_rates()

        local_id = 0
        for user in self.__bill_database.keys():
            self.__bill_database[user][product] = amount*self.__split_strategy[local_id]
            local_id = local_id + 1

    def add_items(self):
        while(not self._stop):
            data = raw_input('Please give me the product, quantity in lbs, amount in $ (Product:Quantity:Amount): ')
            data = data.split(':', 3)
            if len(data) < 3:
                self._stop = True
                break
            else:
                product = data[0]
                quantity = float(data[1])
                amount = float(data[2])
                self.add_item(product, quantity, amount)

    def get_database(self):
        return self.__bill_database