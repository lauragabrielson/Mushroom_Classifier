import pandas as pd
import data_cat

# read secondary data as pandas.DataFrame, shuffle and write to a new CSV
data_secondary = pd.read_csv(data_cat.FILE_PATH_ALL_SECONDARY_GENERATED,
                                 sep=';', header=0, low_memory=False)
data_secondary = data_secondary.sample(frac=1, random_state=1)
data_secondary.to_csv(data_cat.FILE_PATH_ALL_SECONDARY_SHUFFLED, sep=',', index=False)
