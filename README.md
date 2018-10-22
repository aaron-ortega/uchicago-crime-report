# uchicago-crime-analysis
## Info
This repository holds code used to scrap and clean 8 years, 2010-07-01 to 2018-08-21, worth of crime and fire related incidents reported by the University of Chicago Police Department. The patrol area is between 37th and 64th streets and Cottage Grove Avenue to Lake Shore Drive (Kenwood/HydePark/Woodlawn area).<br> The public data can be found here -> [Daily Crime/Fire Log](https://incidentreports.uchicago.edu/)

<br> The data folder contains two main files: a raw data json file containing the following format<br>
 {<br>
 "Incident": "Lost Property",<br>
 "Location": "5810 S. University (Quad)",<br>
 "Reported": "7/1/10 12:42 PM",<br>
 "Occured": "6/28/10 2:45 PM",<br> 
 "Comments": "Woman reports losing a Canon Power Shot digital camera while in the Quad",<br> 
 "Disposition": "Closed",<br> 
 "UCPD_ID": "W0731"
 <br>}<br>
and a cleaned csv data table. There were over 500 uniquely name incidents. Therefore the focus of the cleaning has been giving to 6 categories of incidents: **lost property**, **theft**, **assault**, **burglary**, and **mental health** related. 

**Note**: Having mental health issues is in no way a crime. It wasn't after seeing the data did I noticed mental health incidents were being reported. It is included in order to increase awareness. 

The data is as follows:

| Index  | Incident | Comments  | Reported | Coordinates|
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0  | lost  |woman reports losing a canon power shot digita...|2010-07-01 12:42:00|(41.7892236, -87.5980197)|
| 5  | lost  |staff member reports losing wallet containing ...|2010-07-01 23:09:00|(41.66861859999999, -87.7841447)|

### Motivation
Wanted to familiarize myself w/ webscraping (scrapy), text data wrangling (pandas), and interactive web mapping (folium).

## Questions
- [x] Is there an overall crime trend? Constant/increasing/decreasing?
- [x] And what about specific incidents?
- [ ] Are there "hot" areas of crime?
- [x] Is daytime safer than nighttime?

## Observations

Recalling that 2010 has half a year of reporting one can assume that the number of incidents would be comparable to those in 2011 and 2012. After 2012 it appears that the total number of incidents has gone down and remained somewhat constant. Whether this is due to less reporting or enhanced security it cannot be said. Now what about specific incident trends?

![](./plots/total_incidents_per_year.png)

## More in campus or outside? Check interactive cluster (coming soon)
Check out 2018's in the meantime [Nbviewer data interactive](https://nbviewer.jupyter.org/github/aaron-ortega/uchicago-crime-analysis/blob/master/data_interactive.ipynb)

- **Assault** reports have increased over the last past three years.
- **Burglary** was bad in 2010 as it tops over the other years and with only six months worth of data (ouch!) 
- **Lost** property happens and it won't ever stop
- **Theft** has been on the decline these past years, but we won't know if the trend will continue for 2018. 
- A third of **Mental Health** incidents where reported by the University's Student Counseling Service

![](./plots/total_occurred_per_incident.png)

During incident reports, an approximation on the "time of incident" is usually given and it can be anywhere from a few hours to days. Hence, the difficulty of finding if an incident occurred during day or nighttime. The data below represents those which could be pinpointed. A [sunset-sunrise API](https://sunrise-sunset.org/api) was used to determine the information below.

**Important**<br> Just using the plot below isn't enough to say anything about day or nighttime crime prevalence; half of the total reports could not be classified. One can use 2017 and 2018's assaults as an example. In 2017, 35 assaults where reported compared to 2018's 25 (as of September). However, the plot gives the impression that nightime 2018 has been pervasive and that cannot be supported with the shown data.

![](./plots/total_reported_day_night_incident.png)

Finally, here is a breakdown by day and surprisingly the weekend is less eventful.

![](./plots/total_incidents_per_dayofweek.png)

