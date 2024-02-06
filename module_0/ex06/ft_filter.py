def ft_filter(funct, nbr):
    """ft_filter
        have same comportement of filter
        recived 2 param :
            1 - an function who return true / false
            2 - an list on numbers
        return value : all numbers who reply true when
       they are send on function
    """
    if funct:
        return (item for item in nbr if funct(item))
    return nbr
