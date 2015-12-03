from mapreduce import MapReduce

#----------------------------------------

class WordCount(MapReduce):

    def mapper(self, _, line):
        for word in line.split():
            yield (word,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

#----------------------------------------

input = [
    "this is an example of this line",
    "this is an example of some example text",
    "this is another example example example",
    "and this is some more text and text and text"
]

input = open("alice.txt").readlines()

output = WordCount.run(input)
for item in output:
    print item