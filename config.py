
# config.py

import os

# General Configurations
TRIGGER_FOLDER = os.path.join(os.getcwd(), 'data', 'trigger_folder')
PROCESSED_FOLDER = os.path.join(os.getcwd(), 'data', 'processed')
SAMPLE_OUTPUT_FOLDER = os.path.join(os.getcwd(), 'data', 'samples')
LOG_FOLDER = os.path.join(os.getcwd(), 'logs')

# Namespaces for XML parsing
NAMESPACES = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

# Database configuration
DATABASE_URI = 'sqlite:///mutual_funds.db'

# Logging configuration
LOG_FILE = "/Users/tylermontell/Projects/magic_machine_app/logs/application.log"

# Excluded characters and terms
EXCLUDED_CHARACTERS = ["©", "™", "®"]
EXCLUDED_TERMS = [
    "TM-", "Benchmark Universe", "FINRA members", "Print Date",
    "Ranked by:", "ascending", "Benchmark:", "Aggregate:", "Average:",
    "©2024 Morningstar.", "2024 Morningstar", "©2023 Morningstar.", "2023 Morningstar", "©2022 Morningstar.", "2022 Morningstar", "All Rights Reserved", "©2021 Morningstar.", "2021 Morningstar", "©2020 Morningstar.", "2020 Morningstar"
]

# Header mappings
HEADER_MAPPINGS = {

"Mid Blend": "%_mid_blend",
"Mid Growth": "%_mid_growth",
"Mid Value": "%_mid_value",
"% Africa/ Middle East": "%_africa_middle_east",
"Africa/ Middle East": "%_africa_middle_east",
"% Americas": "%_americas",
"Americas": "%_americas",
"% Asia - Developed": "%_asia_developed",
"Asia - Developed": "%_asia_developed",
"% Asia - Emerging": "%_asia_emerging",
"Asia - Emerging": "%_asia_emerging",
"% Australasia": "%_australasia",
"Australasia": "%_australasia",
"Basic Materials": "%_basic_materials",
"% Bonds Long": "%_bonds_long",
"Bonds Long": "%_bonds_long",
"% Bonds Short": "%_bonds_short",
"Bonds Short": "%_bonds_short",
"Cash & Equivalents": "%_cash",
"Cash & Equivalents %": "%_cash",
"% Cash Long": "%_cash_long",
"Cash Long": "%_cash_long",
"% Cash Short": "%_cash_short",
"Cash Short": "%_cash_short",
"Communication Services": "%_communication_services",
"Communications": "%_communication_services",
"Consumer Cyclical": "%_consumer_cyclical",
"Consumer Defensive": "%_consumer_defensive",
"Corporate": "%_corporate",
"Corporate %": "%_corporate",
"Cyclical": "%_cyclical",
"Defensive": "%_defensive",
"Derivative": "%_derivative",
"Derivative %": "%_derivative",
"Energy": "%_energy",
"% Europe - Developed": "%_europe_developed",
"Europe - Developed": "%_europe_developed",
"% Europe - Emerging": "%_europe_emerging",
"Europe - Emerging": "%_europe_emerging",
"% Financial Services": "%_fin_services",
"Financial Services": "%_fin_services",
"Government": "%_government",
"Government %": "%_government",
"% Greater Asia": "%_greater_asia",
"Greater Asia": "%_greater_asia",
"% Greater Europe": "%_greater_europe",
"Greater Europe": "%_greater_europe",
"Healthcare": "%_healthcare",
"% Japan": "%_japan",
"Japan": "%_japan",
"% Large Blend": "%_large_blend",
"Large Blend": "%_large_blend",
"% Large Growth": "%_large_growth",
"Large Growth": "%_large_growth",
"% Large Value": "%_large_value",
"Large Value": "%_large_value",
"% Latin America": "%_latin_america",
"Latin America": "%_latin_america",
"% Mid Blend": "%_mid_blend",
"% Mid Growth": "%_mid_growth",
"% Mid Value": "%_mid_value",
"Market Maturity % Developed": "%_mkt_maturity_dev",
"Market Maturity % Developed ": "%_mkt_maturity_dev",
"Maturity % Developed ": "%_mkt_maturity_dev",
"Market Maturity % Emerging": "%_mkt_maturity_emerging",
"Market Maturity % Emerging ": "%_mkt_maturity_emerging",
"Maturity % Emerging ": "%_mkt_maturity_emerging",
"Municipal": "%_municipal",
"Municipal %": "%_municipal",
"% Non-US Stocks Long": "%_non_us_stocks_long",
" Non-US Stocks Short": "%_non_us_stocks_short",
"% Non-US Stocks Short": "%_non_us_stocks_short",
"% North America": "%_north_america",
"North America": "%_north_america",
"% Other/ Not Classified Long": "%_other_not_class_long",
"Not Classified Long": "%_other_not_class_long",
"% Other/ Not Classified Short": "%_other_not_class_short",
"Not Classified Short": "%_other_not_class_short",
"Real Estate": "%_real_estate",
"Securitized": "%_securitized",
"Securitized %": "%_securitized",
"Sensitive": "%_sensitive",
"% Small Blend": "%_small_blend",
"Small Blend": "%_small_blend",
"% Small Growth": "%_small_growth",
"Small Growth": "%_small_growth",
"% Small Value": "%_small_value",
"Small Value": "%_small_value",
"% United Kingdom": "%_united_kingdom",
"United Kingdom": "%_united_kingdom",
"% US Stocks Long": "%_us_stocks_long",
"US Stocks Long": "%_us_stocks_long",
"% US Stocks Short": "%_us_stocks_short",
"US Stocks Short": "%_us_stocks_short",
"Utilities": "%_utilities",
"A": "a",
"AA": "aa",
"AAA": "aaa",
"Allocated By": "alloc_by",
"Alpha 10 Yr": "alpha_10yr",
"Alpha10": "alpha_10yr",
"Alpha 3 Yr": "alpha_3yr",
"Alpha3": "alpha_3yr",
"Alpha 5 Yr": "alpha_5yr",
"Alpha5": "alpha_5yr",
"2010": "ar_10",
"2011": "ar_11",
"2012": "ar_12",
"2013": "ar_13",
"2014": "ar_14",
"Annual Return 2014": "ar_14",
"Mkt Annl Return 2014": "ar_14",
"2015": "ar_15",
"Annual Return 2015": "ar_15",
"Mkt Annl Return 2015": "ar_15",
"2016": "ar_16",
"Annual Return 2016": "ar_16",
"Mkt Annl Return 2016": "ar_16",
"2017": "ar_17",
"Annual Return 2017": "ar_17",
"Mkt Annl Return 2017": "ar_17",
"2018": "ar_18",
"Annual Return 2018": "ar_18",
"Mkt Annl Return 2018": "ar_18",
"2019": "ar_19",
"Annual Return 2019": "ar_19",
"Mkt Annl Return 2019": "ar_19",
"2020": "ar_20",
"Annual Return 2020": "ar_20",
"Mkt Annl Return 2020": "ar_20",
"2021": "ar_21",
"Annual Return 2021": "ar_21",
"Mkt Annl Return 2021": "ar_21",
"2022": "ar_22",
"Annual Return 2022": "ar_22",
"Mkt Annl Return 2022": "ar_22",
"2023": "ar_23",
"Annual Return 2023": "ar_23",
"Mkt Annl Return 2023": "ar_23",
"Annual Report Net Expense  Ratio": "ar_net_expense",
"Asset Allocation Model": "asset_alloc_model",
"Average Coupon": "avg_coupon",
"Average Credit Quality": "avg_credit_quality",
"Average Duration": "avg_duration",
"Average Effective Duration": "avg_duration",
"Average Maturity": "avg_maturity",
"Average Quality": "avg_quality",
"Average Weighted Coupon": "avg_weighted_coupon",
"B": "b",
"BB": "bb",
"BBB": "bbb",
"Below B": "below_b",
"Benchmark": "benchmark",
"Benchmark Name": "benchmark",
"BLANK": "blank",
"Constituents  Applied": "constituents_applied",
"Created By": "created_by",
"Currency": "currency",
"Date": "date",
"Date (Mkt)": "date",
"Date Created": "date",
"Return Date (current)": "date",
"Return Date(c)": "date",
"Description": "description",
"Editable": "editable",
"Div": "est_dividend",
"Dividend": "est_dividend",
"Estimated Dividend": "m_est_dividend",
"Fund Objective": "fund_obj",
"Group": "group",
"High PR": "high_6mo_return",
"hP12R": "high_6mo_return",
"Best Case": "high_6mo_return",
"L Score": "l_score",
"Last Modified By": "last_mod_by",
"Last Modified Date/Time": "last_mod_date",
"Locked By": "locked_by",
"Locked Date/Time": "locked_date",
"Low PR": "low_6mo_return",
"lP12R": "low_6mo_return",
"Worst Case": "low_6mo_return",
"M*Risk": "m_risk_score",
"MPRS": "m_risk_score",
"Portfolio  Risk Score ": "m_risk_score",
"Portfolio Risk Score": "m_risk_score",
"Portfolio Risk  Score Date": "m_risk_score_date",
"Portfolio Risk Score Date": "m_risk_score_date",
"Category": "m_cat",
"Morningstar Category": "m_cat",
"Name": "name",
"Name ": "name",
"Portfolio Name": "name",
"security-longname": "name",
"Net Expense": "net_expense",
"Expense Ratio": "r_net_expense",
"Non-US Stocks Long": "non_us_stocks_long",
"NR/NA": "nr_na",
"Potential 12 Mo Return": "pot_12mo_return",
"Potential 6 Mo Return": "pot_6mo_return",
"P6R": "pot_6mo_return",
"Return": "pot_6mo_return",
"Projected Return": "pot_6mo_return",
"Primary Prospectus Benchmark": "prospectus_benchmark",
"Prospectus  Benchmark": "prospectus_benchmark",
"Risk Score": "r_risk_score",
"Risk Number": "r_risk_score",
"Service": "service",
"Shortname": "shortname",
"Source": "source",
"Mkt Standard Deviation 5 Yr ": "standard_dev_5yr",
"Standard Deviation 5 ": "standard_dev_5yr",
"Standard Deviation 5 Yr": "standard_dev_5yr",
"T Score": "t_score",
"Ticker": "ticker",
"security-shortname": "ticker",
"10 Year": "tot_ret_10yr",
"10Y": "tot_ret_10yr",
"10Ym": "tot_ret_10yr",
"Mkt Tot Ret 10 Yr Annlzd (mo-end)": "tot_ret_10yr",
"Mkt Tot Return 10 Yr (mo-end)": "tot_ret_10yr",
"Mkt Tot Return 10 Yr (Qtr-end)": "tot_ret_10yr",
"NAV Tot Ret 10 Yr Annlzd (Qtr-end)": "tot_ret_10yr",
"Tot Ret 10 Yr Annlzd (mo-end)": "tot_ret_10yr",
"Tot Ret 10 Yr Annlzd (Qtr-end)": "tot_ret_10yr",
"12 Month": "tot_ret_12mo",
"12M": "tot_ret_12mo",
"12Mc": "tot_ret_12mo",
"Mkt Tot Ret 12 Mo (Current)": "tot_ret_12mo",
"Mkt Tot Ret 12 Mo (mo-end)": "tot_ret_12mo",
"Mkt Tot Return 12 Mo (Qtr-end)": "tot_ret_12mo",
"NAV Tot Ret 12 Mo (Qtr-end)": "tot_ret_12mo",
"Tot Ret 12 Mo (current)": "tot_ret_12mo",
"Tot Ret 12 Mo (mo-end)": "tot_ret_12mo",
"Tot Ret 12 Mo (Qtr-end)": "tot_ret_12mo",
"15 Year": "tot_ret_15yr",
"Mkt Tot Ret 15 Yr Annlzd (mo-end)": "tot_ret_15yr",
"Mkt Tot Return 15 Yr (Qtr-end)": "tot_ret_15yr",
"NAV Tot Ret 15 Yr Annlzd (Qtr-end)": "tot_ret_15yr",
"Tot Ret 15 Yr Annlzd (mo-end)": "tot_ret_15yr",
"Tot Ret 15 Yr Annlzd (Qtr-end)": "tot_ret_15yr",
"30 Day ": "tot_ret_1mo",
"4Wc": "tot_ret_1mo",
"4Wk": "tot_ret_1mo",
"Mkt Tot Ret 1 Mo (mo-end)": "tot_ret_1mo",
"Mkt Tot Ret 4 Wk (current)": "tot_ret_1mo",
"Mkt Tot Return 1 Mo (Qtr-end)": "tot_ret_1mo",
"NAV Tot Ret 1 Mo (Qtr-end)": "tot_ret_1mo",
"Tot Ret 1 Mo (mo-end)": "tot_ret_1mo",
"Tot Ret 1 Mo (Qtr-end)": "tot_ret_1mo",
"Tot Ret 4 Wk (current)": "tot_ret_1mo",
"90 Day": "tot_ret_3mo",
"90 Day(c)": "tot_ret_3mo",
"90Dc": "tot_ret_3mo",
"Mkt Tot Ret 3 Mo (Current)": "tot_ret_3mo",
"Mkt Tot Ret 3 Mo (current) ": "tot_ret_3mo",
"Mkt Tot Ret 3 Mo (mo-end)": "tot_ret_3mo",
"Mkt Tot Return 3 Mo (Qtr-end)": "tot_ret_3mo",
"NAV Tot Ret 3 Mo (Qtr-end)": "tot_ret_3mo",
"Tot Ret 3 Mo (current)": "tot_ret_3mo",
"Tot Ret 3 Mo (mo-end)": "tot_ret_3mo",
"Tot Ret 3 Mo (Qtr-end)": "tot_ret_3mo",
"3 Year": "tot_ret_3yr",
"3Y": "tot_ret_3yr",
"3Ym": "tot_ret_3yr",
"Mkt Tot Ret 3 Yr Annlzd (mo-end)": "tot_ret_3yr",
"Mkt Tot Return 3 Yr (mo-end)": "tot_ret_3yr",
"Mkt Tot Return 3 Yr (Qtr-end)": "tot_ret_3yr",
"NAV Tot Ret 3 Yr Annlzd (Qtr-end)": "tot_ret_3yr",
"Tot Ret 3 Yr Annlzd (mo-end)": "tot_ret_3yr",
"Tot Ret 3 Yr Annlzd (Qtr-end)": "tot_ret_3yr",
"5 Year": "tot_ret_5yr",
"5Y": "tot_ret_5yr",
"5Ym": "tot_ret_5yr",
"Mkt Tot Ret 5 Yr Annlzd (mo-end)": "tot_ret_5yr",
"Mkt Tot Return 5 Yr (mo-end)": "tot_ret_5yr",
"Mkt Tot Return 5 Yr (Qtr-end)": "tot_ret_5yr",
"NAV Tot Ret 5 Yr Annlzd (Qtr-end)": "tot_ret_5yr",
"Tot Ret 5 Yr Annlzd (mo-end)": "tot_ret_5yr",
"Tot Ret 5 Yr Annlzd (Qtr-end)": "tot_ret_5yr",
"OB10": "tot_ret_diff_bmrk_10yr",
"Tot Ret +/-  Prim Bmrk 10 Yr Annlzd (mo-end)": "tot_ret_diff_bmrk_10yr",
"OB12": "tot_ret_diff_bmrk_12mo",
"Tot Ret +/-  Prim Bmrk 12 Mo (mo-end)": "tot_ret_diff_bmrk_12mo",
"OB15": "tot_ret_diff_bmrk_15yr",
"Tot Ret +/-  Prim Bmrk 15 Yr Annlzd (mo-end)": "tot_ret_diff_bmrk_15yr",
"OB30": "tot_ret_diff_bmrk_1mo",
"Tot Ret +/-  Prim Bmrk 1 Mo (mo-end)": "tot_ret_diff_bmrk_1mo",
"OB90": "tot_ret_diff_bmrk_3mo",
"Tot Ret +/-  Prim Bmrk 3 Mo (mo-end)": "tot_ret_diff_bmrk_3mo",
"OB3": "tot_ret_diff_bmrk_3yr",
"Tot Ret +/-  Prim Bmrk 3 Yr Annlzd (mo-end)": "tot_ret_diff_bmrk_3yr",
"OB5": "tot_ret_diff_bmrk_5yr",
"Tot Ret +/-  Prim Bmrk 5 Yr Annlzd (mo-end)": "tot_ret_diff_bmrk_5yr",
"OBYTD": "tot_ret_diff_bmrk_ytd",
"Tot Ret +/-  Prim Bmrk YTD (mo-end)": "tot_ret_diff_bmrk_ytd",
"Mkt Tot Ret YTD (Current)": "tot_ret_ytd",
"Mkt Tot Ret YTD (mo-end)": "tot_ret_ytd",
"Mkt Tot Return YTD (Qtr-end)": "tot_ret_ytd",
"NAV Tot Ret YTD (Qtr-end)": "tot_ret_ytd",
"Tot Ret YTD (current)": "tot_ret_ytd",
"Tot Ret YTD (mo-end)": "tot_ret_ytd",
"Tot Ret YTD (Qtr-end)": "tot_ret_ytd",
"YTD": "tot_ret_ytd",
"YTDc": "tot_ret_ytd",
"Tracking Method": "tracking_method",
"Vol": "vol",
"Stdev": "vol"
}


