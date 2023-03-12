class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                self.fizzbuzz(self.printFizzBuzz)
            elif num % 3 == 0:
                self.fizz(self.printFizz)
            elif num % 5 == 0:
                self.buzz(self.printBuzz)
            else:
                self.number(num, self.prNumber)

    def prNumber(self, x):
        print(str(x))

    def printFizzBuzz(self):
        print("fizzbuzz")

    def printBuzz(self):
        print("buzz")

    def printFizz(self):
        print("fizz")

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        printFizz()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        printBuzz()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        printFizzBuzz()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, x, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        printNumber(x)


sl = FizzBuzz(15)
