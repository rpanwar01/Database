from mapreduce import MapReduce

#-----------------------------------

class CharCount(MapReduce):

    def mapper(self, _, line):
        for char in line:
            yield (char,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

#-----------------------------------

input = [
    "this is an example of this line",
    "this is an example of some example text",
    "this is another example",
    "and this is some more text and text and text"
]

output = CharCount.run(input)
for item in output:
    print (item)