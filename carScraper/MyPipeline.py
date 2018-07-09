from scrapy.exceptions import DropItem
import sqlite3
class MyPipeline(object):
    # used after the spider is started
    connection = null
    def open_spider(self,spider):
        # open a connection to sqlite3
        connection = sqlite3.connect("cars.db")
        

    def close_spider(self,spider):
        connection.commit()
        connection.close()

        
    def process_item(self, item, spider):
        # add the cars data into the appropiate table in the database

        # INSERT INTO CARS VALUE (item.name)
