import logging
logging.basicConfig(level=logging.DEBUG, filename='sqrt.log')    # DEBUG, INFO, WARN, ERROR



def sqrt(num, guess=1.0):
    if num < 0:
        logging.error("Got a request for square root of negative number.")
        raise ValueError


    logging.info("Find sqrt of {} with guess {}".format(num, guess))
    if good_enough(guess, num):
        return guess
    else:
        logging.debug("Guess is not good enough improve. ...")
        new_guess = improve_guess(guess, num)
        return sqrt(num, new_guess)
    
def good_enough(guess, num):
    logging.debug("Checking if {} is a good enough guess.".format(guess))
    if abs(guess * guess - num) < 0.1:
        return True
    else:
        return False

def avg(a, b):
    return (a+b)/2.0

def improve_guess(guess, num):
    new_guess = avg(guess, num/guess)
    logging.debug("Improved guess to {}".format(new_guess))
    return new_guess




if __name__ == '__main__':
    print(sqrt(87))