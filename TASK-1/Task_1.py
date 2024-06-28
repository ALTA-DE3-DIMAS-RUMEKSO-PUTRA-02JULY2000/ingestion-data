import pandas as pd

pd.set_option('display.max_columns', 18)

df = pd.read_csv("../dataset/sample.csv", sep=",", header=0, names=[
    "vendor_id","tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count",
    "trip_distance", "ratecode_id", "store_and_fwd_flag", "pulocation_id", "dolocation_id",
    "payment_type", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount",
    "improvement_surcharge", "total_amount", "congestion_surcharge"
])
print("")
print("Rename all the columns with snake_case format")
print("")
print(df)
print("-------------------------------------------------------------------------------------")

df_multiple_cols = df[["vendor_id", "passenger_count", "trip_distance", 
                       "payment_type", "fare_amount", "extra", "mta_tax", 
                       "tip_amount", "tolls_amount", "improvement_surcharge", 
                       "total_amount", "congestion_surcharge"]]
df_sorted = df_multiple_cols.sort_values(by='passenger_count', ascending=False)
print("")
print("Show only 12 selected columns and Select only 10 top of highest number of passenger_count.")
print("")
print(df_sorted.head(10))