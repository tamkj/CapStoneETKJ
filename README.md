**Prepared by : Tam Kam Jiunn**  
**Dataset : Sport**  

### Olympic Games Analytics
CapStone Project for VLC-SCADF (LHub)

### Problem Statement
Use data analytic to analyse how do NOCs (National Olympic Committee) perform in Summer Olumpics and what is(are) the factor(s) that contribute to success of NOCs in those events.

### Research Objective
1. Is there a relationship between number of participant and the number of medals won by each NOCs
   > Evaluate the relation between number of participant each NOCs sent and the number of medals each NOCs received.

2. Does Host Nation have an medal advantage? 
   > Evaluation the relationship between the Host Nation and the number of medals the Host Nation received compare to the total available.

3. How has the number of distinct NOCs entering each sport changed over time, and which sport experienced the fastest growth in NOC participation?
   > Evaluate NOCs participation change over time, and which sport experienced the fastest growth in NOC participation.

4. If there is a relationship between athlete age and medal probability, and if there is an optimal winning age by sport?
   > Evaluate the age of medal recipients, if there is a relation between age and medal recipients and the likely age of the medal recipients.

5. Within each sport and sex, is there a relationship between athlete BMI band and medal rate, and which BMI band has the highest medal conversion?
   > Evaluate the profile (BMI) of medal recipients and which profile has the highest medal conversion.

### Dataset Overview
**Filename** : athlete_events(fr1996).csv  
**Time Horizone** : 1896 - 2016  

Link to Jypyter Notebook in Google Colab :  https://github.com/tamkj/CapStoneETKJ/blob/main/CapStone_Sport.ipynb


### Data Dictionary
The dataset consists of the following :
| Column Name | Data Type | Description | Example Value |
| ----------- | --------- | ----------- | ------------- |
| ID | int64 | Game participant's ID | 135563 |
| Name | object | Game participant's name | Olesya Nikolayevna Zykina |
| Sex | object | Game participant's sex | F |
| Age | float64 | Game participant's age | 23 |
| Height | float64 | Game participant's height | 171 |
| Weight | float64 | Game participant's weight | 64 |
| NOC | object | National Olympic Committee | RUS |
| Year | int64 | Year of event | 2004 |
| City | object | Host city | Athina |
| Sport | object | Sport athlete participated | Athletics |
| Event | object | Specific event athlete participated | Athletics Women's 4 x 400 metres Relay | 
| Medal | object | Medal won (if applicable) | Silver |
| Host_Cty | object | Host country | Australia |
| region | object | Country of NOC | Russia |

### Data Quality and Cleaning Notes
Data issue
1. Host city name not in English (eg Athina, Roma)
2. Team looks unusual for some, will use NOC's name instead.
3. Age 75 and above - mainly for event from 1912 to 1948.
4. noc_region.csv - some country name is listed in note. 
5. noc_region.csv - Name of fields is in 2nd row of each column.
6. noc_region.cvs - Singapore NOC code in csv is SIN while NOC code in main dataset is SIN.
7. Respective host cities and countries (ie SummmerOlympic2.cvs) are sourced from internet. 

Cleansing
1. Remove data related to winter games.
2. Host_city_list (ie SummerOlympic2) from Internet is in English, to update host country dataset to relevant non-English name
3. Join main table and Host_city_list.
4. Change SIN in main dataset to SGP.
5. Join NOC_region table to main table.
6. Remove unnecessary columns (ie Team, Games, Season). 


 





