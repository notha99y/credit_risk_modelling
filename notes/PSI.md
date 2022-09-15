# Population Stability Index (PSI)
PSI is a measure of how much a population has shifted over time.

It does this by bucketing the two distributions and comparing the percents of items in each of the buckets, resulting in a single number you can used to understand how different the two populations are.

Common interpretations of PSI are:
- $<0.1$: no signficant population change
- $0.1 <= \text{PSI} < 0.2$: moderate population change
- $>= 0.2$: significant population change

# PSI Formula
$$\text{PSI} = \sum((\text{Actual Perc} - \text{Expected Perc}) \times \ln(\frac{\text{Actual Perc}}{\text{Expected Perc}}))$$
