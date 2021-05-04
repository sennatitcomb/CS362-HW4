def volume(a):
   # if isinstance(a, str):
    #    return "Please only enter positive integers"
   # else:
        if (a > 0):
            return a*a*a
        else: 
            return "Please only enter a positive number"

def avg(a):
    #if not a:
     #   return "Please enter a list"
    #else:
        return sum(a) / len(a)

def name(first, last):
    #first = input("Enter a first name: ")
    #last = input("Enter a last name: ")
    return first + " " + last

