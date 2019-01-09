# logsAnalysis
This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The program execute sequentially on these three functions: *get_most_popular_article(), get_most_popular_author(), get_error_days()*. Each function will connect to a local database called *news*, execute a SQL query and output the result in stdout.

## How to use it

### Pre-requisite

First step is to prepare the database, you will need to download the *newsdata.sql* file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it to the root of this repository.

In order to run the program, you will need to use Vagrant and VirtualBox in order to connect to a virtual machine environment.

Once installed, you should be able to run ```vagrant up``` in the root folder of the repository to wake up your virtual machine and run ```vagrant ssh``` to connect to it.

### Create a view
Use the following SQL query to create a *most_read_article* view
```sql
create view "most_read_article" as
select articles.title, count(log.time) as views, articles.author
from log left join articles on SUBSTRING(log.path, 10) = articles.slug
where path not in ('/') and method = 'GET' and status = '200 OK'
group by articles.title, articles.author
order by views desc;
```
### Run the program
Use the following command to run the program
```shell
python loganalysis.py
```
