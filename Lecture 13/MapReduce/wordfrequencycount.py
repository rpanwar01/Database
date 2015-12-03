from mapreduce import MapReduce

class WordFrequencyCount(MapReduce):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)

class WordCount(MapReduce):

    def mapper(self, _, line):
        for word in line.split():
            yield (word,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

class CharCount(MapReduce):

    def mapper(self, _, line):
        for char in line:
            if char != ' ':
                yield (char,1)

    def combiner(self, key, values):
            yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':

    input = [
        "this is an example of this line",
        "this is an example of some example text",
        "this is another example",
        "and this is some more text and text and text"
    ]

    output = WordFrequencyCount.run(input)
    for item in output:
        print (item)

    #output = WordCount.run(open("/home/greg/yelp/reviews.json").readlines())
    #for item in output:
        #print (item)