from mrjob.job import MRJob
import re

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        pattem = re.compile(r'(\W+)')
        for word in re.split(pattem,line):
            if word.isalpha():
                yield (word.lower(), 1)

    def reducer(self, word, counts):
        l = list(counts) #把values变成列表
        yield (word,sum(l))

if __name__ == '__main__':
     MRWordFreqCount.run()