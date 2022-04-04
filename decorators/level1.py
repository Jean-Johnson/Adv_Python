from random import sample


def sample_decorator(function):

    def wrapper(*args, **kwargs):
        print("Inside sample decorator")
        return_val = function(*args,**kwargs)
        return return_val
    return wrapper


@sample_decorator
def sample_function(X):
    return f"sample parameter X -> {X}"
if __name__=="__main__":
    print(sample_function("jean"))