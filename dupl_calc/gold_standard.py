import pandas as pd
from dupl_calc import google_places_api_quality_of_linking
from dupl_calc import here_quality_of_linking

df_dpl = pd.read_csv("../data/restaurants_DPL.tsv", sep='\t')
df_ndpl = pd.read_csv("../data/restaurants_NDPL.tsv", sep='\t')
df_dpl_google = google_places_api_quality_of_linking.get_dpl_df()
df_dpl_here = here_quality_of_linking.get_dpl_df()


def dataframe_difference(df1, df2, which="both"):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2,
                              indicator=True,
                              how='outer')
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    return diff_df

resdf = dataframe_difference(df_dpl, df_dpl_google)
