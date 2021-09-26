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


# main函数入口
if __name__ == '__main__':
    common.run_with_args(stock_fund_flow_individual)





