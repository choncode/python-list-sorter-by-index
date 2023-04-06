"""To write a function that organises files into directories by file type."""

def list_sorter(arg, num):
    """This function will check for existing directory for the defined name and if exists,
    will continue the function or create a new directory. The files will then be categorised by the extensions
    defined in directories.

    Args:
        arg:
            A list or nested list.
        num:
            A number to represent index to sort by.
    Returns:
        A list or nested list, sorted alphabetically by the index given in second argument.
    """

    if isinstance(arg[0], list) == False:
        arg.sort(key=lambda x: x[num])
    else:
        print('this is a nested list')
        for lists in arg:
            lists.sort(key=lambda x: x[num])
    print(arg)       
    return arg



