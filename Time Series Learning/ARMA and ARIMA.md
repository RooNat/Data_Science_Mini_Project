---
tags: Time_Series
Module: 4
typora-copy-images-to: ./attachments
---

# ARMA, ARIMA and SARIMA

[toc]

> Reference:
>
> [1] [Choosing the best q and p from ACF and PACF plots in ARMA-type modeling](https://www.baeldung.com/cs/acf-pacf-plots-arma-modeling)
>
> [2] [Interpreting ACF and PACF Plots for Time Series Forecasting](https://towardsdatascience.com/interpreting-acf-and-pacf-plots-for-time-series-forecasting-af0d6db4061c)
>
>
> Lab:
>
> [1] [A Guide to Time Series Forecasting with ARIMA in Python 3](https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3)
>
> [2] [Time Series: Interpreting ACF and PACF](https://www.kaggle.com/code/iamleonie/time-series-interpreting-acf-and-pacf/notebook)
>
> [3] [Time Series For beginners with ARIMA](https://www.kaggle.com/code/freespirit08/time-series-for-beginners-with-arima/notebook)

## ARMA

$ARMA(p,q)$ is a combination of $AR(p)$ and $MA(q)$ models. For example, $ARMA(3,3)$ of signal the $S_t$ can be formulated as
$$
S_t=\beta_0+\beta_1S_{t-1}+\beta_2S_{t-2}+\beta_3 S_{t-3}+\epsilon_t+ \gamma_1\epsilon_{t-1}+\gamma_2\epsilon_{t-2}+\gamma_3 \epsilon_{t-3}
$$
where $\beta, \gamma$ are coefficients and $\epsilon$ is error. 



## ARIMA

> Reference: 
>
> [1] [Time Series For beginners with ARIMA](https://www.kaggle.com/code/freespirit08/time-series-for-beginners-with-arima/notebook)
>
> [2] [Introudction to ARIMA: nonseaonal models](https://people.duke.edu/~rnau/411arim.htm)
>
> [3] 

### What is ARIMA Model?

ARIMA(Auto Regressive Integrated Moving Average) is a combination of 2 models AR(Auto Regressive) & MA(Moving Average).

It has **3 hyperparameters** 

1. P(auto regressive lags),
2. d(order of differentiation),
3. Q(moving avg.)

which respectively comes from the AR, I & MA components.

The AR part is correlation between prev & current time periods. To smooth out the noise, the MA part is used. The I part binds together the AR & MA parts.

#### How to get the d value for ARIMA?

> Reference: 
>
> [1] [Quick way to find p,d,q values for ARIMA](https://analyticsindiamag.com/quick-way-to-find-p-d-and-q-values-for-arima/)
>
> [2] [How to build ARIMA Model in Python for time series forecasting?](https://www.projectpro.io/article/how-to-build-arima-model-in-python/544)

There is no such method that can tell us how much value of d will be optimal. However, the value of differencing can be optimal till 2 so we will try our time series in both. Pandas provide this option of differencing. Let’s utilize this.

```python
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})
 
# Original Series
fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.plot(data.Passengers); ax1.set_title('Original Series'); ax1.axes.xaxis.set_visible(False)
# 1st Differencing
ax2.plot(data.Passengers.diff()); ax2.set_title('1st Order Differencing'); ax2.axes.xaxis.set_visible(False)
# 2nd Differencing
ax3.plot(data.Passengers.diff().diff()); ax3.set_title('2nd Order Differencing')
plt.show()
```

![img](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230421_1682087592.png)

Here we can see how the time series has become stationary. One thing which is noticeable here is in first-order differencing we have fewer noises in the data while after 1st order there is an increase in the noise. So we can select 1st order differencing for our model. We can also verify this using an autocorrelation plot. 

```python
from statsmodels.graphics.tsaplots import plot_acf
fig, (ax1, ax2, ax3) = plt.subplots(3)
plot_acf(data.Passengers, ax=ax1)
plot_acf(data.Passengers.diff().dropna(), ax=ax2)
plot_acf(data.Passengers.diff().diff().dropna(), ax=ax3)

```

![img](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230421_1682087629.png)

**Here we can see that in second-order differencing the immediate lag has gone on the negative side, representing that in the second-order the series has become over the difference.** 

From the autocorrelation graph, we can decide if more differencing is needed. If collectively the autocorrelations, or the data point of each lag (in the horizontal axis), are positive for several consecutive lags, more differencing might be needed. Conversely, if more data points are negative, the series is over-differenced.

### Seasonality

> Reference:
>
> [1] [How to Remove Trends and Seasonality with a Difference Transform in Python](https://machinelearningmastery.com/remove-trends-seasonality-difference-transform-python/)
>
> 

#### Remove the seasonality

#### Seasonality vs. Cycles

### How to find the value of p & q for ARIMA?

#### Using ACF and PACF to choose the value of p &q

1. <u>P</u>: To figure out the **order of an AR model**, you need to **look at the PACF**.

   **We can select the order $p$ for AR($p$) model based on significant spikes from the PACF plot.** One more indication of the AR process is that the ACF plot decays more slowly.

   - **Example**:

     For instance, we can conclude from the example below that the PACF plot has significant spikes at lags 2 and 3 because of the significant PACF value. In contrast, for everything within the blue band, we don’t have evidence that it’s different from zero. Also, we could try for $p$ other values of lag that are outside of the blue belt. **To conclude, everything outside the blue boundary of the PACF plot tell us the order of the AR model:**

     ![image-20230421131002762](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230421_1682079003.png)
2. <u>Q</u>: To figure out the **order of an MA model**, you need to **look at the ACF**.

   **In contrast to the AR model, we can select the order $q$ for model MA(q) from ACF if this plot has a sharp cut-off after lag $q$**. One more indication of the MA process is that the PACF plot decays more slowly.

   - Similar to selecting $p$ for the AR model, in order to select the appropriate $q$ order for the MA model, we need to analyse all spikes higher than the blue area. In that sense, from the image below, we can try using $q=6$ or $q=3$.

     ![image-20230421131328603](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230421_1682079210.png)

#### Machine Learning Approach for Choosing p and q Order

> Sometimes it’s very hard and time expensive to find the right order of $p$ and $q$ for the ARMA model by analyzing ACF and PACF plots as we mentioned above. Therefore, there are some easier approaches where it comes to tuning this model. Today, most statistical tools have integrated functionality that is often called “auto ARIMA”.
>
> For example, in python and R, the auto ARIMA method itself will generate the optimal $p$ and $q$ parameters, which would be suitable for the data set to provide better forecasting. The high-level logic behind that is the same as the logic behind hyperparameter tuning of any other machine learning model. We need to try some combinations of $p$ and $q$ parameters and compare results using a validation set.

Since our search space is not big, usually values $p$ and $q$ are not higher than 10, we can apply a popular technique for hyperparameter optimization called **grid search**.

Grid search is simply an exhaustive search through a manually specified subset of the hyperparameter space of a learning algorithm. Basically, it means that this method will try each combination of ![p](./attachments/quicklatex.com-5faad0904f612a3fa5b27faafb8dc903_l3-20230421142306425.svg) and ![q](./attachments/quicklatex.com-420eca7b6df080cc5f01773d1978f44a_l3-20230421142306417.svg) from the specified subset that we provided.

Also, in order to find the best combination of $p$ and $q$ , we need to have some objective function that will measure model performance on a validation set.

Usually, we can use AIC and BIC for that purpose. The lower the value of these criteria, the better the model is.

1. **Akaike Information Criteria (AIC)**

   **AIC stands for Akaike Information Criteria, and it’s a statistical measure that we can use to compare different models for their relative quality.** It measures the quality of the model in terms of its goodness-of-fit to the data, its simplicity, and how much it relies on the tuning parameters. The formula for AIC is
   $$
   AIC= 2k-2l
   $$
   where $l$ is a log-likelihood, and $k$ is a number of parameters. For example, the AR($p$) model has $p+1$ parameters. From the formula above, we can conclude that AIC prefers a higher log-likelihood that indicates how strong the model is in fitting the data and a simpler model in terms of parameters.

   

2. **Bayesian Information Criteria (BIC)**

   In addition to AIC, the BIC uses one more indicator $n$ that defines **the number of samples used for fitting**. The formula for BIC is
   $$
   BIC=k \mathrm{log} n-2l
   $$



##### Cross-Validation for Time-Series

Finally, since we’re dealing with time series, we would need to utilize [appropriate validation techniques](https://www.baeldung.com/cs/train-test-datasets-ratio) for parameter tuning. This is important because we want to simulate the real-time behavior of the data flow. For instance, it wouldn’t be correct to use a data sample $x_i$ to predict data sample $x_j$ if $x_j$ comes before $x_i$ by time because in real life we can’t use information from the future to predict data in real-time.

Thus, one popular validation technique used for tuning time-series-based machine learning models is cross-validation for time-series. The goal is to see which hyperparameters of the model give the best result in sense of our selected measurement metric on the training data and then use that model for future predictions.

For example, if our data consist of five time-points, we can make a train-test split as:

- Training [1], Test [2]
- Training [1, 2], Test [3]
- Training [1, 2, 3], Test [4]
- Training [1, 2, 3, 4], Test [5]

Of course, one time-point might not be enough as the starting training set, but instead of one, we can start with $n$ starting points and follow the same logic.



## SARIMA