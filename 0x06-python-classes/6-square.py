class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size ** self.__size)

    @property
    def size(self):
        return (__size)

    @property
    def position(self):
        return (__position)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    position.setter
    def position(self, value):
        if (not all(num < 0 for num in value)
                or not all(isinstance(num, int) for num in value)
                or not isinstance(value, tuple)
                or len(position) != 1):
            raise TypeError(position must be a tuple of 2 positive integers)
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()

