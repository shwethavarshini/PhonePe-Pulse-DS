# PhonePe-Pulse-DS
Inroduction
PhonePe is an Indian digital payments and financial services company headquartered in India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface, went live in August 2016. We ill be dealing with the data of Phonepe transactions and users over the last four years (2018,2019,2020,2021). We aim to collect, clean, organize, store, analyze and visualize the data. 

## 1) Data collection
   I have collected the data from Phonepe pulse github repository. I have cloned the data file and stored in my system as csv file. I have also collected data of longitude and latitude of Indian districts and states for mapping purpose.
   
## 2) Data cleaning and organizing
   I have used python pandas to clean data and do fair works. There has been a promblem with two districts of Arunachal Pradesh whose data were missing in few  data files. Hence I have mentioned 'NA' in the data fields of those districts. I have also reoved some irrelevant fields in csv tables. Then it is organised the revised data in a suitable format to use.

 ## 3) Data storage
   I have stored data in MySQL as various tables and different variable data files in the project folder to get easy access of the data. I have also made it available in my Github respository of this project.

## 4) Dashboard with Streamlit
   I have used Streamlit for creating a visually appealing dashboard. I have created three different sections, each does an unique way of visualization approach. The first section shows an Indian map representation of data with the information and scaling beside. The second section has four subsections and each subsections contains their own options of choice. This section involves graphs/plots/charts. The last section shows up four diffrent tables of the top ranking states on the corresponding titles. I have tried to show maximum colour variations and made it simple to users.

