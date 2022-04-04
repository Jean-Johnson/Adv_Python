import time

def time_tracker(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        fuc_return_val = function(*args,**kwargs)
        end = time.time()
        function_name = function.__name__
        print(f"{function_name}: start -> {start}: end -> {end}: total execution time -> {end-start}")
        return fuc_return_val
    return wrapper

@time_tracker
def long_function(x):
    for i in range(x):
        continue # just to imitate tasks
    return f"Loop completed"

if __name__=="__main__":
    print(long_function(10000000))