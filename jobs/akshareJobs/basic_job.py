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

# 600开头的股票是上证A股，属于大盘股
# 600开头的股票是上证A股，属于大盘股，其中6006开头的股票是最早上市的股票，
# 6016开头的股票为大盘蓝筹股；900开头的股票是上证B股；
# 000开头的股票是深证A股，001、002开头的股票也都属于深证A股，
# 其中002开头的股票是深证A股中小企业股票；
# 200开头的股票是深证B股；
# 300开头的股票是创业板股票；400开头的股票是三板市场股票。
def stock_a(code):
    # print(code)
    # print(type(code))
    # 上证A股  # 深证A股
    if code.startswith('600') or code.startswith('6006') or code.startswith('601') or code.startswith('000') or code.startswith('001') or code.startswith('002'):
        return True
    else:
        return False
# 过滤掉 st 股票。
def stock_a_filter_st(name):
    # print(code)
    # print(type(code))
    # 上证A股  # 深证A股
    if name.find("ST") == -1:
        return True
    else:
        return False

# 过滤价格，如果没有基本上是退市了。
def stock_a_filter_price(latest_price):
    # float 在 pandas 里面判断 空。
    if np.isnan(latest_price):
        return False
    else:
        return True

####### 3.pdf 方法。宏观经济数据
# 接口全部有错误。只专注股票数据。
def stat_all(tmp_datetime):

    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)





# 上海证券交易所-股票数据总貌
def stock_sse_summary(tmp_datetime):
    #############################
    # 上海证券交易所
    try:
        data = ak.stock_sse_summary()
        # 描述: 上海证券交易所-股票数据总貌
        common.insert_db(data, "ak_a_basic_market_appearance", False, "`type`,`item`")

    except Exception as e:
        print("error :", e)


# 上海证券交易所-每日概况
def stock_sse_deal_daily(tmp_datetime):
    #############################
    # 上海证券交易所-每日概况
    #描述: 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况
    try:
        data = ak.stock_sse_deal_daily()
        # 描述: 上海证券交易所-每日概况
        common.insert_db(data, "ak_a_basic_exchanger_daily_summary", False, "单日情况")

    except Exception as e:
        print("error :", e)


# 东方财富网-实时行情数据
def stock_zh_a_spot_em(tmp_datetime):
    ##########################
    # 实时行情数据-东财
    # 东方财富网-实时行情数据
    try:
        data = ak.stock_zh_a_spot_em()
        # 描述: 东方财富网-实时行情数据
        common.insert_db(data, "ak_a_basic_realtime_market_data", False, "序号")
    except Exception as e:
        print("error :", e)


# 东方财富网-A股历史行情数据
def stock_zh_a_hist(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 历史行情数据-东财
    # 东方财富网-A股历史行情数据
    try:
        symbol_value = "603777";
        # symbol	str	symbol='603777'; 股票代码可以在 ak.stock_zh_a_spot_em() 中获取
        # period	str	period='daily'; choice of {'daily', 'weekly', 'monthly'}
        # start_date	str	start_date='20210301'; 开始查询的日期
        # end_date	str	end_date='20210616'; 结束查询的日期
        # adjust	str	默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据

        # 股票数据复权
        # 1.为何要复权：由于股票存在配股、分拆、合并和发放股息等事件，会导致股价出现较大的缺口。 若使用不复权的价格处理数据、计算各种指标，将会导致它们失去连续性，且使用不复权价格计算收益也会出现错误。 为了保证数据连贯性，常通过前复权和后复权对价格序列进行调整。
        # 2.前复权：保持当前价格不变，将历史价格进行增减，从而使股价连续。 前复权用来看盘非常方便，能一眼看出股价的历史走势，叠加各种技术指标也比较顺畅，是各种行情软件默认的复权方式。 这种方法虽然很常见，但也有两个缺陷需要注意。
        # 2.1 为了保证当前价格不变，每次股票除权除息，均需要重新调整历史价格，因此其历史价格是时变的。 这会导致在不同时点看到的历史前复权价可能出现差异。
        # 2.2 对于有持续分红的公司来说，前复权价可能出现负值。
        # 3.后复权：保证历史价格不变，在每次股票权益事件发生后，调整当前的股票价格。 后复权价格和真实股票价格可能差别较大，不适合用来看盘。 其优点在于，可以被看作投资者的长期财富增长曲线，反映投资者的真实收益率情况。
        # 4.在量化投资研究中普遍采用后复权数据。
        data = ak.stock_zh_a_hist(symbol=symbol_value, period="weekly", adjust="qfq", start_date="20210101", end_date=datetime_int)
        # 描述: 东方财富网-A股历史行情数据
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_basic_history_market_data", False, "`symbol`, `日期`")
    except Exception as e:
        print("error :", e)


# 东方财富网-分时数据-东财
def stock_zh_a_hist_min_em(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 分时数据-东财
    # 东方财富网-分时数据
    try:
        symbol_value = "603777"
        # symbol	str	symbol='sh000300'; 股票代码
        # period	str	period='5'; choice of {'1', '5', '15', '30', '60'}; 其中 1 分钟数据返回近 5 个交易日数据且不复权
        # adjust	str	adjust=''; choice of {'', 'qfq', 'hfq'}; '': 不复权, 'qfq': 前复权, 'hfq': 后复权, 其中 1 分钟数据返回近 5 个交易日数据且不复权
        # start_date	str	start_date="1979-09-01 09:32:00"; 日期时间; 默认返回所有数据
        # end_date	str	end_date="2222-01-01 09:32:00"; 日期时间; 默认返回所有数据
        data = ak.stock_zh_a_hist_min_em(symbol=symbol_value, period="5", adjust="qfq", start_date="20210101", end_date=datetime_int)
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_basic_time_sharing_data", False, "`symbol`, `时间`")
    except Exception as e:
        print("error :", e)


# 东方财富网-盘前数据-东财
def stock_zh_a_hist_pre_min_em(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 盘前数据-东财
    # 东方财富网-盘前数据
    try:
        symbol_value = "603777"
        # symbol	str	symbol="000001"; 股票代码
        # start_time	str	start_date="09:00:00"; 时间; 默认返回所有数据
        # end_time	str	end_date="15:40:00"; 时间; 默认返回所有数据
        data = ak.stock_zh_a_hist_pre_min_em(symbol=symbol_value, start_time="09:00:00", end_time="16:00:00")
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_basic_pre_disk_data", False, "`symbol`, `时间`")
    except Exception as e:
        print("error :", e)


# 历史分笔数据-网易
def stock_zh_a_tick_163(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 历史分笔数据-网易
    # 描述: A 股 Tick 数据是从网易财经获取, 历史数据按日频率更新, 晚上 10 更新数据; 可以调用 stock_zh_a_tick_163_now(code=”000001”) 接口获取 当日数据(该接口只能在交易日获取数据), 主要参数无市场标识
    try:
        symbol_value = "sh600848"
        # symbol	str	Y	symbol="sh600000"
        # trade_date	datetime	Y	trade_date="20200408"
        data = ak.stock_zh_a_tick_163(code=symbol_value, trade_date="20210923")
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_basic_historical_calculus_data", False, "`symbol`, `时间`")
    except Exception as e:
        print("error :", e)


# A股CDR-历史行情数据
def stock_zh_a_cdr_daily(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # A股CDR-历史行情数据
    # 描述: 上海证券交易所 - 科创板 - CDR
    try:
        symbol_value = "sh600848"
        # symbol	str	symbol='sh689009'; CDR 股票代码
        # start_date	str	start_date='20201103'
        # end_date	str	end_date='20201116'
        data = ak.stock_zh_a_cdr_daily(symbol=symbol_value, start_date="20100923", end_date=datetime_int)
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_basic_cdr_data", False, "`symbol`, `date`")
    except Exception as e:
        print("error :", e)


# 股票指数-实时行情指数
def stock_zh_index_spot(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 中国股票指数数据, 注意该股票指数指新浪提供的国内股票指数
    try:
        data = ak.stock_zh_index_spot()
        common.insert_db(data, "ak_a_basic_index_realtime_market_data", False, "代码")
    except Exception as e:
        print("error :", e)


# 股票指数-历史行情数据
def stock_zh_index_daily(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 描述: 股票指数数据是从新浪财经获取的数据, 历史数据按日频率更新
    try:
        symbol_value = "sh600848"
        # symbol	str	Y	symbol="sz399552"
        data = ak.stock_zh_index_daily(symbol=symbol_value)
        # 重置索引
        data = data.reset_index()
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])
        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_basic_index_history_market_data", False, "`symbol`, `date`")
    except Exception as e:
        print("error :", e)


# main函数入口
if __name__ == '__main__':
    common.run_with_args(stock_sse_summary)
    common.run_with_args(stock_sse_deal_daily)
    common.run_with_args(stock_zh_a_spot_em)
    # 暂时使用默认的股票
    common.run_with_args(stock_zh_a_hist)
    common.run_with_args(stock_zh_a_hist_min_em)
    common.run_with_args(stock_zh_a_hist_pre_min_em)
    common.run_with_args(stock_zh_a_tick_163)
    common.run_with_args(stock_zh_a_cdr_daily)
    common.run_with_args(stock_zh_index_spot)
    common.run_with_args(stock_zh_index_daily)





