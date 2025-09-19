class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("Your jar should be able to hold atleast 1 cookie")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return  self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Too many cookies to fit in this jar.")
        self._capacity -= n
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("You have no or less cookies left.")
        self._capacity += n
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size



def main():
    cookieJar = Jar(20)
    print(cookieJar.capacity)
    cookieJar.deposit(10)
    print(cookieJar.size)
    print(cookieJar)




if __name__ == "__main__":
    main()
