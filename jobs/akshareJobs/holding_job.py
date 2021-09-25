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

# 持股统计 专栏


# 沪深港通持股-北向净流入()
def stock_em_hsgt_north_net_flow_in(tmp_datetime):
    #############################
    try:
        indicator_value = "沪股通"
        # indicator	str	indicator="沪股通"; choice of {"沪股通", "深股通", "北上"}
        data = ak.stock_em_hsgt_north_net_flow_in(indicator=indicator_value)
        # 描述: 东方财富网-数据中心-特色数据-沪深港通持股; 注: 资金净流入=当日资金限额-当日资金余额; 资金净流入包含当日成交净买额和当日买入申报未成交金额; 北向资金是沪股通与深股通的资金加总
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])

        new_data = pd.concat([indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_north_inflow", False, "`indicator`,`date`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-北向资金余额()
def stock_em_hsgt_north_cash(tmp_datetime):
    #############################
    # 描述: 东方财富网-数据中心-特色数据-沪深港通持股; 注: 资金净流入=当日资金限额-当日资金余额; 资金净流入包含当日成交净买额和当日买入申报未成交金额; 北向资金是沪股通与深股通的资金加总
    try:
        indicator_value = "沪股通"
        # indicator	str	indicator="沪股通"; 三选一 ("沪股通", "深股通", "北上")
        data = ak.stock_em_hsgt_north_cash(indicator=indicator_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])

        new_data = pd.concat([indicator, data], axis=1)
        common.insert_db(new_data, "ak_a_holding_north_fund_balance", False, "`indicator`,`date`")

    except Exception as e:
        print("error :", e)


# 沪深港通持股-北向累计净流入()
def stock_em_hsgt_north_acc_flow_in(tmp_datetime):
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-沪深港通持股, 注: 资金净流入=当日资金限额-当日资金余额; 资金净流入包含当日成交净买额和当日买入申报未成交金额; 北向资金是沪股通与深股通的资金加总
    try:
        indicator_value = "沪股通"
        # indicator	str	indicator="沪股通"; 三选一 ("沪股通", "深股通", "北上")
        data = ak.stock_em_hsgt_north_acc_flow_in(indicator=indicator_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])

        new_data = pd.concat([indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_north_accumulated_inflow", False, "`indicator`,`date`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-南向净流入()
def stock_em_hsgt_south_net_flow_in(tmp_datetime):
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-沪深港通持股; 注: 资金净流入=当日资金限额-当日资金余额; 资金净流入包含当日成交净买额和当日买入申报未成交金额; 南向资金是沪股通与深股通的资金加总
    try:
        indicator_value = "沪股通"
        # indicator	str	indicator="沪股通"; 三选一 ("沪股通", "深股通", "北上")
        data = ak.stock_em_hsgt_south_net_flow_in(indicator=indicator_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])

        new_data = pd.concat([indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_south_inflow", False, "`indicator`,`date`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-南向资金余额()
def stock_em_hsgt_south_cash(tmp_datetime):
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-沪深港通持股, 注: 资金净流入=当日资金限额-当日资金余额; 资金净流入包含当日成交净买额和当日买入申报未成交金额; 南向资金是沪股通与深股通的资金加总
    try:
        indicator_value = "沪股通"
        # indicator	str	indicator="沪股通"; 三选一 ("沪股通", "深股通", "北上")
        data = ak.stock_em_hsgt_south_cash(indicator=indicator_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])

        new_data = pd.concat([indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_south_fund_balance", False, "`indicator`,`date`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-南向累计净流入()
def stock_em_hsgt_south_acc_flow_in(tmp_datetime):
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-沪深港通持股, 注: 资金净流入=当日资金限额-当日资金余额; 资金净流入包含当日成交净买额和当日买入申报未成交金额; 南向资金是沪股通与深股通的资金加总
    try:
        indicator_value = "沪股通"
        # indicator	str	indicator="沪股通"; 三选一 ("沪股通", "深股通", "北上")
        data = ak.stock_em_hsgt_south_acc_flow_in(indicator=indicator_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])

        new_data = pd.concat([indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_south_accumulated_inflow", False, "`indicator`,`date`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-个股排行()
def stock_em_hsgt_hold_stock(tmp_datetime):
    ##########################
    # 描述: 东方财富网-数据中心-沪深港通持股-个股排行
    try:
        indicator_value = "今日排行"
        market_value = "沪股通"
        # market	str	market="沪股通"; choice of {"北向", "沪股通", "深股通"}
        # indicator	str	indicator="沪股通"; choice of {"今日排行", "3日排行", "5日排行", "10日排行", "月排行", "季排行", "年排行"}
        data = ak.stock_em_hsgt_hold_stock(market=market_value, indicator=indicator_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])
        market = pd.DataFrame([market_value for _ in range(len(data))], columns=["market"])

        new_data = pd.concat([market, indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_individual_ranking", False, "`market`,`indicator`,`序号`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-板块排行()
def stock_em_hsgt_board_rank(tmp_datetime):
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-沪深港通持股, 注: 资金净流入=当日资金限额-当日资金余额; 资金净流入包含当日成交净买额和当日买入申报未成交金额; 南向资金是沪股通与深股通的资金加总
    try:
        indicator_value = "3日"
        symbol_value = "北向资金增持行业板块排行"
        # symbol	str	Y	symbol="北向资金增持行业板块排行"; choice of {"北向资金增持行业板块排行", "北向资金增持概念板块排行", "北向资金增持地域板块排行"}
        # indicator	str	Y	indicator="今日"; choice of {"今日", "3日", "5日", "10日", "1月", "1季", "1年"}
        data = ak.stock_em_hsgt_board_rank(symbol=symbol_value, indicator=indicator_value)
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_plate_ranking", False, "`symbol`,`indicator`,`序号`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-每日个股统计()
def stock_em_hsgt_stock_statistics(tmp_datetime):
    ##########################
    # 描述: 东方财富网-数据中心-沪深港通-沪深港通持股-每日个股统计
    try:
        start_date_value = "20210922"
        end_date_value = "20210924"
        symbol_value = "沪股通持股"
        # symbol	str	symbol="北向持股"; choice of {"北向持股", "沪股通持股", "深股通持股", "南向持股"}
        # start_date	str	start_date="20210601"; 此处指定近期交易日
        # end_date	str	end_date="20210608"; 此处指定近期交易日
        data = ak.stock_em_hsgt_stock_statistics(symbol=symbol_value, start_date=start_date_value, end_date=end_date_value)
        data = data.reset_index()
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_individual_statistics_daily", False, "`symbol`,`index`,`持股日期`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-每日机构统计()
def stock_em_hsgt_institution_statistics(tmp_datetime):
    ##########################
    # 描述: 东方财富网-数据中心-沪深港通-沪深港通持股-每日机构统计
    try:
        market_value = "沪股通持股"
        # market	str	market="北向持股"; choice of {"北向持股", "沪股通持股", "深股通持股", "南向持股"}
        data = ak.stock_em_hsgt_institution_statistics(market=market_value, start_date="20210922", end_date="20210924")
        data = data.reset_index()
        market = pd.DataFrame([market_value for _ in range(len(data))], columns=["market"])

        new_data = pd.concat([market, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_institutional_statistics_daily", False, "`market`,`index`,`持股日期`")
    except Exception as e:
        print("error :", e)


# 沪深港通持股-沪深港通历史数据()
def stock_em_hsgt_hist(tmp_datetime):
    ##########################
    # 描述: 获取东方财富网-数据中心-资金流向-沪深港通资金流向-沪深港通历史数据
    try:
        symbol_value = "沪股通"
        # symbol	str	Y	symbol="港股通沪"; choice of {"沪股通", "深股通", "港股通沪", "港股通深"}
        data = ak.stock_em_hsgt_hist(symbol=symbol_value)
        data = data.reset_index()
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)

        common.insert_db(new_data, "ak_a_holding_history_data", False, "`symbol`,`index`,`日期`")
    except Exception as e:
        print("error :", e)



# main函数入口
if __name__ == '__main__':
    # common.run_with_args(stock_em_hsgt_north_net_flow_in)
    # common.run_with_args(stock_em_hsgt_north_cash)
    # common.run_with_args(stock_em_hsgt_north_acc_flow_in)
    # common.run_with_args(stock_em_hsgt_south_net_flow_in)
    # common.run_with_args(stock_em_hsgt_south_cash)
    # common.run_with_args(stock_em_hsgt_south_acc_flow_in)
    # common.run_with_args(stock_em_hsgt_hold_stock)
    # common.run_with_args(stock_em_hsgt_board_rank)
    # common.run_with_args(stock_em_hsgt_stock_statistics)
    # common.run_with_args(stock_em_hsgt_institution_statistics)
    common.run_with_args(stock_em_hsgt_hist)





