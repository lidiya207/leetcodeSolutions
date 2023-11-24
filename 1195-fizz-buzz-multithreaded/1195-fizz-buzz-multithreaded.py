import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cv = threading.Condition()
        self.num = 1
        
    def workerFunc(self, shouldPrint: 'Callable[[int], bool]', printFunc: 'Callable[[], None]') -> None:
        with self.cv:
            while self.num <= self.n:
                if shouldPrint(self.num):
                    printFunc()
                    self.num += 1
                    self.cv.notify_all()
                else:
                    self.cv.wait()
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self.workerFunc(lambda x: x % 3 == 0 and x % 5 != 0, printFizz)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self.workerFunc(lambda x: x % 3 != 0 and x % 5 == 0, printBuzz)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self.workerFunc(lambda x: x % 3 == 0 and x % 5 == 0, printFizzBuzz)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        self.workerFunc(lambda x: x % 3 != 0 and x % 5 != 0, lambda: printNumber(self.num))