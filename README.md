# AQI
Air Quality Prediction


**AQI Calculation:**

How is AQI Calculated?

The AQI calculation is made based on 7 measures of pollutants

**PM2.5, PM10,SO2, NOx, NH3, CO &amp; O3**

![](RackMultipart20201124-4-13titrp_html_a582b50293e03580.png)

1. Overall AQI is calculated only if data is available for minimum three pollutants out of which one should necessarily be either PM2.5 or PM10.
2. A minimum of 16 hours of data is considered necessary for calculating sub-index i.e. For 5 pollutants the average value in last 24-hrs is used with the condition of having at least 16 values.
3. The maximum value in last 8-hrs is used for **CO** and **O3**

![](RackMultipart20201124-4-13titrp_html_86d6bd6683593ba8.png)

The breakpoints shown in above table are used in the sub-index calculation.

**Observations:**

**Observation No 1:** [https://app.cpcbccr.com/AQI\_India/](https://app.cpcbccr.com/AQI_India/) The official CPCB Website

Here the AQI is calculated based on the Max value of the overall average of a pollutant.

![](RackMultipart20201124-4-13titrp_html_dcdb44572e3dec49.png)

As you can see from the above screenshot that the **Final AQI value 330** is the maximum value of all the averages.

The averages are calculated based on the last 24-hourly concentration values of **PM2.5, PM10, SO2, NO2, NH3** and 8-hourly in the case of **CO** and **O3**.

For ex: 101 is the average of **last** 8-hours of data.

**Observation No 2:**

AQI Calculator Excel:

The sub-index is calculated by the equation for a given pollutant concentration

Ip = [{(IHI – ILO)/(BHI -BLO)} \* (Cp -BLO)]+ ILO

Where

BHI = Breakpoint concentration greater or equal to given concentration.

BLO = Breakpoint concentration smaller or equal to given concentration.

IHI=AQI value corresponding to BHI

ILO = AQI value corresponding to BLO

Ip = Pollutant concentration

![](RackMultipart20201124-4-13titrp_html_e79e19602842ffed.png)

**Example:**

The 24-hour average value of PM10 on 3/11/20 at station Anand Vihar Delhi is **360**.

From the breakpoints picture.

IHI = 400, ILO = 301, BHI= 430, BLO = 351

**Ip = [{(400 – 301)/(430 -351)} \* (360 -351)]+ 301**

Ip = 313

_This result matches the one in the AQI Calculator._

**Observation No 3:**

**AQIPY Library:**

This is a custom library which has AQI calculators of 10countries. I have used aqi\_in.py to get aqi. Unfortunately the results are incorrect.

![](RackMultipart20201124-4-13titrp_html_7e0d8ea66186e68.png)

The result is the same i.e. 500 for different set of inputs.

Resources:

[https://app.cpcbccr.com/ccr\_docs/How\_AQI\_Calculated.pdf](https://app.cpcbccr.com/ccr_docs/How_AQI_Calculated.pdf)

[https://github.com/atmotube/aqipy](https://github.com/atmotube/aqipy)

[http://www.indiaenvironmentportal.org.in/files/file/Air%20Quality%20Index.pdf](http://www.indiaenvironmentportal.org.in/files/file/Air%20Quality%20Index.pdf)

[https://app.cpcbccr.com/AQI\_India/](https://app.cpcbccr.com/AQI_India/)
