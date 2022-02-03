# Software Engineer Assignment - DATA/ETL
## Technologies: Python, Scrapy Framework
## Database: mongoDB (noSQL)

I’ve scraped [Net-a-porter] website of its two sections (topwear and footwear) and those two urls are: 

- Topwear - https://www.net-a-porter.com/en-in/shop/clothing/tops
- Footwear - https://www.net-a-porter.com/en-in/shop/shoes

## Task: 1

Create virtual environment 
- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#
```sh
pip install -r requirements.txt
```

Create MongoDB Atlas accounts and configure your database credentials into <b>settings.py</b> file in "configure item pipelines" section

```sh
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {'net_a_porterscrapyer.pipelines.NetAPorterscrapyerPipeline': 300,}

# MONGO_URI = 'mongodb+srv://mongodbuser:mongodbuser123@cluster0.yzgln.mongodb.net/prashantverma?retryWrites=true&w=majority'
# MONGO_DATABASE = 'prashantverma'
```

Open the command prompt: 

```sh 
scrapy crawl ecommerce
``` 
It will store the data in Mongodb Atlas (database: prashantverma, collection: flipkart) 
if you want to save into one file then write 
```sh 
scrapy crawl ecommerce -O your_file_name.json
```

> Note: If you do a capital O, It will overwrite the file completely but if you do a lowercase o, it will actually append it to your file into one file.



## Task: 2

MongoDB Shell (mongosh): <b> https://downloads.mongodb.com/compass/mongosh-1.1.7-x64.msi</b>

Open the mongosh shell to connect with mongoDB Atlas and the command is, 
mongosh <b>"mongoDB Atla urls"</b> and mongosh shell will connect with the mongoDB Atla.

Example: 

```sh
mongosh “mongodb+srv://mongodbuser:mongodbuser123@cluster0.yzgln.mongodb.net/prashantverma?retryWrites=true&w=majority"
```
1. How many products did you scrape? 
- Query: db.flipkart.countDocuments() 
Output: 3934

2. How many unique brands are present in the collection? 
- Query: db.flipkart.distinct('brand').length
Output: 276

3. Which brand in Topwear section is selling the most number of products?
- Query: db.flipkart.aggregate([{$group: {_id: "$brand", count: {$sum: 1}}}, {$sort:{count: -1, _id: 1}}])

4. How many products have `shirt` in their name?
- Query: db.flipkart.find({"name" : /shirt/ })

## Documents and References

| Name | Sources |
| ------ | ------ |
| MongoDB Atlas | [https://docs.atlas.mongodb.com/getting-started/][PlDb] |
| MongoDB Shell (mongosh) | [https://docs.mongodb.com/mongodb-shell/][PlGh] |


   [PlDb]: <https://www.mongodb.com/cloud/atlas/register>
   [PlGh]: <https://docs.mongodb.com/mongodb-shell/connect/#std-label-mdb-shell-connect>
