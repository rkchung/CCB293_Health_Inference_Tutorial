import pandas as pd

def mutate(df_var_eff):
    mut = pd.read_csv("data/mutation.txt", delimiter=",", na_values='-')
    return pd.concat((mut, df_var_eff), sort=True)

