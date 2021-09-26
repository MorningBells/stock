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
import json

import MySQLdb

# 基本面分析 专栏


# 基本面数据-财务报表()
def stock_financial_report_sina(tmp_datetime):
    #############################
    try:
        symbols = ["资产负债表", "利润表", "现金流量表"]
        stock_value = "600004"
        for symbol_value in symbols:
            # stock	str	Y	stock="600004"; 股票代码
            # symbol	str	Y	symbol="现金流量表"; choice of {"资产负债表", "利润表", "现金流量表"}
            data = ak.stock_financial_report_sina(symbol=symbol_value, stock=stock_value)
            # 描述: 获取新浪财经-财务报表-三大报表
            symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])
            stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])

            stable_data = pd.DataFrame(data, columns=["报表日期", "单位"])
            stable_data = stable_data.reset_index()

            json_result = data.to_json(orient='index')
            dict_json = json.loads(json_result)

            for key, value in dict_json.items():
                dict_json[key] = json.dumps(value, ensure_ascii=False)

            json_data = pd.DataFrame.from_dict(dict_json, orient='index', columns=['详情text'])
            text_data = json_data.reset_index()
            # text_data = pd.DataFrame(json_data, columns=["详情text"])

            new_data = pd.concat([symbol, stock, stable_data, text_data], axis=1)

            common.insert_db(new_data, "ak_a_fundamental_financial_statements", False, "`symbol`,`stock`,`报表日期`")

    except Exception as e:
        print("error :", e)


# 基本面数据-财务摘要()
def stock_financial_abstract(tmp_datetime):
    #############################
    # 新浪财经-财务报表-财务摘要
    try:
        stock_value = "600004"
        # stock	str	Y	stock="600004"; 股票代码
        data = ak.stock_financial_abstract(stock=stock_value)
        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])
        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_financial_summary", False, "`stock`,`截止日期`")
    except Exception as e:
        print("error :", e)


# 基本面数据-财务指标()
def stock_financial_analysis_indicator(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-财务分析-财务指标
    try:
        stock_value = "600004"
        # stock	str	Y	stock="600004"; 股票代码
        data = ak.stock_financial_analysis_indicator(stock=stock_value)

        data = data.reset_index()
        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])
        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_financial_indicators", False, "`stock`,`index`", varchar_length=100)
    except Exception as e:
        print("error :", e)


# 基本面数据-历史分红()
def stock_history_dividend(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-发行与分配-历史分红
    try:
        data = ak.stock_history_dividend()
        data = data.reset_index()

        common.insert_db(data, "ak_a_fundamental_historical_dividend", False, "`代码`,`index`", varchar_length=100)
    except Exception as e:
        print("error :", e)


# 基本面数据-股东户数()
def stock_zh_a_gdhs(tmp_datetime):
    #############################
    # 描述: 获取东方财富网-数据中心-特色数据-股东户数数据
    try:
        data = ak.stock_zh_a_gdhs()
        data = data.reset_index()

        common.insert_db(data, "ak_a_fundamental_shareholders_number", False, "`代码`,`index`", varchar_length=100)
    except Exception as e:
        print("error :", e)


# 基本面数据-分红配股()
def stock_history_dividend_detail(tmp_datetime):
    #############################
    # 描述: 获取东方财富网-数据中心-特色数据-股东户数数据
    try:
        indicator_value = "分红"
        stock_value = "600012"
        date_value = "2021-08-24"
        # indicator	str	Y	indicator="配股"; choice of {"分红", "配股"}
        # stock	str	Y	stock="600012"; 股票代码
        # date	str	Y	date="1994-12-24"; 分红配股的具体日期, e.g., "1994-12-24"
        data = ak.stock_history_dividend_detail(indicator=indicator_value, stock=stock_value, date=date_value)
        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([stock, indicator, date, data], axis=1)

        new_data = new_data.drop_duplicates(subset="item", keep='first', inplace=False)

        common.insert_db(new_data, "ak_a_fundamental_dividend_rights_offering", False, "`stock`,`indicator`,`date`,`item`")
    except Exception as e:
        print("error :", e)


# 基本面数据-新股发行()
def stock_ipo_info(tmp_datetime):
    #############################
    # 描述: 获取东方财富网-数据中心-特色数据-股东户数数据
    try:
        stock_value = "600012"
        # stock	str	Y	stock="600004"; 股票代码
        data = ak.stock_ipo_info(stock=stock_value)
        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])
        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_new_shares_issued", False, "`stock`,`item`")
    except Exception as e:
        print("error :", e)


# 基本面数据-股票增发()
def stock_add_stock(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-发行与分配-增发
    try:
        stock_value = "688166"
        # stock	str	Y	stock="600004"; 股票代码
        data = ak.stock_add_stock(stock=stock_value)
        # if "无增发记录" in data:
        if isinstance(data, str):
            print(data, "跳过处理")
            return

        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])

        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_stock_issuance", False, "stock")
    except Exception as e:
        print("error :", e)


# 基本面数据-限售解禁()()
def stock_restricted_shares(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-发行分配-限售解禁
    try:
        stock_value = "688166"
        # stock	str	Y	stock="600004"; 股票代码
        data = ak.stock_restricted_shares(stock=stock_value)
        data = data.reset_index()
        # if "无增发记录" in data:
        if isinstance(data, str):
            print(data, "跳过处理")
            return

        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])

        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_sales_ban_lifting", False, "`stock`,`index`")
    except Exception as e:
        print("error :", e)


# 基本面数据-流通股东()
def stock_circulate_stock_holder(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股东股本-流通股东
    try:
        stock_value = "688166"
        # stock	str	Y	stock="600004"; 股票代码
        data = ak.stock_circulate_stock_holder(stock=stock_value)
        data = data.reset_index()
        # if "无增发记录" in data:
        if isinstance(data, str):
            print(data, "跳过处理")
            return

        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])

        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_circulation_shareholders", False, "`stock`,`index`")
    except Exception as e:
        print("error :", e)


# 基本面数据-板块行情()()
def stock_sector_spot(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股东股本-流通股东
    try:
        indicator_value = "新浪行业"
        # indicator	str	Y	indicator="新浪行业"; choice of {"新浪行业", "启明星行业", "概念", "地域", "行业"}
        data = ak.stock_sector_spot(indicator=indicator_value)
        # data = data.reset_index()
        # if "无增发记录" in data:
        if isinstance(data, str):
            print(data, "跳过处理")
            return

        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])

        new_data = pd.concat([indicator, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_plate_market", False, "`indicator`,`label`,`板块`")
    except Exception as e:
        print("error :", e)


# 基本面数据-板块详情()
def stock_sector_detail(tmp_datetime):
    #############################
    # 描述: 获取新浪行业-板块行情-成份详情, 由于新浪网页提供的统计数据有误, 部分行业数量大于统计数
    try:
        sector_value = "new_mtc"
        # sector	str	Y	sector="hangye_ZL01"; 通过 stock_sector_spot 返回数据的 label 字段选择 sector
        data = ak.stock_sector_detail(sector=sector_value)
        # data = data.reset_index()
        # if "无增发记录" in data:
        if isinstance(data, str):
            print(data, "跳过处理")
            return

        sector = pd.DataFrame([sector_value for _ in range(len(data))], columns=["sector"])

        new_data = pd.concat([sector, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_plate_details", False, "`sector`,`symbol`")
    except Exception as e:
        print("error :", e)



# 基本面数据-股票列表(A股、上证、两网以及退市)()
# def stock_info_sh_name_code(tmp_datetime):
#     #############################
#     # 描述: 获取新浪行业-板块行情-成份详情, 由于新浪网页提供的统计数据有误, 部分行业数量大于统计数
#     try:
#         sector_value = "new_mtc"
#         # sector	str	Y	sector="hangye_ZL01"; 通过 stock_sector_spot 返回数据的 label 字段选择 sector
#         data = ak.stock_info_sh_name_code(sector=sector_value)
#         # data = data.reset_index()
#         # if "无增发记录" in data:
#         if isinstance(data, str):
#             print(data, "跳过处理")
#             return
#
#         sector = pd.DataFrame([sector_value for _ in range(len(data))], columns=["sector"])
#
#         new_data = pd.concat([sector, data], axis=1)
#
#         common.insert_db(new_data, "ak_a_fundamental_stocks_list", False, "`sector`,`symbol`")
#     except Exception as e:
#         print("error :", e)


# 基本面数据-基金持股()
def stock_fund_stock_holder(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        stock_value = "600004"
        # stock	str	Y	stock="600004"; 股票代码
        data = ak.stock_fund_stock_holder(stock=stock_value)
        data = data.reset_index()
        # if "无增发记录" in data:
        if isinstance(data, str):
            print(data, "跳过处理")
            return

        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])

        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_fund_holding", False, "`stock`,`index`,`基金名称`")
    except Exception as e:
        print("error :", e)


# 基本面数据-基金持股明细()
def stock_report_fund_hold_detail(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        symbol_value = "005827"
        date_value = "2021-06-30"
        # symbol	str	Y	symbol="005827"; 基金代码
        # date	str	Y	date="20200630"; 财报发布日期, xxxx-03-31, xxxx-06-30, xxxx-09-30, xxxx-12-31
        data = ak.stock_report_fund_hold_detail(symbol=symbol_value, date=date_value)
        # if "无增发记录" in data:
        if isinstance(data, str):
            print(data, "跳过处理")
            return

        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])

        new_data = pd.concat([symbol, date, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_fund_holding_detail", False, "`symbol`,`date`,`序号`")
    except Exception as e:
        print("error :", e)


# 基本面数据-主要股东()
def stock_main_stock_holder(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        stock_value = "600004"
        # stock	str	Y	stock="600004"; 股票代码
        data = ak.stock_main_stock_holder(stock=stock_value)
        data = data.reset_index()
        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])

        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_main_shareholders", False, "`stock`,`index`")
    except Exception as e:
        print("error :", e)


# 基本面数据-机构持股-机构持股一览表()
def stock_institute_hold(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        quarter_value = "20211"
        # quarter	str	Y	quarter="20051"; 从 2005 年开始, {"一季报":1, "中报":2 "三季报":3 "年报":4}, e.g., "20191", 其中的 1 表示一季报; "20193", 其中的 3 表示三季报;
        data = ak.stock_institute_hold(quarter=quarter_value)
        quarter = pd.DataFrame([quarter_value for _ in range(len(data))], columns=["quarter"])

        new_data = pd.concat([quarter, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_institutional_holdings_list", False, "`quarter`,`证券代码`")
    except Exception as e:
        print("error :", e)


# 基本面数据-机构持股-机构持股详情()
def stock_institute_hold_detail(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        quarter_value = "20211"
        stock_value = "300003"
        # stock	str	Y	stock="300003"; 股票代码
        # quarter	str	Y	quarter="20201"; 从 2005 年开始, {"一季报":1, "中报":2 "三季报":3 "年报":4}, e.g., "20191", 其中的 1 表示一季报; "20193", 其中的 3 表示三季报;
        data = ak.stock_institute_hold_detail(quarter=quarter_value, stock=stock_value)
        quarter = pd.DataFrame([quarter_value for _ in range(len(data))], columns=["quarter"])
        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])

        new_data = pd.concat([quarter, stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_institutional_holdings_details", False, "`quarter`,`stock`,`持股机构代码`")
    except Exception as e:
        print("error :", e)


# 基本面数据-机构推荐-机构推荐池()
def stock_institute_recommend(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        indicators = {'最新投资评级', '上调评级股票', '下调评级股票', '股票综合评级', '首次评级股票', '目标涨幅排名', '机构关注度', '行业关注度', '投资评级选股'}
        for indicator_value in indicators:
            # indicator	str	Y	indicator="行业关注度"; choice of {'最新投资评级', '上调评级股票', '下调评级股票', '股票综合评级', '首次评级股票', '目标涨幅排名', '机构关注度', '行业关注度', '投资评级选股'}
            data = ak.stock_institute_recommend(indicator=indicator_value)
            json_result = data.to_json(orient='index')
            dict_json = json.loads(json_result)

            for key, value in dict_json.items():
                dict_json[key] = json.dumps(value, ensure_ascii=False)

            json_data = pd.DataFrame.from_dict(dict_json, orient='index', columns=['详情text'])
            text_data = json_data.reset_index()


            indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])

            new_data = pd.concat([indicator, text_data], axis=1)

            common.insert_db(new_data, "ak_a_fundamental_institutional_recommendation_pool", False, "`indicator`,`index`")

    except Exception as e:
        print("error :", e)


# 基本面数据-机构推荐-股票评级记录()
def stock_institute_recommend_detail(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        stock_value = "300003"
        # stock	str	Y	stock="300003"; 股票代码
        data = ak.stock_institute_recommend_detail(stock=stock_value)
        data = data.reset_index()
        stock = pd.DataFrame([stock_value for _ in range(len(data))], columns=["stock"])

        new_data = pd.concat([stock, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_institutional_recom_stock_rating_records", False, "`stock`,`index`,`股票代码`")
    except Exception as e:
        print("error :", e)


# 基本面数据-机构推荐-投资评级)
def stock_rank_forecast_cninfo(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        date_value = "20210910"
        # date	str	date="20210910"; 交易日
        data = ak.stock_rank_forecast_cninfo(date=date_value)
        data = data.reset_index()
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])

        new_data = pd.concat([date, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_institutional_recom_investment_rating", False, "`date`,`index`,`证券代码`")
    except Exception as e:
        print("error :", e)


# 基本面数据-机构推荐-行业市盈率()
def stock_industry_pe_ratio_cninfo(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        date_value = "20210910"
        symbol_value = "证监会行业分类"
        # symbol	str	symbol="证监会行业分类"; choice of {"证监会行业分类", "国证行业分类"}
        # date	str	date="20210910"; 交易日
        data = ak.stock_industry_pe_ratio_cninfo(date=date_value, symbol=symbol_value)
        data = data.reset_index()
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, date, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_institutional_recomm_industry_p_e_ratio", False, "`symbol`,`date`,`index`")
    except Exception as e:
        print("error :", e)


# 基本面数据-机构推荐-新股过会()
def stock_new_gh_cninfo(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        data = ak.stock_new_gh_cninfo()
        data = data.reset_index()

        common.insert_db(data, "ak_a_fundamental_institutional_recom_new_shares_held", False, "`公司名称`,`上会日期`,`index`")
    except Exception as e:
        print("error :", e)


# 基本面数据-机构推荐-新股发行()
def stock_new_ipo_cninfo(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        data = ak.stock_new_ipo_cninfo()
        data = data.reset_index()

        common.insert_db(data, "ak_a_fundamental_institutional_recom_new_shares_issued", False, "`证劵代码`,`index`")
    except Exception as e:
        print("error :", e)


# 基本面数据-券商业绩报告()
def stock_em_qsjy(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        trade_date_value = "2021-01-01"
        # trade_date
        data = ak.stock_em_qsjy(trade_date=trade_date_value)
        data = data.reset_index()

        trade_date = pd.DataFrame([trade_date_value for _ in range(len(data))], columns=["trade_date"])
        new_data = pd.concat([trade_date, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_brokerage_performance_report", False, "`trade_date`,`index`")
    except Exception as e:
        print("error :", e)

# 基本面数据-A股市盈率()
def stock_a_pe(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        market_value = "000016.XSHG"
        # market	str	Y	market="000016.XSHG"; 参见 stock_a_pe 一览表
        # stock_a_pe 一览表
        #
        # 栏目	参数
        # 上证A股市盈率	sh
        # 深圳A股市盈率	sz
        # 中小板市盈率	zx
        # 创业板市盈率	cy
        # 科创板市盈率	kc
        # 全部A股市盈率-平均数-中位数	all
        # 沪深300市盈率	000300.XSHG
        # 上证50市盈率	000016.XSHG
        # 上证180市盈率	000010.XSHG
        # 上证380市盈率	000009.XSHG
        # 中证流通市盈率	000902.XSHG
        # 中证100市盈率	000903.XSHG
        # 中证500市盈率	000905.XSHG
        # 中证800市盈率	000906.XSHG
        # 中证1000市盈率	000852.XSHG
        data = ak.stock_a_pe(market=market_value)
        data = data.reset_index()
        data = data.rename(columns={"close": "close_value"})


        market = pd.DataFrame([market_value for _ in range(len(data))], columns=["market"])
        new_data = pd.concat([market, data], axis=1)

        new_data["自增序列"] = range(1, len(new_data)+1)

        common.insert_db(new_data, "ak_a_fundamental_a_share_pe_ratio", False, "`market`,`date`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-A股市净率()
def stock_a_pb(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        market_value = "000016.XSHG"
        # market	str	Y	market="000016.XSHG"; 参见 stock_a_pe 一览表
        # stock_a_pb 一览表
        #
        # 栏目	参数
        # 上证A股市净率	sh
        # 深圳A股市净率	sz
        # 中小板市净率	zx
        # 创业板市净率	cy
        # 沪深300市净率	000300.XSHG
        # 上证50市净率	000016.XSHG
        # 上证180市净率	000010.XSHG
        # 上证380市净率	000009.XSHG
        # 中证流通市净率	000902.XSHG
        # 中证100市净率	000903.XSHG
        # 中证500市净率	000905.XSHG
        # 中证800市净率	000906.XSHG
        # 中证1000市净率	000852.XSHG
        data = ak.stock_a_pb(market=market_value)
        data = data.reset_index()

        market = pd.DataFrame([market_value for _ in range(len(data))], columns=["market"])
        new_data = pd.concat([market, data], axis=1)

        new_data["自增序列"] = range(1, len(new_data)+1)

        common.insert_db(new_data, "ak_a_fundamental_a_share_market_net_rate", False, "`market`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-A股个股指标()
def stock_a_lg_indicator(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        market_value = "000016.XSHG"

        data = ak.stock_a_lg_indicator(market=market_value)
        data = data.reset_index()

        market = pd.DataFrame([market_value for _ in range(len(data))], columns=["market"])
        new_data = pd.concat([market, data], axis=1)

        new_data["自增序列"] = range(1, len(new_data)+1)

        common.insert_db(new_data, "ak_a_fundamental_a_share_stock_index", False, "`market`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-A股等权重与中位数市盈率()
def stock_a_ttm_lyr(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:

        data = ak.stock_a_ttm_lyr()
        data["自增序列"] = range(1, len(data)+1)

        common.insert_db(data, "ak_a_fundamental_a_share_equal_weight_and_median_pe_ratio", False, "`date`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-A股等权重与中位数市净率()
def stock_a_all_pb(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:

        data = ak.stock_a_all_pb()
        data["自增序列"] = range(1, len(data)+1)

        common.insert_db(data, "ak_a_fundamental_a_shareEqualWeight_medianMarketToMarket_ratio", False, "`date`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-创新高与新低的股票数量()
def stock_a_high_low_statistics(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        market_value = "all"
        # market	str	Y	market="all"; {"all": "全部A股", "sz50": "上证50", "hs300": "沪深300", "zz500": "中证500"}
        data = ak.stock_a_high_low_statistics(market_value)
        data["自增序列"] = range(1, len(data)+1)

        market = pd.DataFrame([market_value for _ in range(len(data))], columns=["market"])
        new_data = pd.concat([market, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_new_highs_and_new_low_number_of_stocks", False, "`market`,`date`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-破净股统计()
def stock_a_below_net_asset_statistics(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        symbol_value = "全部A股"
        # symbol	str	symbol="全部A股"; choice of {"全部A股", "沪深300"}
        data = ak.stock_a_below_net_asset_statistics(symbol_value)
        data["自增序列"] = range(1, len(data)+1)

        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])
        new_data = pd.concat([symbol, data], axis=1)

        common.insert_db(new_data, "ak_a_fundamental_net_stock_statistics", False, "`symbol`,`date`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-首发申报信息()
def stock_ipo_declare(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        data = ak.stock_ipo_declare()
        data["自增序列"] = range(1, len(data)+1)

        common.insert_db(data, "ak_a_fundamental_first_declaration_information", False, "`序号`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-注册制审批-科创板()
def stock_register_kcb(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        data = ak.stock_register_kcb()
        data["自增序列"] = range(1, len(data)+1)

        common.insert_db(data, "ak_a_fundamental_registration_examination_science_board", False, "`序号`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-注册制审批-创业板()
def stock_register_cyb(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        data = ak.stock_register_cyb()
        data["自增序列"] = range(1, len(data)+1)

        common.insert_db(data, "ak_a_fundamental_registration_examination_entrepreneurship_ship", False, "`序号`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-注册制审批-达标企业()
def stock_register_db(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        data = ak.stock_register_db()
        data["自增序列"] = range(1, len(data)+1)

        common.insert_db(data, "ak_a_fundamental_registration_examination_standard_enterprises", False, "`序号`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-增发()
def stock_em_qbzf(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        data = ak.stock_em_qbzf()
        data["自增序列"] = range(1, len(data)+1)

        common.insert_db(data, "ak_a_fundamental_additional_issuance", False, "`股票代码`,`自增序列`")
    except Exception as e:
        print("error :", e)


# 基本面数据-配股()
def stock_em_pg(tmp_datetime):
    #############################
    # 描述: 获取新浪财经-股本股东-基金持股
    try:
        data = ak.stock_em_pg()
        data["自增序列"] = range(1, len(data)+1)

        common.insert_db(data, "ak_a_fundamental_rights_offering", False, "`股票代码`,`自增序列`")
    except Exception as e:
        print("error :", e)



# main函数入口
if __name__ == '__main__':
    # common.run_with_args(stock_financial_report_sina)
    # common.run_with_args(stock_financial_abstract)
    # common.run_with_args(stock_financial_analysis_indicator)
    # common.run_with_args(stock_history_dividend)
    # common.run_with_args(stock_zh_a_gdhs)
    # 报错了，数据问题 common.run_with_args(stock_history_dividend_detail)
    # common.run_with_args(stock_ipo_info)
    # common.run_with_args(stock_add_stock)
    # common.run_with_args(stock_restricted_shares)
    # common.run_with_args(stock_circulate_stock_holder)
    # common.run_with_args(stock_sector_spot)
    # common.run_with_args(stock_sector_detail)

    # 基本面数据-股票列表(A股、上证、两网以及退市)() 先不做 common.run_with_args(stock_info_sh_name_code)

    # common.run_with_args(stock_fund_stock_holder)
    # common.run_with_args(stock_report_fund_hold_detail)
    # common.run_with_args(stock_main_stock_holder)
    # common.run_with_args(stock_institute_hold)
    # common.run_with_args(stock_institute_hold_detail)
    # common.run_with_args(stock_institute_recommend)
    # common.run_with_args(stock_institute_recommend_detail)
    # common.run_with_args(stock_rank_forecast_cninfo)
    # common.run_with_args(stock_industry_pe_ratio_cninfo)
    # common.run_with_args(stock_new_gh_cninfo)
    # common.run_with_args(stock_new_ipo_cninfo)
    # 返回数据有误 common.run_with_args(stock_em_qsjy)
    # common.run_with_args(stock_a_pe)
    # common.run_with_args(stock_a_pb)
    # common.run_with_args(stock_a_ttm_lyr)
    # common.run_with_args(stock_a_all_pb)
    # common.run_with_args(stock_a_high_low_statistics)
    # common.run_with_args(stock_a_below_net_asset_statistics)
    # common.run_with_args(stock_ipo_declare)
    # common.run_with_args(stock_register_kcb)
    # common.run_with_args(stock_register_cyb)
    common.run_with_args(stock_register_db)
    common.run_with_args(stock_em_qbzf)
    common.run_with_args(stock_em_pg)



