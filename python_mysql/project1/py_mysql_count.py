# -*- coding: utf8 -*-
import pymysql
import sys

class TransferMoney():
    def __init__(self,conn):
        self.conn=conn
    def check_acct_available(self,acctid):
        curs=self.conn.cursor()
        try:
            sql='select * from count where count_id=%s'%acctid
            curs.execute(sql)
            print('check_acct_available: '+sql)
            rs=curs.fetchall()
            if len(rs) != 1:
                raise Exception('账户%s不存在'%acctid)
        finally:
            curs.close()
            
    def has_enough_money(self,acctid,money):
        curs=self.conn.cursor()
        try:
            sql='select * from count where count_id=%s and count_money>%s'%(acctid,money)
            curs.execute(sql)
            print('has_enough_money: '+sql)
            rs=curs.fetchall()
            if len(rs) != 1:
                raise Exception('账户%s钱不够'%acctid)
        finally:
            curs.close()
    def reduce_money(self,acctid,money):
        curs=self.conn.cursor()
        try:
            sql='update count set count_money=count_money-%s where count_id=%s'%(money,acctid)
            curs.execute(sql)
            print('reduce_money: '+sql)
            rs=curs.fetchall()
            if curs.rowcount != 1:
                raise Exception('账户%s减钱失败'%acctid)
        finally:
            curs.close()
    def add_money(self,acctid,money):
        curs=self.conn.cursor()
        try:
            sql='update count set count_money=count_money+%s where count_id=%s'%(money,acctid)
            curs.execute(sql)
            print('add_money: '+sql)
            rs=curs.fetchall()
            if curs.rowcount != 1:
                raise Exception('账户%s加钱失败'%acctid)
        finally:
            curs.close()
    def transfer(self,source_acctid,target_acctid,money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

if __name__ == '__main__':
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    #print(money)
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='940211',db='python_mysql',charset='utf8')
    tr_money=TransferMoney(conn)
    
    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print('问题： '+str(e))
    finally:
        conn.close()
