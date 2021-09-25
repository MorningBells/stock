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

# 资金流向 专栏


# 资金流向-个股资金流()
def stock_fund_flow_individual(tmp_datetime):
    #############################
    try:
        symbol_value = "3日排行"
        # symbol	str	Y	symbol="即时"; choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"}
        data = ak.stock_fund_flow_individual(symbol=symbol_value)
        # 描述: 获取同花顺-数据中心-资金流向-个股资金流
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])
        new_data = pd.concat([symbol, data], axis=1)

        common.insert_db(new_data, "ak_a_capital_flow_individual", False, "`symbol`,`序号`")
    except Exception as e:
        print("error :", e)


# 资金流向-概念资金流()
def stock_fund_flow_concept(tmp_datetime):
    #############################
    # 描述: 同花顺-数据中心-资金流向-概念资金流
    try:
        symbol_value = "3日排行"
        # symbol	str	symbol="即时"; choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"}
        data = ak.stock_fund_flow_concept(symbol=symbol_value)
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_capital_flow_concept", False, "`symbol`,`序号`")

    except Exception as e:
        print("error :", e)


# 资金流向-行业资金流()
def stock_fund_flow_industry(tmp_datetime):
    #############################
    # 描述: 同花顺-数据中心-资金流向-行业资金流
    try:
        symbol_value = "3日排行"
        # symbol	str	symbol="即时"; choice of {“即时”, "3日排行", "5日排行", "10日排行", "20日排行"}
        data = ak.stock_fund_flow_industry(symbol=symbol_value)
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_capital_flow_industry", False, "`symbol`,`序号`")

    except Exception as e:
        print("error :", e)


# 资金流向-大单追踪()
def stock_fund_flow_big_deal(tmp_datetime):
    #############################
    # 描述: 获取同花顺-数据中心-资金流向-大单追踪
    try:
        data = ak.stock_fund_flow_big_deal()
        data = data.reset_index()

        common.insert_db(data, "ak_a_capital_flow_large_order_tracking", False, "`index`,`成交时间`,`股票代码`")

    except Exception as e:
        print("error :", e)


# 资金流向-个股资金流排名()
def stock_individual_fund_flow_rank(tmp_datetime):
    #############################
    # 描述: 获取东方财富网-数据中心-资金流向-排名
    try:
        indicator_value = "3日"
        # indicator	str	Y	indicator="今日"; choice {"今日", "3日", "5日", "10日"}
        data = ak.stock_individual_fund_flow_rank(indicator=indicator_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])
        new_data = pd.concat([indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_capital_flow_individual_ranking", False, "`indicator`,`序号`")

    except Exception as e:
        print("error :", e)


# 资金流向-大盘资金流()
def stock_market_fund_flow(tmp_datetime):
    #############################
    # 描述: 获取东方财富网-数据中心-资金流向-排名
    try:
        data = ak.stock_market_fund_flow()

        common.insert_db(data, "ak_a_capital_flow_market", False, "日期")

    except Exception as e:
        print("error :", e)


# 资金流向-板块资金流排名()
def stock_sector_fund_flow_rank(tmp_datetime):
    #############################
    # 描述: 获取东方财富网-数据中心-资金流向-板块资金流-排名
    try:
        indicator_value = "5日"
        sector_type_value = "行业资金流"
        # indicator	str	Y	indicator="5日"; choice of {"今日", "5日", "10日"}
        # sector_type	str	Y	sector_type="地域资金流"; choice of {"行业资金流": "2", "概念资金流": "3", "地域资金流": "1"}
        data = ak.stock_sector_fund_flow_rank(indicator=indicator_value, sector_type=sector_type_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])
        sector_type = pd.DataFrame([sector_type_value for _ in range(len(data))], columns=["sector_type"])

        new_data = pd.concat([indicator, sector_type, data], axis=1)
        common.insert_db(new_data, "ak_a_capital_flow_plate_ranking", False, "`indicator`,`sector_type`,`名称`")

    except Exception as e:
        print("error :", e)


# main函数入口
if __name__ == '__main__':
    # common.run_with_args(stock_fund_flow_individual)
    # common.run_with_args(stock_fund_flow_concept)
    # common.run_with_args(stock_fund_flow_industry)
    # common.run_with_args(stock_fund_flow_big_deal)
    # common.run_with_args(stock_individual_fund_flow_rank)
    # common.run_with_args(stock_market_fund_flow)
    common.run_with_args(stock_sector_fund_flow_rank)





