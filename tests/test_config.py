
class NotInRange(Exception):
    def __init__(self, message="Vale not in Range"):
        self.message = message
        super().__init__(self.message)



def test_generic():


    assert a ==b