#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

class Study_control:
    '''
    Class for study control
    '''

    input = ''

    def __init__(self, input):

        self.input = input
        return

    def control(self):
        print('stud control enter %d' % self.input)
        return

    def control_if(self):
        if self.input == 1 :
            print('input is 1')
        else:
            print('input is not 1')
        return

    def area(self, width, length):
        return width * length
    
    def control_calc(self):
        # number
        value = 5 * 5
        if value == 25:
            print('ok value')
        
        test_area = self.area(5, 6)
        print('area 5 * 6 is', test_area)

        test_float = 1.1 * 8
        print('test float:%f' % test_float)

        # string
        str = 'hello' ' ' 'world'
        print('str: %s' % str)
        print('str index: %c' % str[4])
        print('str last: %c' % str[-1])
        print('str part: %s' % str[0:5])

        str_new = str[0:5] + " study"
        print('str new: %s' % str_new)

        # list
        mylist = [1, 3, 5, 7, 9]
        print(mylist)
        mylist[0] = 100
        print(mylist)
        mylist.append(11)
        print(mylist)
        print('list len: %d' % len(mylist))

        # Fibonacci
        a, b = 0, 1
        while a < 10:
            print(a, end=' ')
            a, b = b, a + 1
        print('')
        return

    def control_for(self):
        test_str = ['cat', 'window', 'hello']
        for w in test_str:
            print(w, len(w))
        
        test_str2 = {'cat':6, 'dog':3, 'duck':100}
        for animal, number in test_str2.copy().items():
            if number < 5:
                del test_str2[animal]
        print(test_str2)

        for i in range(5):
            print(i)

        for i in range(10, 20, 3):
            if i > 15:
                break
            print(i)
        return 0

    def control_while1(self):
        print('now in while 1, not return =============')
        while(True):
            pass
        return

    def control_match(self):
        "control match need python > 3.10"
        #value = 10
        # match need python > 3.10
        #match value:
        #    case 1:
        #        str = 'i don\'t know why'
        #    case 2 | 5:
        #        str = 'o , i know'
        #    case 10:
        #        str = 'it is result'
        
        #print(str)
        return
    
    def control_raise_exception(self):
        raise ValueError
        return
        

def help():
    print('0 -- control')
    print('1 -- control_calc')
    print('2 -- control_if')
    print('3 -- control_for')
    print('4 -- control_while_1')
    print('5 -- control_match')
    print('6 -- control_raise_exception')

def study_control_func():
    my_control = Study_control(2)
    choice = int(input("Please enter an integer: "))
    if choice == 0:
        my_control.control()
    elif choice == 1:
        my_control.control_calc()
    elif choice == 2:
        my_control.control_if()
    elif choice == 3:
        my_control.control_for()
    elif choice == 4:
        my_control.control_while1()
    elif choice == 5:
        my_control.control_match()
    elif choice == 6:
        my_control.control_raise_exception()
    else:
        help()

    return 0

