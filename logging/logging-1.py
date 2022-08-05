import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='example.log', level=logging.DEBUG)

logging.info("This is a info message")
logging.debug("This is a debug message")

logging.warning('Watch out!')
print(logging.DEBUG)
print(logging.INFO)
