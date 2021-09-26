#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import libs.common as common
import sys
import time
import pandas as pd
import numpy as np
from sqlalchemy.types import NVARCHAR
from sqlalchemy import inspect
import datetime
import akshare as ak

import MySQLdb

# 涨停板 专栏


# 涨停板行情-涨停股池()
def stock_em_zt_pool(tmp_datetime):
    #############################
    try:
        date_value = "20210525"
        # date	str	Y	date='20210525'
        data = ak.stock_em_zt_pool(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_raising_limit_pool", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 涨停板行情-昨日涨停板股池()
def stock_em_zt_pool_previous(tmp_datetime):
    #############################
    try:
        date_value = "20210525"
        # date	str	Y	date='20210525'
        data = ak.stock_em_zt_pool_previous(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_raising_limit_yesterday", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 涨停板行情-强势股池()
def stock_em_zt_pool_strong(tmp_datetime):
    #############################
    try:
        date_value = "20210525"
        # date	str	Y	date='20210525'
        data = ak.stock_em_zt_pool_strong(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_raising_limit_strong_pool", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 涨停板行情-次新股池()
def stock_em_zt_pool_sub_new(tmp_datetime):
    #############################
    try:
        date_value = "20210525"
        # date	str	Y	date='20210525'
        data = ak.stock_em_zt_pool_sub_new(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_raising_limit_ipo_pool", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 涨停板行情-炸板股池()
def stock_em_zt_pool_zbgc(tmp_datetime):
    #############################
    try:
        date_value = "20210525"
        # date	str	Y	date='20210525'
        data = ak.stock_em_zt_pool_zbgc(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_raising_limit_fried_plate", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 涨停板行情-跌停股池()
def stock_em_zt_pool_dtgc(tmp_datetime):
    #############################
    try:
        date_value = "20210525"
        # date	str	Y	date='20210525'
        data = ak.stock_em_zt_pool_dtgc(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_raising_limit_limit_down", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# main函数入口
if __name__ == '__main__':
    # common.run_with_args(stock_em_zt_pool)
    # common.run_with_args(stock_em_zt_pool_previous)
    # common.run_with_args(stock_em_zt_pool_strong)
    # common.run_with_args(stock_em_zt_pool_sub_new)
    # common.run_with_args(stock_em_zt_pool_zbgc)
    common.run_with_args(stock_em_zt_pool_dtgc)





