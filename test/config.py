# config.py

# **General Configuration**

namespaces = {
    'ss': 'urn:schemas-microsoft-com:office:spreadsheet'
}

excluded_characters = ["©", "®"]

# **Report Configurations**

# The `report_configs` dictionary contains configurations for each report type.
# Each report type has:
# - 'headers': List of column headers expected in the report.
# - 'exclusions': List of phrases or words to exclude while parsing.
# - 'descriptor': Unique identifier found in the report to determine the report type.

report_configs = {
    # **Benchmark Reports**

    'bench_annual': {
        'descriptor': 'TM- BM Annual',
        'headers': [
            "Name", "Type", "Annual Return 2014", "Annual Return 2015",
            "Annual Return 2016", "Annual Return 2017", "Annual Return 2018",
            "Annual Return 2019", "Annual Return 2020", "Annual Return 2021",
            "Annual Return 2022", "Annual Return 2023"
        ],
        'exclusions': [
            "Benchmark Universe", "FINRA members", "Print Date", "Ranked by:",
            "ascending", "Benchmark:", "Aggregate:", "Average:", "©2024 Morningstar.",
            "2024 Morningstar"
        ],
    },
    'bench_compare': {
        'descriptor': 'TM- Benchmark Compare',
        'headers': [
            "Name", "Description", "Date", "Currency", "Constituents Applied",
            "Tot Ret 1 Mo (Qtr-end)", "Tot Ret 3 Mo (Qtr-end)", "Tot Ret YTD (Qtr-end)",
            "Tot Ret 12 Mo (Qtr-end)", "Tot Ret 3 Yr Annlzd (Qtr-end)",
            "Tot Ret 5 Yr Annlzd (Qtr-end)", "Tot Ret 10 Yr Annlzd (Qtr-end)",
            "Tot Ret 15 Yr Annlzd (Qtr-end)", "Standard Deviation 5 Yr",
            "Cyclical", "Sensitive", "Defensive", "Basic Materials", "Consumer Cyclical",
            "Financial Services", "Real Estate", "Communication Services", "Energy",
            "Industrials", "Technology", "Consumer Defensive", "Healthcare", "Utilities",
            "% Africa/ Middle East", "% Americas", "% North America", "% Latin America",
            "% Asia - Developed", "% Asia - Emerging", "% Australasia", "% United Kingdom",
            "% Europe - Developed", "% Europe - Emerging", "% Greater Asia", "% Greater Europe",
            "% Japan", "Market Maturity % Developed", "Market Maturity % Emerging",
            "Average Maturity", "Average Effective Duration", "Average Credit Quality",
            "Average Weighted Coupon", "AAA", "AA", "A", "BBB", "BB", "B", "Below B",
            "% Large Blend", "% Large Growth", "% Large Value", "% Mid Blend", "% Mid Growth",
            "% Mid Value", "% Small Blend", "% Small Growth", "% Small Value", "% Bonds Long",
            "% Bonds Short", "% Cash Long", "% Cash Short", "% US Stocks Long",
            "% US Stocks Short", "% Non-US Stocks Long", "% Non-US Stocks Short"
        ],
        'exclusions': [
            "Benchmark Universe", "FINRA members", "Print Date", "Ranked by:",
            "ascending", "Benchmark:", "Aggregate:", "Average:", "©2024 Morningstar.",
            "2024 Morningstar"
        ],
    },

    # **ETF Reports**

    'etf_annual': {
    'descriptor': 'TM- ETF Annual',
    'headers': [
        "Name", "Ticker", "Morningstar Category", "Mkt Annl Return 2014",
        "Mkt Annl Return 2015", "Mkt Annl Return 2016", "Mkt Annl Return 2017",
        "Mkt Annl Return 2018", "Mkt Annl Return 2019", "Mkt Annl Return 2020",
        "Mkt Annl Return 2021", "Mkt Annl Return 2022", "Mkt Annl Return 2023"
    ],
    'exclusions': [
        "US ETF Universe", "FINRA members:", "Print Date", "Ranked by:",
        "ascending", "Aggregate:", "Average:", "Benchmark:",
        "©2024 Morningstar.", "2024 Morningstar."
        ],
    },

    'etf_compare': {
        'descriptor': 'TM- ETF Compare Fund',
        'headers': [
            "Name", "Ticker", "Date (Mkt)", "Morningstar Category", "Prospectus  Benchmark",
            "Fund Objective", "Annual Report Net Expense  Ratio", "Mkt Tot Return 1 Mo (Qtr-end)",
            "Mkt Tot Return 3 Mo (Qtr-end)", "Mkt Tot Return YTD (Qtr-end)",
            "Mkt Tot Return 12 Mo (Qtr-end)", "Mkt Tot Return 3 Yr (Qtr-end)",
            "Mkt Tot Return 5 Yr (Qtr-end)", "Mkt Tot Return 10 Yr (Qtr-end)",
            "Mkt Tot Return 15 Yr (Qtr-end)", "Standard Deviation 5 Yr", "Cyclical",
            "Sensitive", "Defensive", "Basic Materials", "Consumer Cyclical",
            "Financial Services", "Real Estate", "Communication Services", "Energy",
            "Industrials", "Technology", "Consumer Defensive", "Healthcare", "Utilities",
            "% Africa/ Middle East", "% Americas", "% North America", "% Latin America",
            "% Asia - Developed", "% Asia - Emerging", "% Australasia", "% United Kingdom",
            "% Europe - Developed", "% Europe - Emerging", "% Greater Asia", "% Greater Europe",
            "% Japan", "Market Maturity % Developed", "Market Maturity % Emerging",
            "Average Maturity", "Average Effective Duration", "Average Credit Quality",
            "Average Weighted Coupon", "AAA", "AA", "A", "BBB", "BB", "B", "Below B",
            "Government %", "Corporate %", "Securitized %", "Municipal %",
            "Cash & Equivalents %", "Derivative %", "% Large Blend", "% Large Growth",
            "% Large Value", "% Mid Blend", "% Mid Growth", "% Mid Value", "% Small Blend",
            "% Small Growth", "% Small Value", "% Bonds Long", "% Bonds Short",
            "% Cash Long", "% Cash Short", "% US Stocks Long", "% US Stocks Short",
            "% Non-US Stocks Long", "% Non-US Stocks Short", "Portfolio Risk Score"
        ],
        'exclusions': [
            "Aggregate:", "Average:", "Benchmark:", "©2024 Morningstar", "2024 Morningstar"
        ],
    },
    'etf_model_compare': {
        'descriptor': 'TM- ETF Model Compare',
        'headers': [
            "Name", "Ticker", "Morningstar Category", "Date (Mkt)", "Mkt Tot Return 1 Mo (Qtr-end)",
            "Mkt Tot Return 3 Mo (Qtr-end)", "Mkt Tot Return YTD (Qtr-end)", "Mkt Tot Return 12 Mo (Qtr-end)",
            "Mkt Tot Return 3 Yr (Qtr-end)", "Mkt Tot Return 5 Yr (Qtr-end)", "Mkt Tot Return 10 Yr (Qtr-end)",
            "Mkt Tot Return 15 Yr (Qtr-end)", "Standard Deviation 5 Yr", "Average Maturity",
            "Average Effective Duration", "Average Weighted Coupon", "AAA", "AA", "A", "BBB", "BB", "B",
            "Below B", "NR/NA", "% Large Blend", "% Large Growth", "% Large Value", "% Mid Blend",
            "% Mid Growth", "% Mid Value", "% Small Blend", "% Small Growth", "% Small Value",
            "% Bonds Long", "% Bonds Short", "% Cash Long", "% Cash Short", "% US Stocks Long",
            "% US Stocks Short", "% Non-US Stocks Long", "% Non-US Stocks Short",
            "% Other/ Not Classified Long", "% Other/ Not Classified Short", "Cyclical",
            "Sensitive", "Defensive", "Basic Materials", "Consumer Cyclical", "Financial Services",
            "Real Estate", "Communication Services", "Energy", "Industrials", "Technology",
            "Consumer Defensive", "Healthcare", "Utilities", "Portfolio Risk Score"
        ],
        'exclusions': [
            "TM- Allocation ETF", "US ETF Universe", "Ranked by:", "Aggregate:", "Average:",
            "FINRA members", "Print Date", "Benchmark:", "S&P 500 TR USD", "©2024 Morningstar.",
            "2024 Morningstar."
        ],
    },

    # **Fund Reports**

    'fund_annual': {
        'descriptor': 'TM- MF Annual',
        'headers': [
            "Name", "Ticker", "Morningstar Category", "Annual Return 2014",
            "Annual Return 2015", "Annual Return 2016", "Annual Return 2017",
            "Annual Return 2018", "Annual Return 2019", "Annual Return 2020",
            "Annual Return 2021", "Annual Return 2022", "Annual Return 2023"
        ],
        'exclusions': [
            "US Mutual Fund Universe", "FINRA members:", "Print Date", "Ranked by:",
            "ascending", "Aggregate:", "Average:", "Benchmark:", "2024 Morningstar.",
            "©2024 Morningstar."
        ],
    },
    'fund_compare': {
        'descriptor': 'TM- Fund Compare',
        'headers': [
            "Name", "Ticker", "Date", "Morningstar Category", "Annual Report Net Expense  Ratio",
            "Tot Ret 1 Mo (Qtr-end)", "Tot Ret 3 Mo (Qtr-end)", "Tot Ret YTD (Qtr-end)",
            "Tot Ret 12 Mo (Qtr-end)", "Tot Ret 3 Yr Annlzd (Qtr-end)", "Tot Ret 5 Yr Annlzd (Qtr-end)",
            "Tot Ret 10 Yr Annlzd (Qtr-end)", "Tot Ret 15 Yr Annlzd (Qtr-end)", "Standard Deviation 5 Yr",
            "Cyclical", "Sensitive", "Defensive", "Basic Materials", "Consumer Cyclical",
            "Financial Services", "Real Estate", "Communication Services", "Energy", "Industrials",
            "Technology", "Consumer Defensive", "Healthcare", "Utilities", "% Africa/ Middle East",
            "% Americas", "% North America", "% Latin America", "% Asia - Developed", "% Asia - Emerging",
            "% Australasia", "% United Kingdom", "% Europe - Developed", "% Europe - Emerging",
            "% Greater Asia", "% Greater Europe", "% Japan", "Market Maturity % Developed",
            "Market Maturity % Emerging", "Average Maturity", "Average Effective Duration",
            "Average Credit Quality", "Average Weighted Coupon", "AAA", "AA", "A", "BBB", "BB", "B",
            "Below B", "Government %", "Corporate %", "Securitized %", "Municipal %",
            "Cash & Equivalents %", "Derivative %", "% Large Blend", "% Large Growth", "% Large Value",
            "% Mid Blend", "% Mid Growth", "% Mid Value", "% Small Blend", "% Small Growth", "% Small Value",
            "% Bonds Long", "% Bonds Short", "% Cash Long", "% Cash Short", "% US Stocks Long",
            "% US Stocks Short", "% Non-US Stocks Long", "% Non-US Stocks Short", "Portfolio Risk Score"
        ],
        'exclusions': [
            "US Mutual Fund Universe", "FINRA members:", "Print Date", "Ranked by:",
            "ascending", "Aggregate:", "Average:", "Benchmark:", "2024 Morningstar.",
            "©2024 Morningstar."
        ],
    },
    'fund_model_compare': {
        'descriptor': 'TM- Fund Model',
        'headers': [
            "Name", "Ticker", "Morningstar Category", "Date", "Tot Ret 1 Mo (Qtr-end)",
            "Tot Ret 3 Mo (Qtr-end)", "Tot Ret YTD (Qtr-end)", "Tot Ret 12 Mo (Qtr-end)",
            "Tot Ret 3 Yr Annlzd (Qtr-end)", "Tot Ret 5 Yr Annlzd (Qtr-end)",
            "Tot Ret 10 Yr Annlzd (Qtr-end)", "Tot Ret 15 Yr Annlzd (Qtr-end)",
            "Standard Deviation 5 Yr", "Average Maturity", "Average Effective Duration",
            "Average Weighted Coupon", "AAA", "AA", "A", "BBB", "BB", "B", "Below B",
            "NR/NA", "% Large Blend", "% Large Growth", "% Large Value", "% Mid Blend",
            "% Mid Growth", "% Mid Value", "% Small Blend", "% Small Growth", "% Small Value",
            "% Bonds Long", "% Bonds Short", "% Cash Long", "% Cash Short", "% US Stocks Long",
            "% US Stocks Short", "% Non-US Stocks Long", "% Non-US Stocks Short",
            "% Other/ Not Classified Long", "% Other/ Not Classified Short", "Cyclical",
            "Sensitive", "Defensive", "Basic Materials", "Consumer Cyclical", "Financial Services",
            "Real Estate", "Communication Services", "Energy", "Industrials", "Technology",
            "Consumer Defensive", "Healthcare", "Utilities", "Portfolio Risk Score"
        ],
        'exclusions': [
            "Aggregate:", "Average:", "Benchmark Universe", "FINRA members", "Print Date",
            "Ranked by:", "ascending", "Benchmark:"
        ],
    },

    # **Portfolio Reports**

    'model_basics': {
        'descriptor': 'Basics',
        'headers': [
            'Portfolio Name', 'Portfolio Risk Score', 'Portfolio Risk Score Date', 'Source', 
            'Editable', 'Service', 'Benchmark Name', 'Asset Allocation Model', 
            'Allocated By', 'Tracking Method', 'Created By', 'Date Created', 
            'Last Modified By', 'Last Modified Date/Time', 'Locked By', 'Locked Date/Time'
        ],
        'exclusions': [
            "FBA Mods", "Model Portfolios", "Basics", "FINRA members: For internal or institutional use only.",
            "Print Date", "Ranked by:", "ascending", "Portfolio Name", "©2024 Morningstar",
            "2024 Morningstar"
        ],
    },
    'model_compare': {
        'descriptor': 'Model Compare',
        'headers': [
            'Name', 'Return Date (current)', 'NAV Tot Ret 1 Mo (Qtr-end)', 'NAV Tot Ret 3 Mo (Qtr-end)',
            'NAV Tot Ret YTD (Qtr-end)', 'NAV Tot Ret 12 Mo (Qtr-end)', 'NAV Tot Ret 3 Yr Annlzd (Qtr-end)',
            'NAV Tot Ret 5 Yr Annlzd (Qtr-end)', 'NAV Tot Ret 10 Yr Annlzd (Qtr-end)',
            'NAV Tot Ret 15 Yr Annlzd (Qtr-end)', 'Mkt Standard Deviation 5 Yr', 'Average Maturity',
            'Average Effective Duration', 'Average Weighted Coupon', 'AAA', 'AA', 'A', 'BBB', 'BB', 'B',
            'Below B', 'NR/NA', '% Large Blend', '% Large Growth', '% Large Value', '% Mid Blend',
            '% Mid Growth', '% Mid Value', '% Small Blend', '% Small Growth', '% Small Value',
            '% Bonds Long', '% Bonds Short', '% Cash Long', '% Cash Short', '% US Stocks Long',
            '% US Stocks Short', '% Non-US Stocks Long', '% Non-US Stocks Short',
            '% Other/ Not Classified Long', '% Other/ Not Classified Short', 'Cyclical', 'Sensitive',
            'Defensive', 'Basic Materials', 'Consumer Cyclical', 'Financial Services', 'Real Estate',
            'Communication Services', 'Energy', 'Industrials', 'Technology', 'Consumer Defensive',
            'Healthcare', 'Utilities', 'Tot Ret +/-  Prim Bmrk 1 Mo (mo-end)',
            'Tot Ret +/-  Prim Bmrk 3 Mo (mo-end)', 'Tot Ret +/-  Prim Bmrk YTD (mo-end)',
            'Tot Ret +/-  Prim Bmrk 12 Mo (mo-end)', 'Tot Ret +/-  Prim Bmrk 3 Yr Annlzd (mo-end)',
            'Tot Ret +/-  Prim Bmrk 5 Yr Annlzd (mo-end)', 'Tot Ret +/-  Prim Bmrk 10 Yr Annlzd (mo-end)',
            'Tot Ret +/-  Prim Bmrk 15 Yr Annlzd (mo-end)', 'Alpha 3 Yr', 'Alpha 5 Yr', 'Alpha 10 Yr'
        ],
        'exclusions': [
            "FBA Mods", "Model Portfolios", "Basics", "FINRA members: For internal or institutional use only.",
            "Print Date", "Ranked by:", "ascending", "Portfolio Name", "©2024 Morningstar",
            "2024 Morningstar"
        ],
    },
    'model_annual': {
        'descriptor': 'Annual',
        'headers': [
            'Name', 'Morningstar Category', 'Mkt Annl Return  2014', 'Mkt Annl Return  2015',
            'Mkt Annl Return  2016', 'Mkt Annl Return  2017', 'Mkt Annl Return  2018',
            'Mkt Annl Return  2019', 'Mkt Annl Return  2020', 'Mkt Annl Return  2021',
            'Mkt Annl Return  2022', 'Mkt Annl Return  2023'
        ],
        'exclusions': [
            "FBA Mods", "Model Portfolios", "Basics", "FINRA members: For internal or institutional use only.",
            "Print Date", "Ranked by:", "ascending", "Portfolio Name", "©2024 Morningstar",
            "2024 Morningstar"
        ],
    },
}


fund_expected_columns = [
        'Name', 'Ticker', 'Morningstar Category', 'Annual Return 2014', 'Annual Return 2015', 'Annual Return 2016',
        'Annual Return 2017', 'Annual Return 2018', 'Annual Return 2019', 'Annual Return 2020', 'Annual Return 2021',
        'Annual Return 2022', 'Annual Return 2023', 'Date', 'Annual Report Net Expense  Ratio', 'Tot Ret 1 Mo (Qtr-end)', 
        'Tot Ret 3 Mo (Qtr-end)', 'Tot Ret YTD (Qtr-end)', 'Tot Ret 12 Mo (Qtr-end)', 'Tot Ret 3 Yr Annlzd (Qtr-end)', 
        'Tot Ret 5 Yr Annlzd (Qtr-end)', 'Tot Ret 10 Yr Annlzd (Qtr-end)', 'Tot Ret 15 Yr Annlzd (Qtr-end)', 
        'Standard Deviation 5 Yr', 'Cyclical', 'Sensitive', 'Defensive', "Basic Materials", "Consumer Cyclical", 
        "Financial Services", "Real Estate", "Communication Services", "Energy", "Industrials", "Technology", 
        "Consumer Defensive", "Healthcare", "Utilities", "% Africa/ Middle East", "% Americas", "% North America", 
        "% Latin America", "% Asia - Developed", "% Asia - Emerging", "% Australasia", "% United Kingdom", 
        "% Europe - Developed", "% Europe - Emerging", "% Greater Asia", "% Greater Europe", "% Japan", 
        "Market Maturity % Developed", "Market Maturity % Emerging", "Average Maturity", "Average Effective Duration", 
        "Average Credit Quality", "Average Weighted Coupon", "AAA", "AA", "A", "BBB", "BB", "B", "Below B", "NR/NA", 
        "Government %", "Corporate %", "Securitized %", "Municipal %", "Cash & Equivalents %", "Derivative %", 
        "% Large Blend", "% Large Growth", "% Large Value", "% Mid Blend", "% Mid Growth", "% Mid Value", "% Small Blend", 
        "% Small Growth", "% Small Value", "% Bonds Long", "% Bonds Short", "% Cash Long", "% Cash Short", 
        "% US Stocks Long", "% US Stocks Short", "% Non-US Stocks Long", "% Non-US Stocks Short", "Portfolio Risk Score"
]

# Expected columns for ETFs
etf_expected_columns = [
    "Name", "Ticker", "Date (Mkt)", "Morningstar Category", "Prospectus  Benchmark", "Fund Objective",
    "Annual Report Net Expense  Ratio", "Mkt Tot Return 1 Mo (Qtr-end)", "Mkt Tot Return 3 Mo (Qtr-end)", 
    "Mkt Tot Return YTD (Qtr-end)", "Mkt Tot Return 12 Mo (Qtr-end)", "Mkt Tot Return 3 Yr (Qtr-end)",
    "Mkt Tot Return 5 Yr (Qtr-end)", "Mkt Tot Return 10 Yr (Qtr-end)", "Mkt Tot Return 15 Yr (Qtr-end)", 
    "Standard Deviation 5 Yr", "Cyclical", "Sensitive", "Defensive", "Basic Materials", "Consumer Cyclical", 
    "Financial Services", "Real Estate", "Communication Services", "Energy", "Industrials", "Technology", 
    "Consumer Defensive", "Healthcare", "Utilities", "% Africa/ Middle East", "% Americas", "% North America", 
    "% Latin America", "% Asia - Developed", "% Asia - Emerging", "% Australasia", "% United Kingdom", 
    "% Europe - Developed", "% Europe - Emerging", "% Greater Asia", "% Greater Europe", "% Japan", 
    "Market Maturity % Developed", "Market Maturity % Emerging", "Average Maturity", "Average Effective Duration", 
    "Average Credit Quality", "Average Weighted Coupon", "AAA", "AA", "A", "BBB", "BB", "B", "Below B",
    "Government %", "Corporate %", "Securitized %", "Municipal %", "Cash & Equivalents %", "Derivative %", 
    "% Large Blend", "% Large Growth", "% Large Value", "% Mid Blend", "% Mid Growth", "% Mid Value", 
    "% Small Blend", "% Small Growth", "% Small Value", "% Bonds Long", "% Bonds Short", "% Cash Long", 
    "% Cash Short", "% US Stocks Long", "% US Stocks Short", "% Non-US Stocks Long", "% Non-US Stocks Short", 
    "Portfolio Risk Score", "Mkt Annl Return 2014", "Mkt Annl Return 2015", "Mkt Annl Return 2016",
    "Mkt Annl Return 2017", "Mkt Annl Return 2018", "Mkt Annl Return 2019", "Mkt Annl Return 2020", 
    "Mkt Annl Return 2021", "Mkt Annl Return 2022", "Mkt Annl Return 2023", "NR/NA", "% Other/ Not Classified Long", 
    "% Other/ Not Classified Short"
]
# **Additional Configuration**

# If you have any common exclusions or headers, you can define them here and reference in the report configs.

common_exclusions = ["Print Date", "Ranked by:", "ascending", "Aggregate:", "Average:", "©2024 Morningstar.", "2024 Morningstar"]

