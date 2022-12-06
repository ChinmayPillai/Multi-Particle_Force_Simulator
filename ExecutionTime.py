'''
Find Execution Time of any function given it's arguments
'''

import time


def excTime(func, *args):
    '''
    Code to find Execution Time of any required function. 
    The required function gets run with the given arguments before returning Execution Time

    Args:
        func (function): Function whose exececution time is to be found
        *args (*args): Arguments of the required function in order

    Returns:
        float: Execution Time of function
    '''

    start_time = time.time()

    func(*args)

    end_time = time.time()

    return end_time - start_time

'''
print(excTime())
'''