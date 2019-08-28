# MerkelScience Test Problems.

The code for the first two problems has been written in `MinSliceSumProblem.py` and `PositiveElementSearch.py` files.
The time and space complexities have been mentioned in the comments. I have tried to follow PEP 8 coding standard.
Please navigate to the `/tests` folder. It contains a script that covers various test cases for the above to code files.

# MerkelScience Crawler.
I have used 'Scrapy' framework to scrape the posts on the forum.  
Directory Structure -  
  
  
  
`bitcoininfo1/  

      scrapy.cfg            # deploy configuration file      

      bitcoininfo1/         # project's Python module, you'll import your code from here 

          __init__.py 

          items.py          # Scrapped objects are declared here.

          middlewares.py    # project middlewares file

          pipelines.py      # project pipelines file

          settings.py       # project settings file

          bitpost.csv		# Scraped data stored in this file (CSV format)

          bitpost.json      # Scraped data stored in this file (JSON format)

          spiders/          # a directory where you'll later put your spiders
              __init__.py

              spiderone.py  # Spider script that crawls and extracts important data.

              __pycache__   #`
The scraped data is maintained in the respective .csv and .json files.   
Bugs -   
* Was able to scrape the date/time. But as the mapping of post date-time <-> post was going wrong at times, I've commented it out.  
* Extraction of page number as highlighted in the page.
(This repo doesn't contain the code that puts the processed data into MongoDB)
Thanks.
