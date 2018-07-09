# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class CarscraperPipeline(object):
    connection = sqlite3.connect("cars.db")

    def close_spider(self,spider):
        self.connection.commit()
        self.connection.close()
        
    def process_item(self, item, spider):
        # inserting the items name into the insert statement. one more time. Say it with me. Insert.
        name = item['name']
        items = [item['name'],item['power'],item['maxPowerRpm'],item['torque'],item['maxTorqueRpm']]
        power = item['power']
        max_power_rpm = item['maxPowerRpm']
        torque = item['torque']
        max_torque_rpm = item['maxTorqueRpm']
        record = "'" +name + "','" + power + "','" + max_power_rpm + "','" + torque + "','" + max_torque_rpm + "'"
        self.connection.execute("INSERT INTO CARS (NAME,POWER,MAX_POWER_RPM,TORQUE,MAX_TORQUE_RPM) VALUES (?,?,?,?,?)",items)

        return item
