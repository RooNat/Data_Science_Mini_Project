---
tags: Time_Series
Module: 2
typora-copy-images-to: ./attachments
---

# AR Model

[toc]

## AR Model

> Reference: 
>
> https://otexts.com/fpp2/AR.html
>
> https://machinelearningmastery.com/autoregression-models-time-series-forecasting-python/
>
> https://www.statisticshowto.com/autoregressive-model/
>
> https://www.statsmodels.org/dev/examples/notebooks/generated/autoregressions.html



In a multiple regression model, we forecast the variable of interest using a linear combination of predictors. In an autoregression model, we forecast the variable of interest using a linear combination of *past values of the variable*. The term *auto*regression indicates that it is a regression of the variable against itself.

Thus, an autoregressive model of order $p$ can be written as
$$
y_t=c+\phi_1 y_{t-1}+\phi_2 y_{t-2}+\cdots+ \phi_p y_{t-p}+\varepsilon_t
$$
where $\varepsilon_t$ is **white noise**. This is like a multiple regression but with *lagged values* of $y_t$ as predictors. We refer to this as an **AR(p) model**, an autoregressive model of order $p$.

For an AR(1) model:

- when $\phi_1=0$, $y_t$ is equivalent to white noise;
- when $\phi_1=1$ and $c=0$, $y_t$ is equivalent to a random walk;
- when $\phi_1=1$ and $c\neq0$, $y_t$ is equivalent to a random walk with drift;
- when $\phi_1<0$, $y_t$ tend to oscillate around the mean.

We normally restrict autoregressive models to stationary data, in which case some constraints on the values of the parameters are required.

- For an AR(1) model:  $-1<\phi_1<1$
- For an AR(2) model: $-1< \phi_2<1$, $\phi_1+\phi_2<1$, $\phi_2-\phi_1<1$

The correlation statistics can also help to choose which lag variables will be useful in a model and which will not.

Interestingly, if all lag variables show low or no correlation with the output variable, then it suggests that the time series problem may not be predictable. This can be very useful when getting started on a new dataset.

## Evaluating Time Series Models

### Rolling Forecast Origin

**Idea**: Predict one month in advance each time

Train on months $1,2,3,\cdots k-3 \to$ predict month $k-2$

Train on months $1,2,\cdots k-3,k-2 \to$ predict month $k-1$

Train on months $1,2,\cdots k-3,k-2,k-1 \to$ predict month $k$

