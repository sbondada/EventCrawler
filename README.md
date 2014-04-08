# EventCrawler

The main motive to the project is to collect and identify similar events given an address

> for eg:  
> lets say we have an URL of an event *http://www.workshopsf.org/?page_id=140&id=1328* then our
> goal is to crawl the website and find at least 10 similar events. Our output should look more like
> this

> 1 http://www.workshopsf.org/?id=1328&page_id=140                                                                 
> 2 http://www.workshopsf.org/?id=2028&page_id=140                                                               
> 3 http://www.workshopsf.org/?id=2023&page_id=140                                                               
> 4 http://www.workshopsf.org/?id=2015&page_id=140                                                                 
> 5 http://www.workshopsf.org/?id=2013&page_id=140                                                        
> 6 http://www.workshopsf.org/?id=2012&page_id=140                                                      
> 7 http://www.workshopsf.org/?id=1999&page_id=140                                                          
> 8 http://www.workshopsf.org/?id=1993&page_id=140                                                                
> 9 http://www.workshopsf.org/?id=1973&page_id=140                                                                
> 10 http://www.workshopsf.org/?id=1958&page_id=140    

## Usage 

The steps needed to successfully run the code

* Install the dependent libraries
* clone a local copy of the repository
* locate the root directory
* tweek the configuration parameters, if needed
* execute the program

### Install Dependent Libraries

This project uses [scrapy](http://scrapy.org/) framework to crawl the website and discover similar
websites with a provided URL. so the system should start install scrapy to run the code. You can find
the installation details [here](http://doc.scrapy.org/en/latest/intro/install.html). It has all the dependences list and also instructions to install specific to the platform.

### Clone the Local Repository

Use Git to clone the repository you could use

'''javascript
git clone https://github.com/sbondada/EventCrawler.git
'''

### Locate the Root Repository

Directory structure of the whole code

* EventCrawler
    * **README.md**
    * eventcrawler
        * **scrapy.cfg**- project meta file.
        * eventcrawler- *root directory* for the project.
            * **items.py**- This file has the structure of the item we are extracting from each crawl.
            * **pipelines.py**- This file recieves the items from the spider where postproceessing takes
              place
            * **settings.py**- This file has all the configuration parameters for every part of the
              project needed.
            * spiders
                * **event_spider.py**- This is the main file which has all the code specifing how to
                  crawl, how the linkextracter is, and what are the score function etc.

### Tweek Configuration Parameters

You can modify the configuration parameters of the code by changing the values in **settings.py**.

### Execute The Program        
    
We Use Scrapy to execute the program. Run the following command.

''' javascript
scrapy crawl event -a start_url='http://calendar.boston.com/lowell_ma/events/show/274127485-mrt-presents-shakespeares-will'
'''

* scrapy- command line tool.
* crawl- start crawling a spider
* "event" - name of the spider to run
* -a - option for arguments
* start-url- a place to start crawling


You can find more information on Scrapy command tools
[here](http://doc.scrapy.org/en/latest/topics/commands.html#available-tool-commands) or use *scrapy -h*
command for help.
