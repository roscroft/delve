class Test():
    def __init__(self, test_attr):
        self.test_attr = test_attr
        self.test_fn()
        print(self.test_attr)
    
    def test_fn(self):
        self.test_attr = "goodbye world"