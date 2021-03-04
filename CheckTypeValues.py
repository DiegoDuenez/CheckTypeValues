
class CheckTypeValues:

    def isInt(self, val):
        if type(val) == int:
            return True
        else:
            print(" * * * The value %s is not a Int * * * " % (val))
            return False
    
    def isFloat(self, val):
        if type(val) == float:
            return True
        else:
            print(" * * *The value %s is not a Float * * * " % (val))
            return False
    
    def isString(self, val):
        if type(val) ==  str:
            return True
        else:
            print(" * * * The value %s is not a String * * * " % (val))
            return False
    
    def isNumericBool(self, val):
        if type(val) == int and val == 1 or val == 0:
            return True
        else:
            print(" * * * The value %s is not a Numeric Boolean * * * " % (val))
            return False
    
    def isBool(self, val):
        if type(val) == bool:
            return True
        else:
            print(" * * * The value %s is not a Boolean * * * " % (val))
            return False

    




