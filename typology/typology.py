#Check the type and form of the provided string
def chk_input_form(s):
    n=s
    if not isinstance(s, str):
        #print("not str")
        if s is None:
            #print("is None")
            return type(s).__name__+":"+"NoneType"  #"Invalid number"
        elif isinstance(s, float):
            #print("is float")
            if s != s:
                # NaN is the only value in Python that is not equal to itself
                return type(s).__name__+":"+"float"+"-"+"nan" #"Invalid number"
            elif s == float('inf'):
                return type(s).__name__+":"+"float"+"-"+"infinity" #"Invalid number word"
            elif s == float('-inf'):
                return type(s).__name__+":"+"float"+"-"+"negative infinity" #"Invalid number word"
            else:
                s=str(s)
        elif isinstance(s, bool):
            #print("is bool")
            return type(s).__name__+":"+"bool"+"-"+str(s) #"Invalid number"
        elif isinstance(s, int):
            #print("is int")
            s=str(s)
        elif isinstance(s, complex):
            #print("is complex")
            neg = ""
            if s.real < 0:
                neg += "real"
            if s.imag < 0:
                neg += ",imag" if neg else "imag"
            #print(type(s).__name__+":"+"complex"+("-negative "+neg if neg else ""))
            return type(s).__name__+":"+"complex"+("-negative "+neg if neg else "") #"Invalid number word"                  
        else:
            #print("anything other than str, none, float, bool, int, complex  - could be list, set, dict, range etc..")
            #print(type(s).__name__+":"+type(s).__name__+"-"+str(len(s)))
            return type(s).__name__+":"+type(s).__name__+"-"+str(len(s)) #"Invalid number"  
    else:
        #print("is str")
        if s.isspace():
            return type(s).__name__+":"+"str-whitespace" #Invalid"
        if s.strip() == "":
            return type(s).__name__+":"+"str-empty" #"Invalid"
        if s.lower() in ['none','nan','infinity','inf','-infinity','-inf']:
            return type(s).__name__+":"+"str" #"Invalid" can or cannot this be removed from here ? Will the below num=float(s)
                                                    #convert them into valid float and execute the before except or fail and execute post except
        

    try:
        num = float(eval(s))
        if '^' in s:
            return type(n).__name__+":"+"float"+"-"+"bitwise XOR" #"Invalid number"
        sign = ""
        num_type=""
        if ('.' in s or 'e' in s) or (num-int(num)>0):
            num_type="float"
        else:
            num_type="int"
        if num<0:
            sign="-negative"
        # In case of negative zero
        elif num==0 and '-' in s:
            sign="-negative zero" #"Invalid"
        return type(n).__name__+":"+num_type+sign 

    except:                             # ValueError: do we need to be specific with the errors
        print("except block")
        return type(n).__name__+":"+type(s).__name__
