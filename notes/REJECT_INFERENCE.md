# Reject Inference
Reject inference is a method commonly used in improving the quality of credit score card by incorporating the data from rejected loan applications.

# Why do we need Reject Inference?
Bias can result if a credit scorecard model is built only on accepted applicaants and does not account for applications rejected because of past denials for credit or unknown non default status.

# Reject Inference Methods
## 1. Simple Augmentation a.k.a. Hard Cutoff
The simplest way to include information on rejects is to evaluate them using the existing scorecard

Steps:
1. develop a score card based on the approved loan applications
1. using the resulting scorecard, we can evalute the set of rejects
1. from the rejects, we reevaluate them  as "good" or "bad", new ground truths, based on the acceptable bad rate value
1. with this we can use the rejects as training  

## 2. Parceling
Parceling is similar to Simple Augmentation, with the difference that instead of classifying all rejects at a certain score as good or bad, it assigns them in a proportion to the expected bad rate at that score.

As with simple augmentation, the initial model needs to be good, since it is the only thing being used to allocate the ground truth.

Additionally, business sense would suggest that since the proportion of goods and basds in the rejects cannot be the same as that of the approved (rejects should be worse), a conservative approach requires assigning a higher proportion of rejects as bad in each interval (a bad rate multiplicative factor)

## 3. Fuzzy Augmentation
Each reject is used twice in the final model

The rejected application is broken into two components, a partial good and a partial bad.

If the estimated bad rate from the initial model gives a probability of being bad of 30% on a rejected loan, then the loan will have a sample weight of 0.30 as being bad, and a sample weight of 0.70 as being good.


By using the reject inference method, you can infer the performance of rejects and include them in your credit scorecard model to remedy this bias
# Reference
- https://www.mathworks.com/help/risk/reject-inference-for-credit-scorecards.html#:~:text=Reject%20inference%20is%20a%20method,credit%20or%20unknown%20nondefault%20status.
- https://www.kdnuggets.com/2012/07/scorto-reject-inference-methods.html
- https://plug-n-score.com/learning/how-to-apply-reject-inference-methods.htm
- https://medium.com/@hjdlopes/should-we-reject-reject-inference-an-empirical-study-4f1e5d86bcf4
