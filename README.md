**Prepared by : Tam Kam Jiunn**  
**Dataset : Sport**  

### Olympic Games Analytics
CapStone Project for VLC-SCADF (LHub)

### Problem Statement
Use data analytic to analyse how do NOCs (National Olympic Committee) perform in Summer Olumpics and what is(are) the factor(s) that contribute to success of NOCs in those events.

### Research Objective
1. Is there a relationship between number of participant and the number of medals of each NOCs
   > Evaluate the relation between number of participant each NOCs sent and the number of medals each NOCs received.

2. Does Host Nation have an medal advantage? 
   > Evaluation the relationship between the Host Nation and the number of medals the Host Nation received compare to the total available.

3. How has the number of NOCs entering each sport changed over time and which sport globalised fastest?
   > Evaluate the number of NOCs participate in each sport and the changes in the participating NOCs in each sport.

4. If there is a relationship between athlete age and medal probability, and if there is an optimal winning age by sport?
   > Evaluate the age of medal recipients, if there is a relation between age and medal recipients and the likely age of the medal recipients.

5. If there is a relationship between athlete profile (ie height/weight) and medal probability, and if there is an optimal winning profile by sport?
   > Evaluate the profile (age/height) of medal recipients and if there is a relation between profile and medal recipients.

### Dataset Overview
**Filename** : athlete_events(fr1996).csv  
**Time Horizone** : 1896 - 2016  
**  

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
2. Team looks unusual for some, will use NOC's name instead
3. noc_region.csv - some country name is listed in note 
4. noc_region.csv - Name of fields is in 2nd row of each column.
5. Respective host cities and countries (ie SummmerOlympic2.cvs) are sourced from internet.

Cleansing
1. Remove data related to winter games
2. Host_city_list (ie SummerOlympic2) from Internet is in English, to update host country data set to include non-English name
3. Join main table and Host_city_list
4. Join NOC_region table to main table
5. Remove unnecessary columns (ie Team, Games, Season) 


 





