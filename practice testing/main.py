def add_5(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Please Enter Number'
    except ValueError as err:
        return err
    except TypeError as err:
        return err
