import pandas as pd


class PriceData(object):

    def __init__(self, filename):
        self.df = self.generateDF(filename)

    def generateDF(self, filename):
        orig_df = pd.read_csv(filename)
        filtered_df = orig_df.loc[(orig_df['State'] == "CA")]

        filtered_df['prices'] = filtered_df.iloc[:, 9:].agg(list, axis=1)

        columns = filtered_df.columns

        df_out = filtered_df \
            .drop(columns=columns[3:len(filtered_df.axes[1])-1]) \
            .drop(columns=columns[0:2]) \
            .rename(columns={'RegionName': 'ZipCode'}) \
            .reset_index(drop=True)

        return df_out


if __name__ == "__main__":
    # create dataframe
    df_out = PriceData('zipcode_price_dataset.csv').df
    print(df_out.head(5))
