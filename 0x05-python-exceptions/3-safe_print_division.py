#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
        return (div)
    except (ZeroDivisionError):
        return (None)
    except:
        pass
    finally:
       print("Inside result: {}".format(div))
