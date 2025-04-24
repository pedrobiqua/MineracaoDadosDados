from ucimlrepo import fetch_ucirepo
import pandas as pd

# from ucimlrepo import fetch_ucirepo

# # fetch dataset
# poker_hand = fetch_ucirepo(id=158)

# # data (as pandas dataframes)
# X = poker_hand.data.features
# y = poker_hand.data.targets

# # metadata
# # print(poker_hand.metadata)

# # # variable information
# # print(poker_hand.variables)

# print(X)

# fetch dataset
bank_marketing = fetch_ucirepo(id=222)

# data (as pandas dataframes)
X: pd.DataFrame = bank_marketing.data.features
y: pd.DataFrame = bank_marketing.data.targets

print(X)
print(y)
