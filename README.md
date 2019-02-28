# Shopping-Bots-for-Ecommerce-Stores
## Application domain:  
The web crawler can parse the source code of multiple sources and extracts the information to form a structured format. Users can compare the price of the items in different sources and look at the results sorted by relevance or by price.  

## How to run the code: 
Environment: Python 3.6.5
Dependencies: tkinter, requests, urllib, bs4, webbrowser, Crypto.Cipher
How to run the code: run command “python crawler.py”

## Major/Minor areas of specifications:
Major: Web Client Programming and Crawling
Minor: Advanced Graphical User Interface, Regular expression, Security: ASE symmetrically encrypt technology in encrypt communication, Polite Access: not visit the sites frequently and only valid user can visit.
Slightly involved: Hyperlink - Induced Topic Search

## Sell points:  
1) Real-time information collection  
Users can get information in the real-time instead of information collected/saved earlier to the local and retrieve the query from local data. That is we can get the information most up-to-date.
2) Time-efficient for users  
Instead of opening various web pages in multiple online shopping sites, users can query in the system and get the results of the comparison between the items among different sites. And according to their needs , they can choose different configuration for their query search.
3) Self-adjusted parsing  
Different source page may contains different format, we detect the source page the web crawler is going to and then use different recognition pattern to extract information. And crawled the website based on relevance or price.
4) Clear prompt and user friendly  
Clear instruction on error message and all the selections for the query searching(For example, which website to crawl, crawl according to relevance or price) are listed as checkbox or radio button. Very easy for user to use even if the first time user for our project.
5) Security  
Only valid user can use the crawler, avoiding unknown user doing malicious thins. 
             Plus for  the user validation, we use ASE to encrypt the password message and then 
             decrypt and  validate. Which make our validation more secure in some extent.
6) Multi-category in shopping sites included  
Instead of focusing on a specific comparison(e.g. T-shirt, skirt), we support information extraction for multiple categories in the shopping sites, meaning that a user is able to get all the categorical comparison information for the sites.  

## Limitations and possible improvements:  
Currently it didn’t use database to save the user information. In the future, we can link the crawler to the database in order to deal with more valid users suitations and use the databases to save the user information and user behavior, which can be an extension to the crawler that use collaborative filtering algorithm to give recommendation to the user based on their behavior( become a recommendation system). And for security purpose, we can add a time period threshold that if the user do not do any operations in the systems after this time period, they will be automatically log out and need to sign in again.

## Preview
### Login
<img src="https://github.com/xinyaoliu/Shopping-Bots-for-Ecommerce-Stores/blob/master/screenshots/login.png" width = "100" height = "100" div align=center />
### Search 
<img src="https://github.com/xinyaoliu/Shopping-Bots-for-Ecommerce-Stores/blob/master/screenshots/search.png" width = "100" height = "100" div align=center />
### Search result
<img src="https://github.com/xinyaoliu/Shopping-Bots-for-Ecommerce-Stores/blob/master/screenshots/result.png" width = "100" height = "100" div align=center />


