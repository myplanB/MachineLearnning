def TestPrint():
    name = "hello"
    age = "world"
    print "{0}-{1}".format(name, age)


def TestException():
    try:
        print "hello world!"
    except OSError:
        print "OS error {0}".format(OSError)

def add_candles(cake_func):
    def insert_candles():
        return cake_func() + " and Candles"
    return insert_candles()

@add_candles
def make_cake():
    return "cake"


if __name__ == "__main__":
    print (make_cake)
