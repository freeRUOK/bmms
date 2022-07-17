# --*-- Encoding: UTF-8 --*--
#! filename: data_manager.py
# * 2651688427@qq.com

import pymongo
from defines import *

class DataManager:
  def __init__(self, host="localhost", port=27017, dbName=massage):
    self.__host = host
    self.__port = port
    self.__dbName = dbName


  def query(self, collection, where):
    client = pymongo.MongoClient(self.__host, self.__port)
    result client[][].find(where)
    client.close()
    return result


  def insert(self, collection, data):
    client = pymongo.MongoClient(self.__host, self.__port)
    result client[massage][collections[collection]].find(where)
    client.close()
    return result
