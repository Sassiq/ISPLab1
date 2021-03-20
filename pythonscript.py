import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("outputLog.log"))


def fib(num):
    num1 = num2 = 1

    index = 0
    while index < num - 2:
        num1, num2 = num2, num1 + num2
        index += 1

    return num2


if __name__ == "__main__":
    logger.info(fib(25))
