import pickle

#a better way to store python objects is not to write them
#into string inside files, but to pickle them

d = {"a": 1, "b": 2, "c": 3}

#we are opening a pickle file and bringing it into python
#the wb argument means write binary which we will need
#to pickle our python object
f = open("my_pickle_file.pkl", "wb")

#this line takes our python object and pickles it for long term
#storage in the file opened in f
pickle.dump(d, f)

#here we are de-pickling and importing the python objects from
#the file system
l = pickle.load(f)

#the benefit of pickle is that there is no to string and from string
#convesions done.  The pickled object remains a native python object
#stored as binaries in the OS.
