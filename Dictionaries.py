# Dictionaries are a great way to keep track of things
# Dictionaries are dynamic
book = {
    "title": "A Song of Ice and Fire",
    "author": "George R. R. Martin",
    "year": 1996

}

print(book)
print(book["year"])

myTitle = book["title"]
#myTitle = book.get("title")
# these 'myTitle' string of code do the same thing
print(myTitle)

print(book.keys())
print(book.values())

book["pages"] = 254
print(book)

book["year"] = 1984
book.update({"year": 1997})
print(book)

if "author" in book:
    print("Yes it is in the dictionary")

# we could find the author but not a value, such as the date
#if 1997 in book:
    #print("Yes it is in the dictionary")

book.pop("year")
print(book)

book.popitem()

# this is how you delete an entire dictionary
#del book
#print(book)

# this is how you clear the book, meaning if you want to start over, it will wipe everything, not delete it
#book.clear()
#print(book)