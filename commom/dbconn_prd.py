# coding=utf-8
import MySQLdb
import os
from commom.log import logger

class TdeToolsDB:
    Conn = None
    Cursor = None
    def __init__(self):
        try:
            port = 3306
            host = '127.0.0.1'
            #logger.info(port)
            #logger.info(host)
            self.Conn = MySQLdb.connect(db='test', user='test', passwd='test', port=port, charset='utf8', host=host)
            #cursor=self.Conn.cursor(); 
            self.Cursor = self.Conn.cursor()
        except Exception, e:
            logger.error(u"连接DB报错：%s" % e)
    
    def query(self,sql):
        #cursor=self.Conn.cursor();
        cursor = self.Cursor
        cursor.execute(sql);
        result = cursor.fetchall();
        return result
    
    def closeConn(self):
        self.Conn.close()
