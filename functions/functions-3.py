# function with multiple parameters
def multi_args(*args):
    print(args)


multi_args()
multi_args(1)
multi_args(1, 2)
multi_args(1, 2, 3)


# function with multiple keyword parameters
def multi_keyword_args(**kwargs):
    print(kwargs)


multi_keyword_args()
multi_keyword_args(x=1)
multi_keyword_args(y=2, z=5)
multi_keyword_args(x=1, y=10, z=12)


# function with both multi parameter and multi keyword argument
def multi_pos_keyword_args(*args, **kwargs):
    print(args, kwargs)


multi_pos_keyword_args()
multi_pos_keyword_args(1, 2, 3)
multi_pos_keyword_args(1, 2)
multi_pos_keyword_args(1, x=1, y=3, z=10)
multi_pos_keyword_args(x=1, y=7, z=8)


def list_parameters(x, y=[]):
    y.append(x)
    print(f"id(x) is {id(x)}, id(y) is  {id(y)}")
    print(y)


list_parameters(1)
list_parameters(2)
list_parameters(3, [])
list_parameters(4)
x = 3
z = [1, 2, 3]
print(f"In main id(x) is {id(x)}, id(y) is  {id(z)}")
list_parameters(x, z)
list_parameters(3)

