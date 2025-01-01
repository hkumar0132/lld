from ErrorLogProcessor import ErrorLogProcessor
from DebugLogProcessor import DebugLogProcessor
from InfoLogProcessor import InfoLogProcessor
from constants import ERROR, DEBUG, INFO

def main():

    logger = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))

    logger.log(ERROR, "400 received from API")
    logger.log(DEBUG, "[D]: variable_name")
    logger.log(INFO, "Postgres connection established")

if __name__ == "__main__":
    main()