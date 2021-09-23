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

# 商誉专栏


# A股商誉市场概况
def stock_em_sy_profile(tmp_datetime):
    #############################
    # A股商誉市场概况
    try:
        data = ak.stock_em_sy_profile()
        # 描述: 获取东方财富网-数据中心-特色数据-商誉-A股商誉市场概况
        common.insert_db(data, "ak_a_goodwill_market_appearance", False, "报告期")

    except Exception as e:
        print("error :", e)


# 商誉专题-商誉减值预期明细
def stock_em_sy_yq_list(tmp_datetime):
    #############################
    # 商誉专题-商誉减值预期明细
    # 描述: 获取东方财富网-数据中心-特色数据-商誉-商誉减值预期明细
    try:
        # symbol	str	Y	symbol="沪市主板"; 参见网页选项
        # trade_date	str	Y	trade_date="2019-09-30"; 参见网页选项
        symbol_value = "沪市主板"
        data = ak.stock_em_sy_yq_list(symbol=symbol_value, trade_date="2020-12-31")
        data.rename(columns={"业绩变动原因": "业绩变动原因text"}, inplace=True)
        # 描述: 上海证券交易所-每日概况
        common.insert_db(data, "ak_a_goodwill_impairment_expectations_data", False, "股票代码")

    except Exception as e:
        print("error :", e)


# 个股商誉减值明细
def stock_em_sy_jz_list(tmp_datetime):
    ##########################
    # 个股商誉减值明细
    try:
        # symbol	str	Y	symbol="沪市主板"; 参见网页选项
        # trade_date	str	Y	trade_date="2019-09-30"; 参见网页选项
        symbol_value = "沪市主板"
        data = ak.stock_em_sy_jz_list(symbol=symbol_value, trade_date="2020-12-31")
        # 描述: 获取东方财富网-数据中心-特色数据-商誉-个股商誉减值明细
        common.insert_db(data, "ak_a_goodwill_impairment_data", False, "股票代码")
    except Exception as e:
        print("error :", e)


# 个股商誉明细
def stock_em_sy_list(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 个股商誉明细
    try:
        symbol_value = "沪市主板"
        # symbol	str	Y	symbol="沪市主板"; choice of {"沪市主板", "深市主板", "中小板", "创业板", "沪深两市"}
        # trade_date	str	Y	trade_date="2019-12-31"; 参见网页 数据日期 选项
        data = ak.stock_em_sy_list(symbol=symbol_value, trade_date="2020-12-31")
        # 描述: 获取东方财富网-数据中心-特色数据-商誉-个股商誉明细
        common.insert_db(data, "ak_a_goodwill_data", False, "股票代码")
    except Exception as e:
        print("error :", e)


# 行业商誉
def stock_em_sy_hy_list(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 行业商誉
    try:
        # trade_date	str	Y	trade_date="2019-12-31"; 参见网页的选项
        # 描述: 获取东方财富网-数据中心-特色数据-商誉-行业商誉
        data = ak.stock_em_sy_hy_list(trade_date="2020-12-31")

        common.insert_db(data, "ak_a_goodwill_industry_honor_data", False, "行业名称")
    except Exception as e:
        print("error :", e)


# main函数入口
if __name__ == '__main__':
    common.run_with_args(stock_em_sy_profile)
    common.run_with_args(stock_em_sy_yq_list)
    common.run_with_args(stock_em_sy_jz_list)
    common.run_with_args(stock_em_sy_list)
    common.run_with_args(stock_em_sy_hy_list)





