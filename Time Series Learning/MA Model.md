---
tags: Time_Series
Module: 3
typora-copy-images-to: ./attachments
---

# MA Model

[toc]



## MA Model(Moving Average Model)

> Reference: 
>
> [1] [Moving average models](https://otexts.com/fpp2/MA.html)
>
> 

### Moving Average and ACF

Rather than using past values of the forecast variable in a regression, a moving average model uses past forecast errors in a regression-like model.
$$
y_t=c+\varepsilon_t+\theta_1 \varepsilon_{t-1}+\theta_2 \varepsilon_{t-2}+\cdots +\theta_{q}\varepsilon_{t-q}
$$
where $\varepsilon_t$ is white noise. We refer to this as an **MA(q) model**, a moving average model of order *q*. Of course, we do not *observe* the values of $\varepsilon_t$, so it is not really a regression in the usual sense.

Notice that each value of $y_t$ can be thought of as a weighted moving average of the past few forecast errors. However, moving average *models* should not be confused with the moving average *smoothing* we discussed in Chapter [6](https://otexts.com/fpp2/decomposition.html#decomposition). A moving average model is used for forecasting future values, while **moving average smoothing** is used for estimating the trend-cycle of past values.

