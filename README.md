# DynamicIPPool

### Description
This is an ip(proxy) pool implemented in Python. The major task is to collect(crawl) ips and ports from the Internet, and store the data in a accessible container(here I use `Redis`). 

Also, The pool must check the availability of each ip(proxy) in the background and remove stale data in a timely manner. 

What's more, `Flask` is involved to build some public APIs for data manupulations.

![](http://p0u4yewt0.bkt.clouddn.com/structure.png)
<center> <b>Structure</b> </center>


### Environment
1. `Python 3.6.0`
2. `Scrapy 1.4.0`
3. `Redis 3.2.9`
4. `Flask 0.12.2`

### Goals
+ Build a dynamic ip pool which integrates 
	+ ip crawling
	+ ip storage
	+ ip availability detection

+ Develop convenient APIs for ip data

+ Support my own crawler system

