DESCRIPTION='description'
PRICE='price'
UPC='upc'

class Validate(object):   


    def validate_data(self, value):
            valid_desc = self.__validate_description(value)
            valid_price = self.__validate_price(value)
            valid_upc = self.__validate_upc(value)

            if not valid_desc or not valid_price or not valid_upc:
                return False
        
            return True


    def __validate_description(self, value):
        if DESCRIPTION in value:
            return True
            
        return False


    def __validate_price(self, value):
        try:
            if float(value[PRICE]) or value[PRICE] is None:
                return True
        except:
            return False

    
    def __validate_upc(self, value):
        if value[UPC].isdigit() and len(str(value[UPC])) == 12:
            return True

        return False