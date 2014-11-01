from yopy import Yo
import config
import requests
from pymongo import MongoClient

def main ():
	yo = Yo(config.devKey)
	print(yo.youser("GEORGEPLUKOV", ""))

main()
