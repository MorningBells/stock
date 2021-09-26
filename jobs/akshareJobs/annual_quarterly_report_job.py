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

# 年报季报 专栏


# 年报季报-业绩报表()
def stock_em_yjbb(tmp_datetime):
    #############################
    try:
        date_value = "20210630"
        # date	str	Y	date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始
        data = ak.stock_em_yjbb(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_annual_quarterly_report_performance_statements", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 年报季报-业绩快报()
def stock_em_yjkb(tmp_datetime):
    #############################
    try:
        date_value = "20210630"
        # date	str	Y	date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始
        data = ak.stock_em_yjkb(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_annual_quarterly_report_performance_express", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 年报季报-业绩预告()
def stock_em_yjyg(tmp_datetime):
    #############################
    try:
        date_value = "20210630"
        # date	str	Y	date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始
        data = ak.stock_em_yjyg(date=date_value)
        data.rename(columns={"业绩变动原因": "业绩变动原因text"}, inplace=True)

        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_annual_quarterly_report_performance_forecast", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 年报季报-预计披露时间()
def stock_em_yysj(tmp_datetime):
    #############################
    try:
        date_value = "20210630"
        # date	str	Y	date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始
        data = ak.stock_em_yysj(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_annual_quarterly_report_expected_disclosure_time", False, "`date`,`scode`")
    except Exception as e:
        print("error :", e)


# 年报季报-资产负债表()
def stock_em_zcfz(tmp_datetime):
    #############################
    try:
        date_value = "20210630"
        # date	str	Y	date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始
        data = ak.stock_em_zcfz(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_annual_quarterly_report_balance_sheet", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 年报季报-利润表()
def stock_em_lrb(tmp_datetime):
    #############################
    try:
        date_value = "20210630"
        # date	str	Y	date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始
        data = ak.stock_em_lrb(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_annual_quarterly_report_profit_statement", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 年报季报-现金流量表()
def stock_em_xjll(tmp_datetime):
    #############################
    try:
        date_value = "20210630"
        # date	str	Y	date="20200331"; choice of {"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"}; 从 20100331 开始
        data = ak.stock_em_xjll(date=date_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_annual_quarterly_report_cash_flow", False, "`date`,`序号`")
    except Exception as e:
        print("error :", e)


# main函数入口
if __name__ == '__main__':
    # common.run_with_args(stock_em_yjbb)
    # common.run_with_args(stock_em_yjkb)
    # common.run_with_args(stock_em_yjyg)
    # common.run_with_args(stock_em_yysj)
    # common.run_with_args(stock_em_zcfz)
    # common.run_with_args(stock_em_lrb)
    common.run_with_args(stock_em_xjll)





