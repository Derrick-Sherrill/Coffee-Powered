import pandas as pd

# concat two series
# concat series to df
# concat two dataframes

excel_df = pd.read_excel('wb.xlsx')
print(excel_df)
###
python_series_a = pd.Series([1,2,3,4,5], index=[1,2,3,4,5], name='Python Series 1')
python_series_b = pd.Series([6,7,8,9,10], index=[4,5,6,7,8], name='Python Series 2')

two_series_df_0 = pd.concat([python_series_a, python_series_b], axis=0) #along index
print(two_series_df_0)

two_series_df_1 = pd.concat([python_series_a, python_series_b], axis=1) # along column names
print(two_series_df_1, type(two_series_df_1))

two_series_df_2 = pd.concat([python_series_b, python_series_a], axis=1) #Order Important
print(two_series_df_2)

new_df_from_two_dfs = pd.concat([two_series_df_1, excel_df], axis=1) #join = outer by default
print(new_df_from_two_dfs)


new_df_with_keys = pd.concat([two_series_df_1, excel_df], axis=1, keys=['key1','key2'])
print(new_df_with_keys)

print(new_df_with_keys['key1'])
