1. 放弃Tushare，改用akshare。因为Tushare的积分制度让我望而生畏。除此之外还有Baostock和理杏仁

2. 定时拉取，拉取ak获得的数据：

#### A股基本数据(ak_shares_basic_data)
  - [x] A股-股票市场总貌(ak_a_basic_market_appearance)
  - [x] A股-证券交易所-每日概况(ak_a_basic_exchanger_daily_summary)
  - [x] A股实时行情数据(新浪、东财)(ak_a_basic_realtime_market_data)
  - [x] A股历史行情数据(新浪、东财)(ak_a_basic_history_market_data)
  - [x] A股分时数据(ak_a_basic_time_sharing_data)
  - [x] A股盘前数据(ak_a_basic_pre_disk_data)
  - [x] 历史分笔数据(腾讯、网易)(ak_a_basic_historical_calculus_data)
  - [x] A股CDR(中国存托凭证,中国存托凭证（Chinese Depository Receipt，CDR），是指由存托人签发、以境外证券为基础在中国境内发行、代表境外基础证券权益的证券。  一般来说，在境外(包含中国[香港](https://baike.baidu.com/item/香港/128775))上市公司将部分已发行上市的股票托管在当地保管银行，并发行由中国境内的存托银行发行、在境内A股市场上市、以人民币交易结算、供国内投资者买卖的投资凭证，从而实现股票的异地买卖。 2020年9月22日，证监会发布公告称，同意九号有限公司（即“九号智能”）科创板公开发行存托凭证注册。这意味着，九号智能将成为第一家通过发行CDR（中国存托凭证）的形式登陆科创板的红筹企业。)
    (ak_a_basic_cdr_data)
  - [x] 股票指数-实时行情数据(ak_a_basic_index_realtime_market_data)
  - [x] 股票指数-历史行情数据-历史行情数据(新浪/腾讯)(ak_a_basic_index_history_market_data)

#### 商誉专题

  - [x] 商誉专题-A股商誉市场概况 (ak_a_goodwill_market_appearance)
  - [x] 商誉专题-商誉减值预期明细 (ak_a_goodwill_impairment_expectations_data)
  - [x] 商誉专题-个股商誉减值明细 (ak_a_goodwill_impairment_data)
  - [x] 商誉专题-个股商誉明细 (ak_a_goodwill_data)
  - [x] 商誉专题-行业商誉 (ak_a_goodwill_industry_honor_data)



#### 股票分区

  - [x] 次新股(ak_a_partition_ipo)
  - [x] 风险警示板(ak_a_partition_st)
  - [x] 新股列表 (ak_a_partition_new)
  - [x] 两网以及退市股 (ak_a_partition_stop)
  - [x] 新股数据-打新收益率 (ak_a_partition_new_yields)
  - [x] 新股数据-新股申购与中签 (ak_a_partition_initial_public_offerings)
  - [x] 科创板-实时行情数据 (ak_a_partition_ipo_science_board_realtime_data)
  - [x] 科创板-历史行情数据 (ak_a_partition_ipo_science_board_history_data)
  - [x] 科创板公告 (ak_a_partition_ipo_science_board_history_notice)



#### 数据分析

  - [x] 赚钱效益分析(ak_a_analyse_benefits)
  - [x] 调查平均持仓(ak_a_analyse_average_position)
  - [x] 资讯数据-每日快讯(ak_a_analyse_daily_information_data)
  - 手续费-国内券商佣金
    - 以万 2.5 佣金结构为例 
      上海证券交易所
      项目	费用	收取部门
      证管费	万 0.2	由证监会收取
      经手费	万 0.487	由交易所收取
      券商收入	万 1.813	由券商收取
    - 以万 1.2 佣金结构为例
      上海证券交易所
      项目	费用	收取部门
      证管费	万 0.2	由证监会收取
      经手费	万 0.487	由交易所收取
      券商收入	万 0.513	由券商收取
  - [x] 一致行动人(ak_a_analyse_concerted_action_man)
  - [x] 盈利预测(ak_a_analyse_profit_forecast)
  - [x] 股票热度(ak_a_analyse_stock_heat)
  - [x] 盘口异动(ak_a_analyse_plate_rim_movement)
  - [x] 两市停复牌(ak_a_analyse_stopped_trading)
  - [x] 股票账户统计-股票账户统计月度(ak_a_analyse_stock_Account_statistics_monthly)
  - [x] 分析师指数-分析师指数最新排名(ak_a_analyse_analyst_index_latest_ranking)
  - [x] 分析师指数-分析师详情(ak_a_analyse_analyst_details)
  - [x] 千股千评(ak_a_analyse_thousand_comments)
  - [x] 企业社会责任(ak_a_analyse_corporate_social_responsibility)
  - [x] 机构调研统计(ak_a_analyse_institutional_research_statistics)
  - [x] 机构调研详细(ak_a_analyse_institutional_research_details)
  - [x] 股权质押市场(ak_a_analyse_equity_pledge_market)
  - [x] 上市公司质押比例(ak_a_analyse_companies_pledge_ratio)
  - [x] 重要股东股权质押明细(ak_a_analyse_important_shareholders_pledge_details)
  - [x] 质押公司分布统计证券公司(ak_a_analyse_securities_companies_distribution_statistics)
  - [x] 质押公司分布统计银行(ak_a_analyse_bank_pledge_company_distribution_statistics)
  - [x] 上市公司质押比例_行业数据(ak_a_analyse_industry_pledge_ratio)
  - [x] 高管持股-股东增减持(ak_a_analyse_executive_holding_shareholders_increase_decrease)
  - [x] 高管持股-分红配送(ak_a_analyse_executive_holding_dividend_distribution)



#### 持股统计
  - [x] 沪深港通持股-北向净流入(ak_a_holding_north_inflow)
  - [x] 沪深港通持股-北向资金余额(ak_a_holding_north_fund_balance)
  - [x] 沪深港通持股-北向累计净流入(ak_a_holding_north_accumulated_inflow)
  - [x] 沪深港通持股-南向净流入(ak_a_holding_south_inflow)
  - [x] 沪深港通持股-南向资金余额(ak_a_holding_south_fund_balance)
  - [x] 沪深港通持股-南向累计净流入(ak_a_holding_south_accumulated_inflow)
  - [x] 沪深港通持股-板块排行(ak_a_holding_plate_ranking)
  - [x] 沪深港通持股-个股排行(ak_a_holding_individual_ranking)
  - [x] 沪深港通持股-每日个股统计(ak_a_holding_individual_statistics_daily)
  - [x] 沪深港通持股-每日机构统计(ak_a_holding_institutional_statistics_daily)
  - [x] 沪深港通持股-沪深港通历史数据(ak_a_holding_history_data)

#### 资金流向
  - [x] 资金流向-个股资金流(ak_a_capital_flow_individual)
  - [x] 资金流向-概念资金流(ak_a_capital_flow_concept)
  - [x] 资金流向-行业资金流(ak_a_capital_flow_industry)
  - [x] 资金流向-大单追踪(ak_a_capital_flow_large_order_tracking)
  - [x] 资金流向-个股资金流排名(ak_a_capital_flow_individual_ranking)
  - [x] 资金流向-大盘资金流(ak_a_capital_flow_market)
  - [x] 资金流向-板块资金流排名(ak_a_capital_flow_plate_ranking)



#### 基本面分析
  - [x] 基本面数据-财务报表(ak_a_fundamental_financial_statements)
  - [x] 基本面数据-财务摘要(ak_a_fundamental_financial_summary)
  - [x] 基本面数据-财务指标(ak_a_fundamental_financial_indicators)
  - [x] 基本面数据-历史分红(ak_a_fundamental_historical_dividend)
  - [x] 基本面数据-股东户数(ak_a_fundamental_shareholders_number)
  - [x] 基本面数据-分红配股(ak_a_fundamental_dividend_rights_offering)
  - [x] 基本面数据-新股发行(ak_a_fundamental_new_shares_issued)
  - [x] 基本面数据-股票增发(ak_a_fundamental_stock_issuance)
  - [x] 基本面数据-限售解禁(ak_a_fundamental_sales_ban_lifting)
  - [x] 基本面数据-流通股东(ak_a_fundamental_circulation_shareholders)
  - [x] 基本面数据-板块行情(ak_a_fundamental_plate_market)
  - [x] 基本面数据-板块详情(ak_a_fundamental_plate_details)
  - [x] 基本面数据-股票列表(A股、上证、两网以及退市)(ak_a_fundamental_stocks_list)
  - [x] 基本面数据-基金持股(ak_a_fundamental_fund_holding)
  - [x] 基本面数据-基金持股明细(ak_a_fundamental_fund_holding_detail)
  - [x] 基本面数据-主要股东(ak_a_fundamental_main_shareholders)
  - [x] 基本面数据-机构持股-机构持股一览表(ak_a_fundamental_institutional_holdings_list)
  - [x] 基本面数据-机构持股-机构持股详情(ak_a_fundamental_institutional_holdings_details)
  - [x] 基本面数据-机构推荐-机构推荐池(ak_a_fundamental_institutional_recommendation_pool)
  - [x] 基本面数据-机构推荐-股票评级记录(ak_a_fundamental_institutional_recom_stock_rating_records)
  - [x] 基本面数据-机构推荐-投资评级(ak_a_fundamental_institutional_recom_investment_rating)
  - [x] 基本面数据-机构推荐-行业市盈率(ak_a_fundamental_institutional_recomm_industry_p_e_ratio)
  - [x] 基本面数据-机构推荐-新股过会(ak_a_fundamental_institutional_recom_new_shares_held)
  - [x] 基本面数据-机构推荐-新股发行(ak_a_fundamental_institutional_recom_new_shares_issued)
  - [x] 基本面数据-券商业绩报告(ak_a_fundamental_brokerage_performance_report)
  - [x] 基本面数据-A股市盈率(ak_a_fundamental_a_share_pe_ratio)
  - [x] 基本面数据-A股市净率(ak_a_fundamental_a_share_market_net_rate)
  - [x] 基本面数据-A股个股指标(ak_a_fundamental_a_share_stock_index)
  - [x] 基本面数据-A股等权重与中位数市盈率(ak_a_fundamental_a_share_equal_weight_and_median_pe_ratio)
  - [x] 基本面数据-A股等权重与中位数市净率(ak_a_fundamental_a_shareEqualWeight_medianMarketToMarket_ratio)
  - [x] 基本面数据-创新高与新低的股票数量(ak_a_fundamental_new_highs_and_new_low_number_of_stocks)
  - [x] 基本面数据-破净股统计(ak_a_fundamental_net_stock_statistics)
  - [x] 基本面数据-首发申报信息(ak_a_fundamental_first_declaration_information)
  - [x] 基本面数据-注册制审批-科创板(ak_a_fundamental_registration_examination_science_board)
  - [x] 基本面数据-注册制审批-创业板(ak_a_fundamental_registration_examination_entrepreneurship_ship)
  - [x] 基本面数据-注册制审批-达标企业(ak_a_fundamental_registration_examination_standard_enterprises)
  - [x] 基本面数据-增发(ak_a_fundamental_additional_issuance)
  - [x] 基本面数据-配股(ak_a_fundamental_rights_offering)


#### 龙虎榜
  - [ ] 龙虎榜-营业厅排名-上榜次数最多(ak_a_topBrands_business_hall_ranking_most_on_list)
  - [ ] 龙虎榜-营业厅排名-资金实力最强(ak_a_topBrands_business_hall_ranking_strongest_financial_strength)
  - [ ] 龙虎榜-营业厅排名-抱团操作实力(ak_a_topBrands_business_hall_ranking_group_operation_strength)
  - [ ] 龙虎榜-每日详情(ak_a_topBrands_daily_details)
  - [ ] 龙虎榜-个股上榜统计(ak_a_topBrands_individual_statistics)
  - [ ] 龙虎榜-营业上榜统计(ak_a_topBrands_business_hall_statistics)
  - [ ] 龙虎榜-机构席位追踪(ak_a_topBrands_institutional_seat_tracking)
  - [ ] 龙虎榜-机构席位成交明细(ak_a_topBrands_institutional_seat_transaction_details)


#### 年报季报

  - [ ] 年报季报-业绩报表(ak_a_annual_quarterly_report_performance_statements)
  - [ ] 年报季报-业绩快报(ak_a_annual_quarterly_report_performance_express)
  - [ ] 年报季报-业绩预告(ak_a_annual_quarterly_report_performance_forecast)
  - [ ] 年报季报-预计披露时间(ak_a_annual_quarterly_report_expected_disclosure_time)
  - [ ] 年报季报-资产负债表(ak_a_annual_quarterly_report_balance_sheet)
  - [ ] 年报季报-利润表(ak_a_annual_quarterly_report_profit_statement)
  - [ ] 年报季报-现金流量表(ak_a_annual_quarterly_report_cash_flow)



#### 涨停板

  - [ ] 涨停板行情-涨停股池(ak_a_raising_limit_pool)
  - [ ] 涨停板行情-昨日涨停板股池(ak_a_raising_limit_yesterday)
  - [ ] 涨停板行情-强势股池(ak_a_raising_limit_strong_pool)
  - [ ] 涨停板行情-次新股池(ak_a_raising_limit_ipo_pool)
  - [ ] 涨停板行情-炸板股池(ak_a_raising_limit_fried_plate)
  - [ ] 涨停板行情-跌停股池(ak_a_raising_limit_limit_down)




3. 定时分析
  - [ ] 指定股票去进行分析
  - [ ] 自动选择要分析的股票
  - [ ] 自动剔除不再分析的股票
  - [ ] 自动选择要演算的股票
  - [ ] 自动剔除要演算的股票
  - [ ] 记录演算的操作步骤
 

4. 地量见地价
5. 天量见天价

    1. 一些基本概念
      # 股票数据复权
            # 1.为何要复权：由于股票存在配股、分拆、合并和发放股息等事件，会导致股价出现较大的缺口。 若使用不复权的价格处理数据、计算各种指标，将会导致它们失去连续性，且使用不复权价格计算收益也会出现错误。 为了保证数据连贯性，常通过前复权和后复权对价格序列进行调整。
            # 2.前复权：保持当前价格不变，将历史价格进行增减，从而使股价连续。 前复权用来看盘非常方便，能一眼看出股价的历史走势，叠加各种技术指标也比较顺畅，是各种行情软件默认的复权方式。 这种方法虽然很常见，但也有两个缺陷需要注意。
            # 2.1 为了保证当前价格不变，每次股票除权除息，均需要重新调整历史价格，因此其历史价格是时变的。 这会导致在不同时点看到的历史前复权价可能出现差异。
            # 2.2 对于有持续分红的公司来说，前复权价可能出现负值。
            # 3.后复权：保证历史价格不变，在每次股票权益事件发生后，调整当前的股票价格。 后复权价格和真实股票价格可能差别较大，不适合用来看盘。 其优点在于，可以被看作投资者的长期财富增长曲线，反映投资者的真实收益率情况。
            # 4.在量化投资研究中普遍采用后复权数据。

      # 看盘技巧
       # 1）、在上午开盘时成交量急速放大，且形态较好的个股.可仿分时图谱即时买进。不放量不买！
       # 2）、涨幅榜前20位的同类强势个股。可寻机买进。（板块）
       # 3）、今天继续强势的昨日强势股。可逢低买入。强者恒强原则！
       # 4）、低开后平稳上涨且有大手笔成交股。可随机买进。
       # 5）、尾盘进入60分钟涨幅排名榜（前20名）个股。可今买明卖。
       # 6）、盘中涨幅不多而突然放量上涨的个股。可及时买进。
       # 7）、炒股票要紧盯热点。买就买热点原则！
       # 8）、对于那些首次进入成交量排行榜，股价又涨的股票须有进货的考虑；对于那些首次进入成交量排行榜，股价又跌的股票应有出货的考虑。
       # 9）、开盘大幅低开后，走高至涨停(特别在大盘不太强时),可仿分时图谱进出.
       # 10）、每周第一天收盘往往与本周周线收盘相吻合，即同阴阳。
       # 11）、每月第一天收盘往往与月线收盘相吻合，即同阴阳。
       # 12）、上午不论何因停盘的股票，复盘后只要不涨停立即卖掉（无论好坏消息）
       # 13）、第一天出现“小猫钓鱼”走势，可大胆跟进并持有，但一旦钓鱼反抽卖掉。要斩就早斩.要追就早追.犹豫不决.股市大忌逢高不出货、套牢不斩仓、热点转移不换手、才解套来又被套，亏损股民共有特性！ （此乃多数） 对股民来说最危险的事情莫过于企盼狂跌中的股票不会再下跌了（事实还跌）个股异动预示底部临近； 板块轮涨表明已可建仓；疯狂拉升注定结束！
       # 14）、在上午临收盘时成交稀少且弱于大盘走势的个股，应逢高了结。
       # 15）、昨日上涨前20名，而今日弱势调整的个股，说明庄家实力较弱，应退出为上。
       # 16）、高开低走且有大手笔成交的个股。必须即时卖出。
       # 17）、尾盘进入60分钟跌幅榜的个股，必须先卖掉，恐有利空。
       # 18）、在强势时，可在周初重仓，而在周末轻仓，并养成一种习惯。但在敏感区域必须空仓。初进末结！
       # 19）、在弱势时，可在周中小仓,而在周末平仓，并养成一种习惯。（最好不要全仓。逆市有险！）
       # 20）、在平势时，可在周一小仓，而在周中平仓，并养成一种习惯。（最好不要全仓。逆市有险！）
       # 21）、每次个股大涨之后的第二天上午10时30分以前5浪不板出货.特别在平衡市中见利即出。
       # 22）、股市易在每日下午14：30分后开始出现大波动，买卖须在此时观察清楚后再采取行动！最后一分钟买入，风险只有一分钟。
       # 23）、应付股市的突然变化，唯一的方法就是果断斩仓。（要有壮士断臂精神！）
       # 24）、中国股市只要大幅高开先出总没错！特别具有下列情形更应注意：
       # 25）、大盘跌的时候，内盘大于外盘会下跌，而且两者差异愈悬殊则跌幅愈大。
       # 26）、当第一个跌停板出现以后要有警觉心，特别同板块的股票应做先行出脱的考虑。
       # 27）、当个股即将触及跌停板前，应先做最坏的打算(即先出来),不可有反弹回生的幻想。
       # 28）、以上两条出现跌停的股票如若是龙头或领涨股，则必须不打折扣立即逃跑。涨跌停板具有极强的传染性。
       # 29）、带量冲关之后如被拉回，必跌幅不浅（尤其弱市）。挑顶卖货！
       # 30）、高开低走、并均价线向下，反抽必卖。只因会形成乌云盖顶！饿狼扑食！
       # 注：何为乌云盖顶？只要盖过昨日收盘价就是，也就是说高开后不可补当日缺口.
       # 31）、高开高走不涨停，先卖掉。
       # 32）、分时走势图中出现数次急跌拉回，小心庄家向买盘出货。深水炸弹！也称下跌脉冲。
       # 33）、分时走势图中出现冲高回落走势并于上午伴有较大成交量，只要不涨停，五浪或拐头时先出货。翻山越岭！（即全天走势如同翻过一座大山一样，前市上山、后市下山）
       # 34）、当股价跌破前一天涨停板价时，说明前一天的涨停毫无意义，就是最后一棒！
       # 35）、炒股：不需要什么提前预测，也不需要到处打听消息，只要看懂了盘面，就能轻轻松松逃顶和抄底.盘面反映一切！
       # 36）、在相对高位区，“事故多发地带”股民应采取“一看二慢三通过”和“宁等三分不抢一秒”及“卖要坚决、买要谨慎、割肉要狠、止损要快”的策略！
    
    # 涨跌比：即沪深两市上涨个股所占比例，体现的是市场整体涨跌，占比越大则代表大部分个股表现活跃。
    # 涨停板数与跌停板数的意义：涨停家数在一定程度上反映了市场的投机氛围。当涨停家数越多，则市场的多头氛围越强。真实涨停是非一字无量涨停。真实跌停是非一字无量跌停。
  - # 所谓无量涨停板,指的是涨停当日成交量非常小,日换手率低于5%。一般来说,无量涨停中换手率越小越好,低于1%是最佳状态,不过在实际操作中,低于5%也算“无量”,起码不能超过10%。
    # 一般来说,无量涨停的后市上涨空间巨大,需高度关注,并随时准备在后市震荡中介入。
    # 放量涨停具体就是指，在股价涨停的情况下或者是过程中，成交量相对于一般的情况出现了明显的波动，放出了非常巨大的量。

    * 什么是南向北向资金
      * 北向资金，就是从南方来的资金，通常指通过香港市场流入A股的资金，也就是所谓外资。南向资金，自然是南下流入香港市场的资金了。 
      * 在股市中，“南”代表中国香港，“北”代表中国大陆。从沪港通衍生出来的概念。香港买沪市叫北上，沪市买香港叫南下。 
      * 2019年8月19日，北向资金净流入84.83亿元，为今年以来北向资金第六大单日净流入规模。同时，近期央行披露数据显示，北向资金占外资持股比例达63.71%。 
      * 值得注意的是，二季度末境外机构和个人持有境内股票16473.00亿元，较一季度末的16838.88亿元减少365.88亿元。此外，二季度大盘呈下跌态势，北向资金整体出现净流出，不过持股市值不降反升，在一定程度上也体现出北向资金的选股能力。
      * 中国大陆资本流动是受到管制不是自由流动的，但是香港的资本流动是自由流动的，人民币升值期间会有很多香港资金和国际资金通过各种非正常渠道进入内地，博取人民币升值的收益。
    * 什么是炸板
      * 炸板是一种口语化的表达，指的是股票封死涨停板后又有大量抛单把价格又打下来，把封板给炸了，这种现象就叫炸板。通常炸板对于股市来说是一件坏事，因为炸板有可能预示着这个股票会有利空。 
      * 值得一提的是，在股市中，涨停也被称作为打板，例如当一只股票涨停了，就会说这只股票打板了，跌停则称为砸板。