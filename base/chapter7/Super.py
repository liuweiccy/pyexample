# 超类
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, seq):
        return [x for x in seq if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
seq = f.filter([1, 2, 3, 4, 5])
print(seq)

spam = SPAMFilter()
spam.init()
seq = spam.filter(['SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])
print(seq)


print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))

print(SPAMFilter.__base__)
print(Filter.__base__)

print(f.__class__)
print(spam.__class__)

print(type(f))
print(type(spam))

print(spam.__dict__)


print(isinstance(spam, SPAMFilter))
print(isinstance(spam, Filter))
print(isinstance(f, SPAMFilter))
