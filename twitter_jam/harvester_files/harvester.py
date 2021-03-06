#
# Team 43, Melbourne
# Aidan McLoughney(1030836)
# Thanaboon Muangwong(1049393)
# Nahid Tajik(1102790)
# Saket Khandelwal (1041999)
# Shmuli Bloom(982837)
#

import logging
from crawler import Crawler
from utils import setup_logging
import configparser
import tweepy.error as ex
import sys, os


def harvester():
    config = configparser.ConfigParser()
    file = os.getenv('CONFIG_FILE','ins_3.ini')
    config.read(f'config/{file}')

    logger = logging.getLogger('crawler')
    setup_logging()
    try:
        tweet = Crawler(config,logger)
        tweet.start_pipeline()
    except ex.TweepError as e:
        logger.error(e)
    except Exception as e:
        logger.exception(e)
    finally:
        sys.exit(0)
    

if __name__ == '__main__':
    harvester()


