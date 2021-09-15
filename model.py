import os
from env import host, user, password

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split

import sklearn.preprocessing
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_selection import SelectKBest, f_regression, RFE

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


def baseline_mean_errors(df, y):
    baseline = df[y].mean()
    base_res = df[y] - baseline
    base_res_sq = base_res**2
    SSE_baseline = base_res_sq.sum()
    MSE_baseline = SSE_baseline/len(df[y])
    RMSE_baseline = MSE_baseline**0.5
    return SSE_baseline, MSE_baseline, RMSE_baseline


def regression_errors(df, y, yhat):
    residual = df[yhat] - df[y]
    residual_sq = residual**2
    SSE = residual_sq.sum()
    ESS = ((df[yhat] - df[y].mean())**2).sum()
    TSS = SSE + ESS
    MSE = SSE/len(df[y])
    RMSE = MSE**0.5
    return SSE, ESS, TSS, MSE, RMSE

    
def k_best(scaled_df, k, target):
    # kbest
    kbest = SelectKBest(f_regression, k=k)
    kbest.fit(scaled_df, target)
    X_kbest = scaled_df.columns[kbest.get_support()]

    # recursive feature elimination
    rfe = RFE(estimator=LinearRegression(), n_features_to_select=k)
    rfe.fit(scaled_df, target)
    X_rfe = scaled_df.columns[rfe.get_support()]
    return X_kbest, X_rfe


def plot_residuals(df, y, yhat, model_name):
    plt.figure(figsize=(15,8))
    plt.title(f'Error for {model_name}')
    sns.regplot(data=df, x=y, y=df[y]-df[yhat], scatter_kws={'color':'skyblue','alpha': .55}, line_kws={'color':'red'})
    plt.axhline(df[yhat].mean(), ls = ':', color='black')
    plt.ylabel(yhat)
    plt.show()


def regression_errors(df, y, yhat):
    residual = df[yhat] - df[y]
    residual_sq = residual**2
    SSE = residual_sq.sum()
    ESS = ((df[yhat] - df[y].mean())**2).sum()
    TSS = SSE + ESS
    MSE = SSE/len(df[y])
    RMSE = MSE**0.5
    return SSE, ESS, TSS, MSE, RMSE


def better_than_baseline(df, y, yhat):
    SSE_baseline, MSE_baseline, RMSE_baseline = baseline_mean_errors(df, y)
    SSE, ESS, TSS, MSE, RMSE = regression_errors(df, y, yhat)
    return RMSE < RMSE_baseline