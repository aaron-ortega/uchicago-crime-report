# uchicago-crime-analysis
## Info
This repository holds code used to scrap and clean almost 7 years, 2010-12-01 to 2017-08-21, worth of crime and fire related incidents reported by the University of Chicago Police Department. The patrol area is between 37th and 64th streets and Cottage Grove Avenue to Lake Shore Drive (Kenwood/HydePark/Woodlawn area). The public data can be found here -> [Daily Crime/Fire Log](https://incidentreports.uchicago.edu/)
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
and a cleaned pickled data table. There were over 500 uniquely name incidents. Therefore the focus of the cleaning has been giving to 6 categories of incidents: **lost property**, **theft**, **assault**, **burglary**, and **mental health** related. The data is as follows:


| Index  | Incident | Comments  | Reported | Coordinates|
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0  | lost  |woman reports losing a canon power shot digita...|2010-07-01 12:42:00|(41.7892236, -87.5980197)|
| 5  | lost  |staff member reports losing wallet containing ...|2010-07-01 23:09:00|(41.66861859999999, -87.7841447)|

### Motivation
Wanted to familiarize myself w/ webscraping (scrapy), text data wrangling (pandas), and interactive web mapping (folium).


There were a few reason why this project has interested me
- the process of gentrification
- UChicago's increase of police personal (one of the largest private police forces in the country)
- I walk my [pup](https://drive.google.com/file/d/1pmwvG7DrPzkTayweOsUlh6lwcWWynhKf/view?usp=sharing) late at night 

Speaking with locals about the rapid change that the neighboorhood has experience over the last decade and a Living in the surrounding area and receiving reportings made me wondering if there is some preferencing 

## Questions
- [ ] Has crime decrease through?
- [ ] Push my commits to GitHub
- [ ] Open a pull request


## Observations
