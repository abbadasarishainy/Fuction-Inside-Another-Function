def outer():
    def inner():
        print("inner function")
    print("outer function")
    inner()
outer()
