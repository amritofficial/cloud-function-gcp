DESCRIPTION='description'
PRICE='price'
UPC='upc'

class Validate(object):   


    def filter_valid(self, data):
        """
        The following method filters the valid data 
        and removes the invalid data
        the method could be consolidated along with valid and invalid for 
        efficiency 
        See the bottom of the file
        :param data: data to be processed
        :return: valid data
        """

        valid = {}
        for key in data.keys():
            valid[key] = []
            for value in data[key]:
                valid_flag = self.validate_data(value)
                if valid_flag:
                    valid[key].append(value)
        
        return valid


    def filter_invalid(self, data):
        """
        The following method filters the invalid data 
        and removes the valid data
        the method could be consolidated along with valid and invalid for 
        efficiency 
        See the bottom of the file
        :param data: data to be processed
        :return: invalid data 
        """

        invalid = {}
        for key in data.keys():
            invalid[key] = []
            for value in data[key]:
                valid_flag = self.validate_data(value)
                if not valid_flag:
                    invalid[key].append(value)

        return invalid


    def filter_data(self, data):
        """
        The following method is not being used but is much more efficient 
        than the above method as it allows filtering of both type of 
        data at the same time and prevents rerunning of loops
        See the bottom of the file
        :param data: data to be processed
        :return: 
        """

        invalid = {}
        valid = {}
        for key in data.keys():
            invalid[key] = []
            valid[key] = []
            for value in data[key]:
                valid_flag = self.validate_data(value)
                if not valid_flag:
                    invalid[key].append(value)
                else:
                    valid[key].append(value)
    

    def validate_data(self, value):
        """
        The following method takes in each row and processess it 
        and returns a flag of validity 
        :param data: object
        :return: True or False on object being valid/invalid
        """

        valid_desc = self.__validate_description(value)
        valid_price = self.__validate_price(value)
        valid_upc = self.__validate_upc(value)

        if not valid_desc or not valid_price or not valid_upc:
            return False
    
        return True


    def __validate_description(self, value):
        """
        A private method to validate description field in the object
        :param value: object in a dict
        :return: Boolean True/False
        """

        if DESCRIPTION in value:
            return True
            
        return False


    def __validate_price(self, value):
        """
        A private method to validate price field in the object
        :param value: object in a dict
        :return: Boolean True/False
        """

        try:
            if float(value[PRICE]) or value[PRICE] is None:
                return True
        except:
            return False

    
    def __validate_upc(self, value):
        """
        A private method to validate upc field in the object
        :param value: object in a dict
        :return: Boolean True/False
        """

        if value[UPC].isdigit() and len(str(value[UPC])) == 12:
            return True

        return False
        