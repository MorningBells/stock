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

# 数据分析 专栏


# 赚钱效益分析
def stock_market_activity_legu(tmp_datetime):
    #############################
    try:
        data = ak.stock_market_activity_legu()
        # 描述: 乐咕乐股网-赚钱效应分析数据
        # 涨跌比：即沪深两市上涨个股所占比例，体现的是市场整体涨跌，占比越大则代表大部分个股表现活跃。
        # 涨停板数与跌停板数的意义：涨停家数在一定程度上反映了市场的投机氛围。当涨停家数越多，则市场的多头氛围越强。真实涨停是非一字无量涨停。真实跌停是非一字无量跌停。
        common.insert_db(data, "ak_a_analyse_benefits", False, "item")
    except Exception as e:
        print("error :", e)


# 调查平均持仓
def stock_average_position_legu(tmp_datetime):
    #############################
    # 描述: 乐咕乐股网-调查平均持仓数据; 该数据近期未更新
    # 目前仓位调查的数据来源是通过微信公众号在每周最后一个交易日投票获得，并在下个交易日前公布，希望朋友们关注公众号积极参与，公众号在最下方可见，获取的数据直接公布在本页面上，所有用户均可使用。
    # 持仓调查的数据是市场参与者心理、行为表现的结果。 市场行为会因为交易规则、政策面消息、媒体噪声等因素的变化而变化。 若排除以上因素，在稳定、可重复的博弈环境下，市场行为的历史数据对于判断市场阶段、拐点有一定的参考价值。
    # 声明：仓位调查得到的结论也未见得正确，持仓调查数据的结果，虽在过往的时间中显示出了一定的规律，但对市场的判断、具体交易决策，此数据只能作为一种数据工具，参考要素之一。
    try:
        data = ak.stock_average_position_legu()
        common.insert_db(data, "ak_a_analyse_average_position", False, "日期")

    except Exception as e:
        print("error :", e)


# 资讯数据-每日快讯
def stock_zh_a_alerts_cls(tmp_datetime):
    ##########################
    # 描述：财联社-快讯数据
    try:
        data = ak.stock_zh_a_alerts_cls()
        data.rename(columns={"快讯信息": "快讯信息text"}, inplace=True)

        common.insert_db(data, "ak_a_analyse_daily_information_data", False, "时间")
    except Exception as e:
        print("error :", e)


# 一致行动人
def stock_em_yzxdr(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-一致行动人
    try:
        # date	str	Y	date="20200930"; 每年的季度末时间点
        data = ak.stock_em_yzxdr(date="20210630")
        common.insert_db(data, "ak_a_analyse_concerted_action_man", False, "序号")
    except Exception as e:
        print("error :", e)


# 盈利预测
def stock_profit_forecast(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-研究报告-盈利预测
    try:
        data = ak.stock_profit_forecast()

        common.insert_db(data, "ak_a_analyse_profit_forecast", False, "序号")
    except Exception as e:
        print("error :", e)


# 股票热度
def stock_wc_hot_rank(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 问财-热门股票排名数据
    try:
        # date	str	date="20210218"; 查询日期
        data = ak.stock_wc_hot_rank(date="20210808")

        common.insert_db(data, "ak_a_analyse_stock_heat", False, "序号")
    except Exception as e:
        print("error :", e)


# 盘口异动
def stock_changes_em(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富-行情中心-盘口异动数据
    try:
        symbol_value = "火箭发射"
        # symbol	str	Y	symbol="大笔买入"; choice of {'火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', '有大买盘', '竞价上涨', '高开5日线', '向上缺口', '60日新高', '60日大幅上涨', '加速下跌', '高台跳水', '大笔卖出', '封跌停板', '打开涨停板', '有大卖盘', '竞价下跌', '低开5日线', '向下缺口', '60日新低', '60日大幅下跌'}
        data = ak.stock_changes_em(symbol=symbol_value)
        symbol = pd.DataFrame([symbol_value for _ in range(len(data))], columns=["symbol"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_analyse_plate_rim_movement", False, "`时间`,`symbol`, `代码`")
    except Exception as e:
        print("error :", e)


# 两市停复牌
def stock_em_tfp(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-两市停复牌
    try:
        date_value = "20200325"
        # date	str	date="20200325"
        data = ak.stock_em_tfp(date=date_value)
        data = data.reset_index()
        symbol = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])

        new_data = pd.concat([symbol, data], axis=1)
        common.insert_db(new_data, "ak_a_analyse_stopped_trading", False, "`序号`,`date`")
    except Exception as e:
        print("error :", e)


# 股票账户统计-股票账户统计月度()
def stock_em_account(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-股票账户统计
    try:
        data = ak.stock_em_account()

        common.insert_db(data, "ak_a_analyse_stock_Account_statistics_monthly", False, "数据日期")
    except Exception as e:
        print("error :", e)


# 分析师指数-分析师指数最新排名)
def stock_em_analyst_rank(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-研究报告-东方财富分析师指数-东方财富分析师指数最新排行
    try:
        year_value = "2020"
        # year	str	Y	year='2020'; 从 2015 年至今
        data = ak.stock_em_analyst_rank(year=year_value)

        year = pd.DataFrame([year_value for _ in range(len(data))], columns=["year"])

        new_data = pd.concat([year, data], axis=1)

        common.insert_db(new_data, "ak_a_analyse_analyst_index_latest_ranking", False, "`year`,`序号`")
    except Exception as e:
        print("error :", e)


# 分析师指数-分析师详情()
def stock_em_analyst_detail(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-研究报告-东方财富分析师指数-分析师详情
    try:
        analyst_id_value = "11000257131"
        indicator_value = "最新跟踪成分股"
        # analyst_id	str	Y	analyst_id="11000257131"; 分析师ID, 从 stock_em_analyst_rank 获取
        # indicator	str	Y	indicator="最新跟踪成分股"; 从 {"最新跟踪成分股", "历史跟踪成分股", "历史指数"} 中选择一个
        data = ak.stock_em_analyst_detail(analyst_id=analyst_id_value, indicator=indicator_value)
        analyst_id = pd.DataFrame([analyst_id_value for _ in range(len(data))], columns=["analyst_id"])
        indicator = pd.DataFrame([indicator_value for _ in range(len(data))], columns=["indicator"])
        new_data = pd.concat([analyst_id, indicator, data], axis=1)
        common.insert_db(new_data, "ak_a_analyse_analyst_details", False, "`analyst_id`,`indicator`,`序号`")
    except Exception as e:
        print("error :", e)


# 千股千评)
def stock_em_comment(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-千股千评
    try:
        data = ak.stock_em_comment()
        common.insert_db(data, "ak_a_analyse_thousand_comments", False, "序号")
    except Exception as e:
        print("error :", e)


# 企业社会责任()
def stock_zh_a_scr_report(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取企业社会责任数据
    try:
        year_value = 2021
        # report_year	int	Y	需要获取的年份, e.g. report_year=2018
        # page	int	Y	需要具体的年份的第几页, e.g. page=1
        data = ak.stock_zh_a_scr_report(report_year=year_value, page=1)
        year = pd.DataFrame([year_value for _ in range(len(data))], columns=["year"])
        new_data = pd.concat([year, data], axis=1)
        common.insert_db(new_data, "ak_a_analyse_corporate_social_responsibility", False, "`year`,`股票名称`")
    except Exception as e:
        print("error :", e)


# 机构调研统计()
def stock_em_jgdy_tj(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 东方财富网-数据中心-特色数据-机构调研-机构调研统计
    try:
        data = ak.stock_em_jgdy_tj()
        data.rename(columns={"接待人员": "接待人员text"}, inplace=True)
        common.insert_db(data, "ak_a_analyse_institutional_research_statistics", False, "序号")
    except Exception as e:
        print("error :", e)


# 机构调研详细()
def stock_em_jgdy_detail(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 东方财富网-数据中心-特色数据-机构调研-机构调研详细
    try:
        data = ak.stock_em_jgdy_detail()
        data = data.reset_index()
        # data.rename(columns={"接待人员": "接待人员text"}, inplace=True)
        common.insert_db(data, "ak_a_analyse_institutional_research_details", False, "序号")
    except Exception as e:
        print("error :", e)


# 股权质押市场()
def stock_em_gpzy_profile(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-股权质押-股权质押市场概况
    try:
        data = ak.stock_em_gpzy_profile()
        common.insert_db(data, "ak_a_analyse_equity_pledge_market", False, "交易日期")
    except Exception as e:
        print("error :", e)


# 上市公司质押比例()
def stock_em_gpzy_pledge_ratio(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-股权质押-股权质押市场概况
    try:
        trade_date_value = "2020-08-14"
        # trade_date	str	Y	trade_date="2020-08-14"; 请访问 http://data.eastmoney.com/gpzy/pledgeRatio.aspx 查询具体交易日
        data = ak.stock_em_gpzy_pledge_ratio(trade_date=trade_date_value)
        trade_date = pd.DataFrame([trade_date_value for _ in range(len(data))], columns=["trade_date"])
        new_data = pd.concat([trade_date, data], axis=1)
        common.insert_db(new_data, "ak_a_analyse_companies_pledge_ratio", False, "`trade_date`,`股票代码`")
    except Exception as e:
        print("error :", e)


# 重要股东股权质押明细()
def stock_em_gpzy_pledge_ratio_detail(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 东方财富网-数据中心-特色数据-股权质押-重要股东股权质押明细
    try:
        data = ak.stock_em_gpzy_pledge_ratio_detail()
        common.insert_db(data, "ak_a_analyse_important_shareholders_pledge_details", False, "序号")
    except Exception as e:
        print("error :", e)


# 质押公司分布统计证券公司()
def stock_em_gpzy_distribute_statistics_company(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-证券公司
    try:
        data = ak.stock_em_gpzy_distribute_statistics_company()
        common.insert_db(data, "ak_a_analyse_securities_companies_distribution_statistics", False, "质押公司股票代码")
    except Exception as e:
        print("error :", e)


# 质押公司分布统计银行()
def stock_em_gpzy_distribute_statistics_bank(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-银行
    try:
        data = ak.stock_em_gpzy_distribute_statistics_bank()
        common.insert_db(data, "ak_a_analyse_bank_pledge_company_distribution_statistics", False, "质押公司股票代码")
    except Exception as e:
        print("error :", e)


# 上市公司质押比例()
def stock_em_gpzy_industry_data(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-股权质押-上市公司质押比例-行业数据
    try:
        data = ak.stock_em_gpzy_industry_data()
        common.insert_db(data, "ak_a_analyse_industry_pledge_ratio", False, "统计时间")
    except Exception as e:
        print("error :", e)


# 高管持股-股东增减持()
def stock_em_ggcg(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-股权质押-上市公司质押比例-行业数据
    try:
        data = ak.stock_em_ggcg()
        data = data.reset_index()
        common.insert_db(data, "ak_a_analyse_executive_holding_shareholders_increase_decrease", False, "`代码`,`index`,`股东名称`,`公告日`")
    except Exception as e:
        print("error :", e)


# 高管持股-分红配送()
def stock_em_fhps(tmp_datetime):
    datetime_str = (tmp_datetime).strftime("%Y-%m-%d")
    datetime_int = (tmp_datetime).strftime("%Y%m%d")
    print("datetime_str:", datetime_str)
    print("datetime_int:", datetime_int)
    ##########################
    # 描述: 获取东方财富网-数据中心-特色数据-股权质押-上市公司质押比例-行业数据
    try:
        date_value = "20201231"
        # date	str	Y	date="20201231"; choice of {"XXXX0630", "XXXX1231"}; 从 19901231 开始
        data = ak.stock_em_fhps(date=date_value)
        date = pd.DataFrame([date_value for _ in range(len(data))], columns=["date"])
        new_data = pd.concat([date, data], axis=1)
        common.insert_db(new_data, "ak_a_analyse_executive_holding_dividend_distribution", False, "`date`,`代码`")
    except Exception as e:
        print("error :", e)


# main函数入口
if __name__ == '__main__':
    # common.run_with_rgs(stock_market_activity_legu)
    # common.run_with_args(stock_average_position_legu)
    # common.run_with_args(stock_zh_a_alerts_cls)
    # common.run_with_args(stock_em_yzxdr)
    # common.run_with_args(stock_profit_forecast)
    # common.run_with_args(stock_wc_hot_rank)
    # common.run_with_args(stock_changes_em)
    # common.run_with_args(stock_em_tfp)
    # common.run_with_args(stock_em_account)
    # common.run_with_args(stock_em_analyst_rank)
    # common.run_with_args(stock_em_analyst_detail)
    # common.run_with_args(stock_em_comment)
    # common.run_with_args(stock_zh_a_scr_report)
    # common.run_with_args(stock_em_jgdy_tj)
    # common.run_with_args(stock_em_gpzy_profile)
    # common.run_with_args(stock_em_gpzy_pledge_ratio)
    # common.run_with_args(stock_em_gpzy_pledge_ratio_detail)
    # common.run_with_args(stock_em_gpzy_distribute_statistics_company)
    # common.run_with_args(stock_em_gpzy_distribute_statistics_bank)
    # common.run_with_args(stock_em_gpzy_industry_data)
    # common.run_with_args(stock_em_ggcg)

    common.run_with_args(stock_em_fhps)

    # 报错了 common.run_with_args(stock_em_jgdy_detail)





