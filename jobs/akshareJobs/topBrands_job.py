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

# 龙虎榜 专栏


# 龙虎榜-营业厅排名-上榜次数最多()
def stock_lh_yyb_most(tmp_datetime):
    #############################
    try:
        data = ak.stock_lh_yyb_most()

        common.insert_db(data, "ak_a_topBrands_business_hall_ranking_most_on_list", False, "`序号`")
    except Exception as e:
        print("error :", e)


# 龙虎榜-营业厅排名-资金实力最强()
def stock_lh_yyb_capital(tmp_datetime):
    #############################
    try:
        data = ak.stock_lh_yyb_capital()

        common.insert_db(data, "ak_a_topBrands_business_hall_ranking_strongest_financial", False, "`序号`")
    except Exception as e:
        print("error :", e)


# 龙虎榜-营业厅排名-抱团操作实力()
def stock_lh_yyb_control(tmp_datetime):
    #############################
    try:
        data = ak.stock_lh_yyb_control()

        common.insert_db(data, "ak_a_topBrands_business_hall_ranking_group_operation", False, "`序号`")
    except Exception as e:
        print("error :", e)


# 龙虎榜-每日详情()
def stock_sina_lhb_detail_daily(tmp_datetime):
    #############################
    try:
        trade_date_value = "20210923"
        symbol_value = "返回当前交易日所有可查询的指标"
        # trade_date	str	Y	trade_date="20200730"; 交易日
        # symbol	str	Y	symbol="涨幅偏离值达7%的证券"; 调用ak.stock_sina_lhb_detail_daily(trade_date="指定交易日", symbol="返回当前交易日所有可查询的指标")返回可以获取的指标
        symbols = ak.stock_sina_lhb_detail_daily(trade_date=trade_date_value, symbol=symbol_value)
        for symbol_str in symbols:
            data = ak.stock_sina_lhb_detail_daily(trade_date=trade_date_value, symbol=symbol_str)

            symbol = pd.DataFrame([symbol_str for _ in range(len(data))], columns=["symbol"])
            trade_date = pd.DataFrame([trade_date_value for _ in range(len(data))], columns=["trade_date"])
            new_data = pd.concat([symbol, trade_date, data], axis=1)
            common.insert_db(new_data, "ak_a_topBrands_daily_symbols_details", False, "`trade_date`,`symbol`,`序号`")
    except Exception as e:
        print("error :", e)


# 龙虎榜-个股上榜统计()
def stock_sina_lhb_ggtj(tmp_datetime):
    #############################
    try:
        recent_day_value = "10"
        # recent_day	str	Y	recent_day="5"; choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;}
        data = ak.stock_sina_lhb_ggtj(recent_day=recent_day_value)
        recent_day = pd.DataFrame([recent_day_value for _ in range(len(data))], columns=["recent_day"])
        new_data = pd.concat([recent_day, data], axis=1)

        common.insert_db(new_data, "ak_a_topBrands_individual_statistics", False, "`recent_day`,`股票代码`")
    except Exception as e:
        print("error :", e)


#  龙虎榜-营业上榜统计()
def stock_sina_lhb_yytj(tmp_datetime):
    #############################
    try:
        recent_day_value = "10"
        # recent_day	str	Y	recent_day="5"; choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;}
        data = ak.stock_sina_lhb_yytj(recent_day=recent_day_value)
        recent_day = pd.DataFrame([recent_day_value for _ in range(len(data))], columns=["recent_day"])
        new_data = pd.concat([recent_day, data], axis=1)

        common.insert_db(new_data, "ak_a_topBrands_business_hall_statistics", False, "`recent_day`,`营业部名称`")
    except Exception as e:
        print("error :", e)


#  龙虎榜-机构席位追踪()
def stock_sina_lhb_jgzz(tmp_datetime):
    #############################
    try:
        recent_day_value = "10"
        # recent_day	str	Y	recent_day="5"; choice of {"5": 最近 5 天; "10": 最近 10 天; "30": 最近 30 天; "60": 最近 60 天;}
        data = ak.stock_sina_lhb_jgzz(recent_day=recent_day_value)
        recent_day = pd.DataFrame([recent_day_value for _ in range(len(data))], columns=["recent_day"])
        new_data = pd.concat([recent_day, data], axis=1)

        common.insert_db(new_data, "ak_a_topBrands_institutional_seat_tracking", False, "`recent_day`,`股票代码`")
    except Exception as e:
        print("error :", e)


#  龙虎榜-机构席位成交明细()
def stock_sina_lhb_jgmx(tmp_datetime):
    #############################
    try:
        data = ak.stock_sina_lhb_jgmx()
        data["自增序列"] = range(1, len(data) + 1)

        common.insert_db(data, "ak_a_topBrands_institutional_seat_transaction_details", False, "`自增序列`,`股票代码`")
    except Exception as e:
        print("error :", e)


# main函数入口
if __name__ == '__main__':
    # common.run_with_args(stock_lh_yyb_most)
    # common.run_with_args(stock_lh_yyb_capital)
    # common.run_with_args(stock_lh_yyb_control)
    # common.run_with_args(stock_sina_lhb_detail_daily)
    # common.run_with_args(stock_sina_lhb_ggtj)
    # common.run_with_args(stock_sina_lhb_yytj)
    # common.run_with_args(stock_sina_lhb_jgzz)
    common.run_with_args(stock_sina_lhb_jgmx)





