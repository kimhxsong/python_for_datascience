import math


def NULL_not_found(obj: any) -> int:
    matchedNULL = ""
    if isinstance(obj, object) and obj == None:
        matchedNULL = "Nothing"
    elif isinstance(obj, float) and math.isnan(obj):
        matchedNULL = "Cheese"
    elif isinstance(obj, int) and obj == 0:
        matchedNULL = "Zero"
    elif isinstance(obj, str) and obj == "":
        matchedNULL = "Empty"
    elif isinstance(obj, bool) and obj == False:
        matchedNULL = "Fake"
    else:
        matchedNULL = None

    if matchedNULL is None:
        print("Type not found")
        return 1
    else:
        print(f"{matchedNULL} : {obj} {type(obj)}")
        return 0
