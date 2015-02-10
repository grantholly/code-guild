"""
This demonstrates the difference between the print and return in a function.
Print is used to send some data to the standard output.  This gets displayed,
or printed, to the user.  Return is different in that it sends some data to
the caller of the function.
"""

def print_function():
    # the string object will be sent to the stdout
    print("hello world")

"""
Here we are trying to assign the value of d to the object returned by the
function call of print_function.  Because print_function sends its data to
the stdout, the variable will not be able to bind to the string "hello world"
"""
d = print_function()

# d doesn't reference anything
print(d)

"""
The return_function returns the string object to the caller of return_function.
In this case, the caller of the function is the assignment of the variable d.
Because the function returns its data to the caller, the assignment to the
variable d works correctly.
"""
def return_function():
    return "hello world"

# d now references the string object returned by the function call
d = return_function()

print(d)
