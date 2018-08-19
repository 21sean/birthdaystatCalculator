from random import*


def random_birthday():
    """ Write 1200 random integers to a file named ’birthdays.dat’;
        each integer should be a random number between 1 and 365.
        >>> random_birthday (1200)
        1200 random ints
        Params: none
        Returns: (int) 1200  random  integers
        """
    f = open('birthdays.dat', 'w')
    birthdays_file = ''
    for i in range(1200):
        days = str(randrange(1, 365))
        birthdays_file += days + ' \n'
    f.write(birthdays_file)
    f.close()


def list_birthdays():
    """read ('r') the data in ’birthdays.dat’ into a list of integers.
            >>> listbirthdays (birthdays.dat)
            101
            Params: none
            Returns: (list) of 1200 random integers from 'birthdays.dat'
            """
    f = open('birthdays.dat', 'r')
    v = []
    for line in f:
        v.append(int(line))
    return v


def jan_birthday_count(k):

    """Count the jan. birthdays, using nested for loop.
    >>> jan_birthday_count (birthday.dat)
    101
    Params: k (int)
    Returns: (int) the number of jan. dates i.e. dates less than 32 from 'birthdays.dat'.
    """
    e = 0
    s = range(1,32)
    for i in s:
        for m in k:
            if i == m:
                e += 1
    return e


def problem_c():
    """ Call random_birthday(), set a variable function to use list birthdays function so that jan birthday
        count can work.
        Params: none
        Returns: (int) the number of jan. dates i.e. ints less than 32.
        """
    random_birthday()
    a = list_birthdays()
    return jan_birthday_count(a)


def problem_d():
    """ Repeating this experiment 10 times using for loop & empty list var.
        >>> jan_birthday_count (1200)
        101
        Params: x (int)
        Returns: (int) the number of jan. dates i.e. dates less than 32.
        """
    a = []
    for i in range(10):
        x = problem_c()
        a.append(x)
    return a


def compute_avg_jan_bd(a):
    """ compute the average of jan birthdays from 1200 random ints in the range 1,365.
        >>> compute_avg_jan_bd (birthdays.dat)
        107.6
        Params: a (list)
        Returns: (float) average the number of jan. dates i.e. dates less than 32.
        """
    n = sum(a)
    m = len(a)
    return n/m


print("1200 random days in a year:")
print(list_birthdays())
print("Number of Jan. birthdays from 10 lists of 1200 ints:")
print(problem_d())
x = problem_d()
print("Average of the 10 Jan. birthdays:")
print(compute_avg_jan_bd(x)) #from x = problem_d()