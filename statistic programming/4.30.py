#벡터 합

def vector_add(v, w):
    """adds two vectors componentwise"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]
vector_add([1,2], [3,4])

#벡터 차

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]
vector_subtract([0, 0, 1], [1, 2, 3])