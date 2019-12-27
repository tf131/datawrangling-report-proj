import pandas as pd
from dupl_calc import google_places_api_quality_v2
from dupl_calc import here_quality_of_linking

# df_dpl = pd.read_csv("../data/restaurants_DPL.tsv", sep='\t')
# df_ndpl = pd.read_csv("../data/restaurants_NDPL.tsv", sep='\t')
# df_dpl_google = google_places_api_quality_of_linking.get_dpl_df()
# df_dpl_here = here_quality_of_linking.get_dpl_df()
df_ndpl_google = google_places_api_quality_of_linking.get_all_permutations2()
#
# def calculate_precision(df, df_gold):
#     counter_TP = 0
#     for index, data in df.iterrows():
#         for index2, data2 in df_gold.iterrows():
#             if data.equals(data2):
#                 counter_TP += 1
#
#     FN = 0
#     tp_and_fp = len(df)
#     return counter_TP / tp_and_fp
#
# def calculate_recall(df, df_gold):
#     counter_TP = 0
#     for index, data in df.iterrows():
#         for index2, data2 in df_gold.iterrows():
#             if data.equals(data2):
#                 counter_TP += 1
#                 ###
#     tp_and_fn = counter_TP
#     return counter_TP
#
#
#
# print(calculate_precision(df_dpl_google, df_dpl))
# print(calculate_precision(df_dpl_here, df_dpl))
