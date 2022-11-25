##High Order Function
-----
#####**Concepto:**
    Funcion que llama otra funcion, los mas usados son:
        Filter
        Map
        Reduce


#####**Filter:**
    my_list = [1,4,5,6,9,13,19,21]
    
    odd = list(filter(lambda x: x%2 != 0, my_list))

    print (odd)

    result [1,5,9,13,19,21]

#####**Map:**
    my_list = [1,2,3,4,5]
    
    squares = list(map(lambda x: x**2, my_list))

    print (squares)

    result [1,5,9,13,19,21]

#####**Reduce:**
    from functools import reduce

    my_list = [2,2,2,2,2]
    
    all_multiplied = reduce(lambda a, b: a * b, my_list)

    print (all_multiplied)

    result 32