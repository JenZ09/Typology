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


# Test cases
test_cases_full = [
    {"serial": 1, "input": None, "expected": "NoneType:NoneType"},
    {"serial": 2, "input": "", "expected": "str:str-empty"},
    {"serial": 3, "input": "   ", "expected": "str:str-whitespace"},
    {"serial": 4, "input": "123", "expected": "str:int"}, #in str form
    {"serial": 5, "input": "-42", "expected": "str:int-negative"}, #in str form
    {"serial": 6, "input": "-3.14", "expected": "str:float-negative"}, #in str form
    {"serial": 7, "input": "3.14", "expected": "str:float"}, #in str form
    {"serial": 8, "input": "NaN", "expected": "str:str"}, #in str form
    {"serial": 9, "input": "Infinity", "expected": "str:str"}, #in str form
    {"serial": 10, "input": "None", "expected": "str:str"}, #in str form
    {"serial": 11, "input": "hello", "expected": "str:str"}, #in str form
    {"serial": 12, "input": "0", "expected": "str:int"}, #in str form
    {"serial": 13, "input": "0.0", "expected": "str:float"}, #in str form
    {"serial": 14, "input": "-0", "expected": "str:int-negative zero"}, #in str form
    {"serial": 15, "input": "-0.0", "expected": "str:float-negative zero"}, #in str form
    {"serial": 16, "input": float('nan'), "expected": "float:float-nan"},
    {"serial": 17, "input": float('inf'), "expected": "float:float-infinity"},
    {"serial": 18, "input": float('-inf'), "expected": "float:float-negative infinity"},
    {"serial": 19, "input": 123, "expected": "int:int"}, #is it str form or int
    {"serial": 20, "input": -42, "expected": "int:int-negative"}, #is it str form or int
    {"serial": 21, "input": -3.14, "expected": "float:float-negative"}, #is it str form or float
    {"serial": 22, "input": 3.14, "expected": "float:float"}, #is it str form or float
    {"serial": 23, "input": 123466778889990000056467457724556598764322233333222222222999999876543211098161514322345, "expected": "int:int"},
    {"serial": 24, "input": 123466778889990000056467457724556598764322233333222222222999999876543211098161514322345.0, "expected": "float:float"},
    {"serial": 25, "input": 2 +3j, "expected": "complex:complex"}, # complex |why not str:complex?
    {"serial": 26, "input": True, "expected": "bool:bool-True"},   # bool    |why not str:bool?
    {"serial": 27, "input": [1, 2, 3], "expected": "list:list-3"}, # list    |why not str:list-[list of number,str,list,,,]|3?
    {"serial": 28, "input": (1, 2, 3, 4), "expected": "tuple:tuple-4"}, # tuple |why not str:tuple-(tuple of ,,,)|4? same as above
    {"serial": 29, "input": {1, 2, 3}, "expected": "set:set-3"}, # set       |why not str:set-{set of number,str}|3? same as above
    {"serial": 30, "input": frozenset([1, 2, 3, 4]), "expected": "frozenset:frozenset-4"}, # frozenset |why not str:frozenset-{frozenset of ,,,}|4?
    {"serial": 31, "input": {"a": 1, "b": 2}, "expected": "dict:dict-2"}, # dict |why not str:dict-{str:num,num:str} |2
    {"serial": 32, "input": range(6), "expected": "range:range-6"}, # range  |why not str:range-6? 
    {"serial": 33, "input": b"hello", "expected": "bytes:bytes-5"}, # bytes |why not str:bytes-5?
    {"serial": 34, "input": bytearray(b"hello"), "expected": "bytearray:bytearray-5"}, # bytearray |why not str:bytearray-5?
    {"serial": 35, "input": memoryview(b"hello"), "expected": "memoryview:memoryview-5"}, # memoryview |why not str:memoryview-5?
    {"serial": 36, "input": 0, "expected": "int:int"}, #is it str form or int
    {"serial": 37, "input": 0.0, "expected": "float:float"}, #is it str form or float
    {"serial": 38, "input": -0, "expected": "int:int"}, #is it str form or int
    {"serial": 39, "input": -0.0, "expected": "float:float-negative zero"}, #is it str form or float
    {"serial": 40, "input": 0.1e-2, "expected": "float:float"},   #is it str form or float
    {"serial": 41, "input": "0.1e-2", "expected": "str:float"}, #in str form
    {"serial": 42, "input": -0.1e-1, "expected": "float:float-negative"}, #is it str form or float
    {"serial": 43, "input": "-0.1e-1", "expected": "str:float-negative"}, #in str form
    {"serial": 44, "input": 0.1e-16, "expected": "float:float"}, #is it str form or float
    {"serial": 45, "input": "0.1e-16", "expected": "str:float"}, #in str form
    {"serial": 46, "input": -0.1e-16, "expected": "float:float-negative"}, #is it str form or float
    {"serial": 47, "input": "-0.1e-16", "expected": "str:float-negative"}, #in str form
    #{"serial": 48, "input": 0.1-e16, "expected": "str"},  #input errors out
    #{"serial": 48, "input": float(0.1-e16), "expected": "str"}, #input errors out
    {"serial": 48, "input": "0.1-e16", "expected": "str:str"}, #in str form
    #{"serial": 49, "input": -0.1-e-16, "expected": "str"}, #input errors out
    {"serial": 49, "input": "-0.1-e-16", "expected": "str:str"}, #in str form
    #{"serial": 50, "input": 0.1e2.5, "expected": "str"}, #coma error compiling
    {"serial": 50, "input": "0.1e2.5", "expected": "str:str"}, #in str form
    #{"serial": 51, "input": 0.1e-2.5, "expected": "str"}, #coma error compiling
    {"serial": 51, "input": "0.1e-2.5", "expected": "str:str"}, #in str form
    #{"serial": 52, "input": -0.1e2.5, "expected": "str"}, #coma error compiling
    {"serial": 52, "input": "-0.1e2.5", "expected": "str:str"}, #in str form
    #{"serial": 53, "input": -0.1e-2.5, "expected": "str"}, #coma error compiling
    {"serial": 53, "input": "-0.1e-2.5", "expected": "str:str"}, #in str form
    {"serial": 54, "input": 0+1, "expected": "int:int"}, #evaluates to int
    {"serial": 55, "input": 0+1*10, "expected": "int:int"}, #evaluates to int without division
    {"serial": 56, "input": 0+1*10-1, "expected": "int:int"}, #evaluates to int without division
    {"serial": 57, "input": "0+1*10-1", "expected": "str:int"}, #evaluates to int without division
    {"serial": 58, "input": (10*12+9-6)/1, "expected": "float:float"}, #evaluates to float with division
    {"serial": 59, "input": "(10*12+9-6)/1", "expected": "str:int"}, #evaluates to float with division
    {"serial": 60, "input": 2**2, "expected": "int:int"}, #evaluates to int with exponent
    {"serial": 61, "input": "2**2", "expected": "str:int"}, #evaluates to int with exponent
    {"serial": 62, "input": 2**-2, "expected": "float:float"}, #evaluates to float with negative exponent
    {"serial": 63, "input": "2**-2", "expected": "str:float"}, #evaluates to float with negative exponent
    {"serial": 64, "input": 2**(1/2), "expected": "float:float"}, #evaluates to float with fractional exponent
    {"serial": 65, "input": "2**(1/2)", "expected": "str:float"}, #evaluates to str with fractional exponent
    {"serial": 66, "input": (10*12+9-6)/4, "expected": "float:float"}, #evaluates to float with division
    {"serial": 67, "input": "(10*12+9-6)/4", "expected": "str:float"}, #evaluates to float with division
]

test_cases_complex = [
    {"serial": 25, "input": -2 -3j, "expected": "complex"}, # complex
    {"serial": 25, "input": -2 +3j, "expected": "complex"}, # complex
    {"serial": 25, "input": 2 -3j, "expected": "complex"}, # complex
    {"serial": 25, "input": 2 +3j, "expected": "complex"}, # complex
    {"serial": 25, "input": -3j, "expected": "complex"}, # complex
    {"serial": 25, "input": +3j, "expected": "complex"}, # complex
    {"serial": 25, "input": -0 -1j, "expected": "complex"}, # complex
    {"serial": 25, "input": 0 -1j, "expected": "complex"}, # complex
    {"serial": 25, "input": -0 -0j, "expected": "complex"}, # complex
    {"serial": 25, "input": 0 +0j, "expected": "complex"}, # complex
    {"serial": 25, "input": -0j, "expected": "complex"}, # complex
    {"serial": 25, "input": +0j, "expected": "complex"}, # complex
    {"serial": 25, "input": 0j, "expected": "complex"}, # complex    
]


test_cases_random = [
    {"serial": 25, "input": -2 -3j, "expected": "complex"}, # complex
    {"serial": 25, "input": -2 +3j, "expected": "complex"}, # complex
    {"serial": 25, "input": 2 -3j, "expected": "complex"}, # complex
    {"serial": 25, "input": 2 +3j, "expected": "complex"}, # complex
]

def run_tests():
    #print(f"{'Serial':<8} {'Input':<12}")
    border=100
    print("="*border)
    print(f"{'Expected':<35} {'Actual':<35} {'Status':<10} {'Type':<10}")
    print("="*border)
    for case in test_cases_full:
    #for case in test_cases_complex:
    #for case in test_cases_random:
        actual = chk_input_form(case["input"])
        status = "Pass" if actual == case["expected"] else "Fail"
        print(f"{case['serial']} {'Input : ':<5} {str(case['input'])}")
        print(f"{case['expected']:<35} {actual:<35} {status:<10} {type(case['input']).__name__:<12}")
        print("="*border)

def main():
    while True:
        user_input = input("Input the string to check or Choose 't' to run predefined 'test' cases, or 'q' to 'quit' : ")
        #print(user_input)
        if user_input in ['q', 'quit']:
            print("Quiting.... Bye!")
            break
        elif user_input in ['t', 'test']:
            run_tests()
        else:
            result = chk_input_form(user_input)
            print(f"Input: '{user_input}' Classified as: {result}")


if __name__ == "__main__":
    main()


'''
# List of values covering all major Python built-in types
values = [
    42,  # int
    3.14,  # float
    2 + 3j,  # complex
    True,  # bool
    "hello",  # str
    None,  # NoneType
    [1, 2, 3],  # list
    (1, 2, 3),  # tuple
    range(5),  # range
    {1, 2, 3},  # set
    frozenset([1, 2, 3]),  # frozenset
    {"a": 1, "b": 2},  # dict
    b"hello",  # bytes
    bytearray(b"hello"),  # bytearray
    memoryview(b"hello")  # memoryview
]

# Loop through each value, assign it to variable s, and print both the value and its type
for value in values:
    s = value
    print(f"Value: {s}, Type: {type(s)}")

'''
