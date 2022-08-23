# Feature Selection
Feature selection is a natural next step after feature creation. 

It is the process of reducing the number of input variables when developing a predictive model.

It is often desirable to perform feature selection, to reduce computation cost, improve interpretability, sometimes even resulting in better model performence.

# Linear models
For linear models, like linear regressions, logistic regression, we can consider feature selection by using the following methods.

## Weight of Evidence (WoE)
WoE value is widely used to measure the strength of a grouping for seperating good and bad risk. 

It is computed from the basic odds ratio.

$$ \text{WoE} = \ln(\frac{\text{Distr Goods}}{\text{Distr Bads}}) * 100 $$

- WoE will be 0 if the odds of  Distribution Goods / Distribution Bads is equal to 1
- if the Distribution Bads in a group is greater than the Distribution Goods, the odds ration will be < 1 and WoE will be a negative number
- if the Distribution Goods in a group is greater than the Distribution Bads, the WoE will be a positive number

The Logit transformation is simply the log of the ods, ln(P(Goods)/P(Bads)).

Therefore, by using WoE-coded predictors in logistic regression, the predictors are all prepared and coded to the same (WoE) scale, and the parameters in the logistic regression equation can be directly compared.

## Information Value (IV)
IV of a predictor is related to the sum of the absolute values of WoE over all groups

Thus, it expresses the amount of diagnostic information of a predictor variable for separating the Goods for the Bads.

Specifically, given a predictor with n groups, each with a certain Distribution of Goods and Bads, the IV for that predictor can be computed as:

$$ \text{IV} = \sum_{i-1}^{n} [(\text{Distr Goods}_{i} - \text{Distr Bads}_{i} \times \ln(\frac{\text{Distr Goods}}{\text{Distr Badss}}))] $$

Interpration of IV can be summarised as:
- < 0.02, then the predictor is not useful for modelling (sperating the Goods from the Bads)
- 0.02 - 0.1, then the predictor has a weak relationship to the Goods/Bads odds ratio
- 0.1 to 0.3, then the predictor has a medium strength relation to the Goods/Bads odds ratio
- > 0.3 then the predictor has a strong relationship to the Goods/Bads odds ratio
## Pairwise Correlation

## Variance Inflation Factor (VIF)
VIF is a measure of the amount of multicollinearity in a set of multiple regression variables.

Mathematcially, the VIF for a regression model variable is equal to the ratio of the overall model variance to the variance of a model that includes only that single independent variable.

This ratio is calculated for each independent variable.

- A high VIF indicates that the associated independent variable is highly collinear with the other variables in the model and should be removed from the model.

Detecting multicollinearity is importnat because while multicollinearity does not reduce the explanatory power of the model, it does reduce the statistical significance of the independent variables.

In a sense, it can be thought of as a kind of double-counting in the model. 

When two or more independent variables are closely related or measure almost the same thing, then the underlying effect that they measure is being accounted for twice (or more) across the variable

It becomes difficult or impossible to say which variable is really influencing the independent variable.



# Tree Based models
Tree based models like Random Forest, and Boosting are non linear algorithms and their approach to feature selections are slightly different compared to their linear cousins.

## SHAP Chart

## Feature Importance 

## Train/val/test split and binning of features

# Embedded Methods
Embedded methods use algorithms that have built in feature selection methods

```python
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression

embeded_lr_selector = SelectFromModel(LogisticRegression(penalty="l1"), max_features=num_feats)
embeded_lr_selector.fit(X_norm, y)

embeded_lr_support = embeded_lr_selector.get_support()
embeded_lr_feature = X.loc[:,embeded_lr_support].columns.tolist()
print(str(len(embeded_lr_feature)), 'selected features')
```


```python
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier

embeded_rf_selector = SelectFromModel(RandomForestClassifier(n_estimators=100), max_features=num_feats)
embeded_rf_selector.fit(X, y)

embeded_rf_support = embeded_rf_selector.get_support()
embeded_rf_feature = X.loc[:,embeded_rf_support].columns.tolist()
print(str(len(embeded_rf_feature)), 'selected features')
```
