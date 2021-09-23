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

# 股票分区 专栏


# 次新股
def stock_zh_a_new(tmp_datetime):
    #############################
    try:
        data = ak.stock_zh_a_new()
        # 描述: 新浪财经-行情中心-沪深股市-次新股
        common.insert_db(data, "ak_a_partition_ipo", False, "symbol")
    except Exception as e:
        print("error :", e)


# 风险警示板
def stock_zh_a_st_em(tmp_datetime):
    #############################
    # 描述: 东方财富网-行情中心-沪深个股-风险警示板
    try:
        data = ak.stock_zh_a_st_em()
        common.insert_db(data, "ak_a_partition_st", False, "序号")

    except Exception as e:
        print("error :", e)


# 新股
def stock_zh_a_new_em(tmp_datetime):
    ##########################
    # 描述: 东方财富网-行情中心-沪深个股-新股
    try:
        data = ak.stock_zh_a_new_em()
        # 描述: 获取东方财富网-数据中心-特色数据-商誉-个股商誉减值明细
        common.insert_db(data, "ak_a_partition_new", False, "序号")
    except Exception as e:
        print("error :", e)


# 两网及退市股
def stock_zh_a_stop_em(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 东方财富网-行情中心-沪深个股-两网及退市
    try:
        data = ak.stock_zh_a_stop_em()
        common.insert_db(data, "ak_a_partition_stop", False, "序号")
    except Exception as e:
        print("error :", e)


# 打新收益
def stock_em_dxsyl(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 东方财富网-数据中心-新股数据-打新收益率
    try:
        # market	str	market="上海主板"; choice of {"上海主板", "创业板", "深圳主板"}
        data = ak.stock_em_dxsyl(market="上海主板")

        common.insert_db(data, "ak_a_partition_new_yields", False, "股票代码")
    except Exception as e:
        print("error :", e)


# 新股申购与中签
def stock_em_xgsglb(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-新股数据-新股申购与中签查询
    try:
        # market	str	market="全部股票"; choice of {"全部股票", "沪市A股", "科创板", "深市A股", "创业板"}
        data = ak.stock_em_xgsglb(market="全部股票")

        common.insert_db(data, "ak_a_partition_initial_public_offerings", False, "股票代码")
    except Exception as e:
        print("error :", e)


# 科创板-实时行情数据
def stock_zh_kcb_spot(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 从新浪财经获取科创板股票数据
    try:
        data = ak.stock_zh_kcb_spot()

        common.insert_db(data, "ak_a_partition_ipo_science_board_realtime_data", False, "symbol")
    except Exception as e:
        print("error :", e)


# 科创板-历史行情数据
def stock_zh_kcb_daily(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 科创板股票数据是从新浪财经获取
    try:
        symbol_value = "sh688008"
        # symbol	str	Y	symbol="sh688008"
        # adjust	str	Y	默认不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据; hfq-factor: 返回后复权因子; hfq-factor: 返回前复权因子
        data = ak.stock_zh_kcb_daily(symbol=symbol_value, adjust="hfq")
        data = data.reset_index()
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_partition_ipo_science_board_history_data", False, "`symbol`,`date`")
    except Exception as e:
        print("error :", e)


# 科创板-科创板公告
def stock_zh_kcb_report_em(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 科创板股票数据是从新浪财经获取
    try:
        # from_page	int	from_page=1; 始获取的页码
        # to_page	int	to_page=100; 结束获取的页码
        data = ak.stock_zh_kcb_report_em(from_page=1, to_page=100)

        common.insert_db(data, "ak_a_partition_ipo_science_board_history_notice", False, "`代码`,`公告代码`")
    except Exception as e:
        print("error :", e)


# main函数入口
if __name__ == '__main__':
    # common.run_with_args(stock_zh_a_new)
    # common.run_with_args(stock_zh_a_st_em)
    # common.run_with_args(stock_zh_a_new_em)
    # common.run_with_args(stock_zh_a_stop_em)
    # common.run_with_args(stock_em_dxsyl)
    # common.run_with_args(stock_em_xgsglb)
    # common.run_with_args(stock_zh_kcb_spot)
    # common.run_with_args(stock_zh_kcb_daily)
    common.run_with_args(stock_zh_kcb_report_em)





