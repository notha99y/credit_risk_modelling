"""
Useful helper functions to calculate WoE and IV
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set()


def woe_discrete(df, discrete_variabe_name, good_bad_variable_df):
    df = pd.concat([df[discrete_variabe_name], good_bad_variable_df], axis=1)
    df = pd.concat(
        [
            df.groupby(df.columns.values[0], as_index=False)[
                df.columns.values[1]
            ].count(),
            df.groupby(df.columns.values[0], as_index=False)[
                df.columns.values[1]
            ].mean(),
        ],
        axis=1,
    )
    df = df.iloc[:, [0, 1, 3]]
    df.columns = [df.columns.values[0], "n_obs", "prop_good"]
    df["prop_n_obs"] = df["n_obs"] / df["n_obs"].sum()
    df["n_good"] = df["prop_good"] * df["n_obs"]
    df["n_bad"] = (1 - df["prop_good"]) * df["n_obs"]
    df["prop_n_good"] = df["n_good"] / df["n_good"].sum()
    df["prop_n_bad"] = df["n_bad"] / df["n_bad"].sum()
    df["WoE"] = np.log(df["prop_n_good"] / df["prop_n_bad"])
    df = df.sort_values(["WoE"])
    df = df.reset_index(drop=True)
    df["diff_prop_good"] = df["prop_good"].diff().abs()
    df["diff_WoE"] = df["WoE"].diff().abs()
    df["IV"] = (df["prop_n_good"] - df["prop_n_bad"]) * df["WoE"]
    df["IV"] = df["IV"].sum()
    return df


def woe_ordered_continuous(df, discrete_variabe_name, good_bad_variable_df):
    df = pd.concat([df[discrete_variabe_name], good_bad_variable_df], axis=1)
    df = pd.concat(
        [
            df.groupby(df.columns.values[0], as_index=False)[
                df.columns.values[1]
            ].count(),
            df.groupby(df.columns.values[0], as_index=False)[
                df.columns.values[1]
            ].mean(),
        ],
        axis=1,
    )
    df = df.iloc[:, [0, 1, 3]]
    df.columns = [df.columns.values[0], "n_obs", "prop_good"]
    df["prop_n_obs"] = df["n_obs"] / df["n_obs"].sum()
    df["n_good"] = df["prop_good"] * df["n_obs"]
    df["n_bad"] = (1 - df["prop_good"]) * df["n_obs"]
    df["prop_n_good"] = df["n_good"] / df["n_good"].sum()
    df["prop_n_bad"] = df["n_bad"] / df["n_bad"].sum()
    df["WoE"] = np.log(df["prop_n_good"] / df["prop_n_bad"])
    # df = df.sort_values(['WoE'])
    # df = df.reset_index(drop = True)
    df["diff_prop_good"] = df["prop_good"].diff().abs()
    df["diff_WoE"] = df["WoE"].diff().abs()
    df["IV"] = (df["prop_n_good"] - df["prop_n_bad"]) * df["WoE"]
    df["IV"] = df["IV"].sum()
    return df


def plot_by_woe(df_WoE, rotation_of_x_axis_labels=0):
    x = np.array(df_WoE.iloc[:, 0].apply(str))
    y = df_WoE["WoE"]
    plt.figure(figsize=(18, 6))
    plt.plot(x, y, marker="o", linestyle="--", color="k")
    plt.xlabel(df_WoE.columns[0])
    plt.ylabel("Weight of Evidence")
    plt.title(str("Weight of Evidence by " + df_WoE.columns[0]))
    plt.xticks(rotation=rotation_of_x_axis_labels)
