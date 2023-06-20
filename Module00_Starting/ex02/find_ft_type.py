def all_thing_is_obj(obj: any) -> int:
    foundType = False

    if isinstance(obj, list):
        foundType = "List"
    elif isinstance(obj, tuple):
        foundType = "Tuple"
    elif isinstance(obj, set):
        foundType = "Set"
    elif isinstance(obj, dict):
        foundType = "Dict"
    elif isinstance(obj, str):
        foundType = f"{obj} is in the kitchen"
    else:
        foundType = None

    if foundType is None:
        print("Type not found")
    else:
        print(f"{foundType} : {type(obj)}")

    return 42

# Expected:
# $>python tester.py | cat -e
# List : <class 'list'>$
# Tuple : <class'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Type not found$
# 42$
# $>
