import porc

API_KEY = "7f516c0e-8468-4db9-b7fd-602c5c600df7"

"""
This is your "database" for remote storage.
It uses key value stores and stores objects in
JSON format.
"""
COLLECTION = "python_db"
"""
A key roughly maps to a specific "table" or "schema"
in your database.  A database can have multiple
tables for storing different kinds of related data.
"""
KEY = "hello world"

client = porc.Client(API_KEY)

"""
Using the .get() method allows you to read from your
databse by implementing the HTTP GET method
"""
response = client.get(COLLECTION, KEY)

# HTTP response code
print(response.response)

# JSON response data
print(response.json)

"""
This allows you to write new data to your database
using the HTTP POST method
"""
data = {"another bit of data": "look here it is"}
posted_data = client.post(COLLECTION, data)

# HTTP code 201 for created
print(posted_data.response)

# each individual key: value pair gets a unique key value
print(posted_data.key)
second_data = posted_data.key

"""
Here I've changed our data to send to the database.
Using the .put() method I can update existing data
in the database by using either its key as in 
{key: value} or by the pair's unique value
"""
data["another bit of data"] = "look I changed it"
updated_data = client.put(COLLECTION, second_data, data)

# get all data from a table
# careful, this could be a very large amount of data
all_data = client.list(COLLECTION)

# how about just a little bit at a time
some_data = all_data.next()

# pages are interable objects
pages = all_data.all()
for page in pages:
    page.raise_for_response()

"""
The different versions of your data are tracked by
using refs.  If you want to rollback changes on a
piece of data, you can check its versions and then
delete only the versions of the data that are bad.
"""
version = client.refs(COLLECTION, second_data)

# see all the versions of our data
print(version.json)

"""
You can delete data using a .delete() method as well.
You can delete by a table (collection), key, unique id, 
or just a version of the data by ref.
"""
deleted_data = client.delete(COLLECTION, second_data)

"""
You can also search for data by building queries.
There is a Search class that implements many methods
for filtering, sorting, pattern matching, and other
querying techniques.
"""

# adding another record with the key of hello
# now we have hello:world and hello:Portland
post = client.post("python_db", {"hello": "Portland"})

# creating a query to search for only hello:Portland
search = porc.Search().query("hello:Portland*")

# send the query to the database
pages = client.search(COLLECTION, search)

# paginated results
page = pages.next()

# matching query results
print(page.json)
