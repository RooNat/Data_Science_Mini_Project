---
tags: Time_Series
Module: 1
typora-copy-images-to: ./attachments
---

# Time Series Introduction

[toc]

## Time Series

> Reference: 
>
> [1] https://www.kaggle.com/code/freespirit08/time-series-for-beginners-with-arima
>
> [2] [Time Series Forecasting Performance Measures With Python](https://machinelearningmastery.com/time-series-forecasting-performance-measures-with-python/#:~:text=The%20mean%20absolute%20error%2C%20or,is%20called%20making%20them%20absolute.)

#### What is the Time series analysis?

A. Time Series is a series of observations taken at **specified time intervals** usually equal intervals. Analysis of the series helps us to predict future values based on previously observed values. In the Time series, **we have only 2 variables, time & the variable we want to forecast.**



#### When shouldn't we use Time Series Analysis?

**A. We don't need to apply Time series in at least the following 2 cases:**

(1) The dependent variable(y) (that is supposed to vary with time)  is constant. Eq: $y=f(x)=3$ , a line parallel to the x-axis(time) will always remain the same.

(2) The dependent variable(y) represents values that can be denoted as a mathematical function. Eq: $sin(x)$ , $log(x)$ , Polynomials, etc. Thus, we can directly get value at some time using the function itself. No need for forecasting.



#### What are the components of Time Series?

**A. There are 4 components:**

(1) **Trend** - Upward and downward movement of the data with time over a large period of time. Eq: Appreciation of Dollar vs rupee.

(2) **Seasonality** - seasonal variances. Eq: Ice cream sales increase in Summer only

(3) **Noise or Irregularity** - Spikes & throughs at random intervals

(4) **Cyclicity** - behavior that repeats itself after large interval of time, like months, years etc.



## ACF and PACF

> Reference: 
>
> https://machinelearningmastery.com/gentle-introduction-autocorrelation-partial-autocorrelation/

![image-20230420220030655](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230420_1682024433.png)

These are plots that graphically summarize the strength of a relationship with an observation in a time series with observations at prior time steps. The difference between autocorrelation and partial autocorrelation can be difficult and confusing for beginners to time series forecasting.

### Autocorrelation Function(ACF)

> Direct influence+ indirect influence

We can assume the distribution of **each variable fits a Gaussian(bell curve) distribution**. If this is the case, we can use the **[Pearson's correlation coefficient](https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/)** to summarize the correlation between the variables.

>  Pearson’s correlation coefficient is a number between -1 and 1 that describes a negative or positive correlation respectively. A value of zero indicates no correlation.

We can calculate the correlation for time series observations with previous time steps, called lags. Because the correlation of the time series observations is calculated with values of the same series at previous times, this is called a serial correlation, or an autocorrelation.

A plot of the autocorrelation of a time series by lag is called the **A**uto**C**orrelation **F**unction, or the acronym ACF. This plot is sometimes called a correlogram or an autocorrelation plot.

**Function:**

```python
plot_acf()
```



### Partial Autocorrelation Function(PACF)

> Just **direct** influence

A partial autocorrelation is a summary of the relationship between an observation in a time series with observations at prior time steps with the relationships of **intervening observations removed**.

The autocorrelation for an observation and an observation at a prior time step is comprised of both the direct correlation and indirect correlations. These indirect correlations are a linear function of the correlation of the observation, with observations at intervening time steps.

It is these indirect correlations that the partial autocorrelation function seeks to remove. Without going into the math, this is the intuition for the partial autocorrelation.

**Function:**

```python
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(time_series_values, lags = 15, method = "ols")
```

*Sidenote: The default parameter for* `method` *is* `yw` *(Yule-Walker with sample-size adjustment in the denominator for acovf). However, this default value is causing some implausible autocorrelations higher than 1 on the sample data. Therefore, we change the* `method` *parameter to one that is not causing this issue.* `ywmle` *would also work fine as suggested in this StackExchange post [3].*



## Stationarity

#### What is Stationarity?

A. Before applying any statistical model to a Time Series, the series has to be stationary, which means that, <u>over different time periods</u>,

(1) It should have a **constant mean**.

(2) It should have **constant variance** or **standard deviation**.

(3) **[Auto-covariance](https://blog.quantinsti.com/autocorrelation-autocovariance/)** should not depend on time.(**There is no seasonality**)

**Trend** & **Seasonality** are two reasons why a Time Series is not stationary & hence need to be corrected.



#### Why does Time Series need to be stationary?

**A. It is because of the following reasons:**

(a) If a TS has a particular behavior over a time interval, then there's a high probability that over a different interval, it will have the same behavior, provided TS is stationary. This helps in forecasting accurately.

(b) Theories & Mathematical formulas are more mature and easier to apply for as TS which is stationary.



#### Tests to check if a series is stationary or not

A. **There are 2 ways to check for Stationary of a TS:**

(a) **Rolling Statistics** - Plot the <u>moving average</u> or <u>moving standard deviation</u> to see if it varies with time. It's a visual technique.

(b) **[ADF Test](#Augmented Dickey-Fuller Test)** - Augmented Dickey- Fuller test is used to gives us various values that can help in identifying stationarity. 

- The <u>Null hypothesis</u> says that a TS is non-stationary.
- It comprises of a **Test Statistics** and some **critical values** for some **confidence levels**. If the Test statistics is **less than the critical values**, we can reject the null hypothesis and say that the series is stationary. <u>The ADF test also gives us a p-value. According to the null hypothesis, lower values of p is better</u>.



#### How to make a time series stationary

> [How to make a time series stationary](https://analyticsindiamag.com/how-to-make-a-time-series-stationary/#:~:text=The%20statistical%20features%20of%20a,made%20stationary%20by%20differencing%20method.&text=The%20data%20which%20changes%20according,compute%20the%20hypothetical%20question%20answering.)

Suppose there is a time series:
$$
y_t= \beta_0+ \beta_1t+\varepsilon_t
$$
It seems like:

<img src="https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230420_1682027425.png" alt="image-20230420225024408" style="zoom:50%;" />

Create a new series called $Z_t$:
$$
Z_t= y_t-y_{t-1} \\
= (\beta_0+\beta_1t+\varepsilon_t)-(\beta_0+\beta_1(t-1)+\varepsilon_{t-1}) \\
= \beta_1 +(\varepsilon_t -\varepsilon_{t-1}) \to \\ 
E(z_t)= \beta_1 \\
Var(z_t) = 2k^2
$$

To detrend the time series data there are certain transformation techniques used and they are listed as follows.

- Log transforming of the data
- Taking the square root of the data
- Taking the cube root
- Proportional change

For this article uses square root transformation:

1. Use **NumPy’s square root function** to transform the required column
2. Then shift the transformation by one using the `shift` function.
3. Take the difference between both the original transformation and shift.
4. Steps 2 and 3 can be done by just using the pandas `diff` function.

```python
# Transforming the data
df_log=np.sqrt(df_use['AverageTemperature'])
df_diff=df_log.diff().dropna()
```



## Unit Roots

> Reference:
>
> [1] https://youtu.be/ugOvehrTRRw
>
> [2] https://medium.com/codex/unit-root-in-time-series-38d451d742ce

A *unit root* is a unit of measurement to determine how much stationarity a time series model has. Also called a *unit root process,* we determine the stochasticity of the model using statistical Hypothesis testing. ‘These are statistical hypothesis tests of stationarity that are designed for determining whether differencing is required.’(3) Although there is a myriad of ways to check for presence of a unit root process, I used an Augmented Dickey Fuller test.

If there is a unit root, the time series is not stationary.

We can test this using ADF test(Augmented Dickey Fuller test).

---

Unit root is **a characteristic of a time series that makes it non-stationary**. Technically speaking, a unit root is said to exist in a time series of the value of $\alpha = 1$ in the below equation.
$$
Y_t=\alpha Y_{t-1}+\beta X_e+\epsilon
$$
where, $Y_t$ is the value of the time series at time ‘t’ and $X_e$ is an **exogenous variable** (a separate explanatory variable, which is also a time series).

1. The presence of a unit root means the time series is non-stationary. 

2. Besides, the number of unit roots contained in the series corresponds to the number of differencing operations required to make the series stationary.

## Augmented Dickey-Fuller Test

> Reference: 
>
> [1] https://youtu.be/1opjnegd_hA
>
> [2] https://medium.com/codex/unit-root-in-time-series-38d451d742ce
>
> [3] https://www.machinelearningplus.com/time-series/augmented-dickey-fuller-test/

Since testing the stationarity of a time series is a frequently performed activity in autoregressive models, the ADF test along with [KPSS test](https://www.machinelearningplus.com/time-series/kpss-test-for-stationarity/) is something that you need to be fluent in when performing [time series analysis](https://www.machinelearningplus.com/time-series/time-series-analysis-python/).

Another point to remember is the ADF test is fundamentally a statistical significance test. That means, there is a **hypothesis testing** involved with a **null** and **alternate** hypothesis and as a result a test statistic is computed and [p-values](https://www.machinelearningplus.com/statistics/p-value/) get reported.

It is from the test statistic and the p-value, you can make an inference as to whether a given series is stationary or not.

### Dickey-Fuller Test

A Dickey-Fuller test is a unit root test that tests the null hypothesis that $\alpha=1$ in the following model equation. 

$\alpha$ is the coefficient of the first lag on $y$.

Null Hypothesis (H0): $\alpha=1$
$$
y_t=c+ \beta t+\alpha y_{t-1}+\phi \Delta Y_{t-1}+e_t
$$
Where,

- $y_{t-1}$= lag 1 of time series
- $\Delta Y_{t-1}$= first difference of the series at time (t-1)

Fundamentally, it has **a similar null hypothesis** as the unit root test. That is, the coefficient of $Y_{t-1}$ is 1, implying the presence of a unit root. If not rejected, the series is taken to be non-stationary.

The **Augmented Dickey-Fuller test** evolved based on the above equation and is one of the most common form of Unit Root test.

### How does Augmented Dickey Fuller(ADF) Test work?

As the name suggest, the ADF test is an ‘augmented’ version of the Dickey Fuller test.

The ADF test expands the Dickey-Fuller test equation to include high order regressive process in the model.
$$
y_t=c+\beta t+\alpha y_{t-1}+\phi_1 \Delta Y_{t-1}+\phi_2 \Delta Y_{t-2}+\cdots + \phi_p \Delta Y_{t-p}+e_t
$$
If you notice, we have only added more differencing terms, while the rest of the equation remains the same. This adds more thoroughness to the test.

The null hypothesis however is still the same as the Dickey Fuller test.

A key point to remember here is: Since the null hypothesis assumes the presence of unit root, that is $\alpha=1$, the **p-value** obtained should be less than the **significance level** (say 0.05) in order to **reject the null hypothesis**. Thereby, inferring that the series is **stationary**.



### ADF Test in Python

How to perform an Augmented Dickey-Fuller test in Python?

The `statsmodel` package provides a reliable implementation of the ADF test via the `adfuller()` function in `statsmodels.tsa.stattools`. It returns the following outputs:

1. The p-value
2. The value of the **test statistic**
3. **Number of lags** considered for the test
4. The critical value cutoffs

- When **<u>the test statistic is lower than the critical value shown</u>**, you reject the null hypothesis and infer that the time series is stationary.
- As see earlier, **the null hypothesis of the test is the presence of unit root,** that is, the series is non-stationary.

```python
# Setup and Import data
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np
%matplotlib inline

url = 'https://raw.githubusercontent.com/selva86/datasets/master/a10.csv'
df = pd.read_csv(url, parse_dates=['date'], index_col='date')
series = df.loc[:, 'value'].values
df.plot(figsize=(14,8), legend=None, title='a10 - Drug Sales Series');
```

![image-20230421101818060](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230421_1682068699.png)

The package and the data are loaded, we have everything needed to perform the test using `adfuller()` .

An optional argument the `adfuller()` accepts is the number of lags you want to consider while performing the **OLS regression**.

By default, this value is `12*(nobs/100)^{1/4}`, where `nobs` is the number of observations in the series. But, optionally you can specify either the maximum number of lags with `maxlags` parameter or let the algorithm compute the optimal number iteratively.

This can be done by setting the `autolag='AIC'`. By doing so, the `adfuller` will choose a the number of lags that yields the lowest AIC. This is usually a good option to follow.

```python
# ADF Test
result = adfuller(series, autolag='AIC')
print(result)
print(f'ADF Statistic: {result[0]}')
print(f'n_lags: {result[1]}')
print(f'p-value: {result[1]}')
for key, value in result[4].items():
    print('Critial Values:')
    print(f'   {key}, {value}')
```

![image-20230421102646447](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230421_1682069207.png)

**The p-value is obtained is greater than significance level of 0.05** and **the ADF statistic is higher than any of the critical values.**

Clearly, there is no reason to reject the null hypothesis. So, the time series is in fact non-stationary.

#### ADF Test on stationary series

Now, let's see another example of performing the test on a series of random numbers which is usually considered as stationary.

```python
# ADF test on random numbers
series = np.random.randn(100)
result = adfuller(series, autolag='AIC')
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')
for key, value in result[4].items():
    print('Critial Values:')
    print(f'   {key}, {value}')
```

![image-20230421102924142](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230421_1682069365.png)

The p-value is very less than the significance level of 0.05 and hence we can reject the null hypothesis and take that the series is stationary.

Let’s visualise the series as well to confirm.

```python
import matplotlib.pyplot as plt
%matplotlib inline
fig, axes = plt.subplots(figsize=(10,7))
plt.plot(series);
plt.title('Random');
```

![image-20230421103050586](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230421_1682069451.png)

## White Noise

> Reference: 
>
> [1] https://machinelearningmastery.com/white-noise-time-series-python/#:~:text=What%20is%20a%20White%20Noise,other%20values%20in%20the%20series.
>
> [2] [How to detect the white noise in time series dataset](https://timeseriesreasoning.com/contents/white-noise-model/)

It answers the crucial question of **when should I stop fitting my model.**

### What is a White Noise Time series?

A time series may be white noise.

A time series is white noise if the variables are <u>independent</u> and <u>identically</u> distributed with **a mean of zero**.

This means that all variables have the **same variance** ($\sigma^2$) and each value has a **zero correlation** with all other values in the series.

If the variables in the series are drawn from a **Gaussian distribution**, the series is called Gaussian white noise.

**It is a time series with:**

1. Mean=0
2. Standard deviation is constant
3. Correlation between lags is 0 (No seasonality)

 ![image-20230420231451715](https://raw.githubusercontent.com/RooNat/Myimages/main/2023/04/upgit_20230420_1682028894.png)



### Why does it matter?

White noise is an important concept in time series analysis and forecasting.

It's important for two main reasons:

1. **Predictability**: If your time series is white noise, then, by definition, it is random. You cannot reasonably model it and make predictions.
2. **Model Diagnostics**: The series of errors from a time series forecast model should ideally be white noise.

Model Diagnostics is an important area of time series forecasting.

Time series data are expected to contain some white noise component on top of the signal generated by the underlying process.

For example:
$$
y(t)=signal(t)+noise(t)
$$
Once predictions have been made by a time series forecast model, they can be collected and analyzed. The series of forecast errors([residuals](#Residuals)) should ideally be white noise.

When forecast errors are white noise, it means that all of the signal information in the time series has been harnessed by the model in order to make predictions. All that is left is the random fluctuations that cannot be modeled.

We could do this using `plot_acf()` to plot the ACF diagram and see if there are some correlations between the lagged values.

A sign that model predictions are not white noise is an indication that further improvements to the forecast model may be possible.

## Residuals

> Reference: https://otexts.com/fpp2/residuals.html

The “residuals” in a time series model are what is left over after fitting a model. For many (but not all) time series models, **the residuals are equal to the difference between the observations and the corresponding fitted values:**
$$
e_t=y_t-\hat y_t
$$
Residuals are useful in checking whether a model has adequately captured the information in the data. A good forecasting method will yield residuals with the following properties:

1. The residuals are uncorrelated. If there are correlations between residuals, then there is information left in the residuals which should be used. in computing forecasts.
2. The residuals have zero mean. If the residuals have a mean other than zero, then the forecasts are biased.



## Lag operator

> Reference: https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/4f2256b0a9c3157a2676806ed261eb8f_MIT14_384F13_lec1.pdf

**Definition:** *Lag operator* Denoted *L*. $Ly_t=y_{t-1}$

