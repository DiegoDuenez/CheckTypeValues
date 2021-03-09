

def isInt(val, warning = True):
    if type(val) == int:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a Int * * * " % (val))
            return False
        else:
            return False

def isFloat(val, warning = True):
    if type(val) == float:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a Float * * * " % (val))
            return False
        else:
            return False

def isString(val, warning = True):
    if type(val) ==  str:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a String * * * " % (val))
            return False
        else:
            return False

def isNumericBool(val, warning = True):
    if type(val) == int and val == 1 or val == 0:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a Numeric Boolean * * * " % (val))
            return False
        else:
            return False

def isBool(val, warning = True):
    if type(val) == bool:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a Boolean * * * " % (val))
            return False
        else:
            return False

def isList(val, warning = True):
    if type(val) == list:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a List * * * " % (val))
            return False
        else:
            return False

def isTuple(val, warning = True):
    if type(val) == tuple:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a Tuple * * * " % (val))
            return False
        else:
            return False

def isDict(val, warning = True):
    if type(val) == dict:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a Dictionary * * * " % (val))
            return False
        else:
            return False

def isComplex(val, warning = True):
    if type(val) == complex:
        return True
    else:
        if warning == True:
            print(" * * * The value %s is not a Complex * * * " % (val))
            return False
        else:
            return False


    

