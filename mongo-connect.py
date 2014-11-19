__author__ = 'Pavitheran'


from pymongo import MongoClient

# #Setup connection
##Replace *** with password to access the database
connection = MongoClient("mongodb://pavipycrawler:***@ds047720.mongolab.com:47720/pycrawlerdb")
database = connection.pycrawlerdb.crawl_collection

crawl_results = {}
flag = True

while (flag):
    # ask for input
    site_name, site_url = input("Enter website name and URL: ").split(',')
    # place values in dictionary
    crawl_results = {'name': site_name, 'url': site_url}
    # insert the record
    database.insert(crawl_results)
    # should we continue?
    flag = input('Enter another record? ')
    if (flag[0].upper() == 'N'):
        flag = False

##Finds stored documents
results = database.find()

print("Database Entries:")
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

# display documents from collection
for record in results:
    # print out the document
    print(record['name'] + ',', record['url'])


# close the connection to MongoDB
connection.close()

