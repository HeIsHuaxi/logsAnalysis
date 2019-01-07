# logsAnalysis
This python program analyze the web request logs of a server stored in SQL tables and output some summary information about the logs.
## How to use it
### Pre-requisite
The program was written and tested using *Python 2.27.12*.
### Create a view
Use the following SQL query to create a *most_read_article* view
```
create view "most_read_article" as
select articles.title, count(log.time) as views, articles.author
from log left join articles on SUBSTRING(log.path, 10) = articles.slug
where path not in ('/') and method = 'GET' and status = '200 OK'
group by articles.title, articles.author
order by views desc;
```
### Run the program
Use the following command to run the program
```
python loganalysis.py
```
