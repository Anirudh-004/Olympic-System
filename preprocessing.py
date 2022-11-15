import pandas as pd

def preprocess(ath_eve,regions):

    ath_eve = ath_eve[ath_eve['Season'] == 'Summer']
    ath_eve = ath_eve.merge(regions, on='NOC', how='left')
    ath_eve.drop_duplicates(inplace=True)
    ath_eve = pd.concat([ath_eve, pd.get_dummies(ath_eve['Medal'])], axis=1)
    return ath_eve