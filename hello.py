class HelloWorld:
    #"""docstring for HelloWorld"""
    args = []
    def __init__(self, string):
        self.string = string

    def hello(self):
        return self.string


a = HelloWorld('hello')
print a.hello()

for i in xrange(5):
    print i * 2

x = int(raw_input("input: "))
if x < 0:
    print '-'
elif x > 0:
    print '+'
else:
    print 'zero'
