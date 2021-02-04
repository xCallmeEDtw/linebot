class switch(object):
    def __init__(self, case_path):
        self.switch_to = case_path
        self._invoked = False

    def case(self, key, method):
        if self.switch_to == key and not self._invoked:
            self._invoked = True
            method()

        return self

    def default(self, method):
        if not self._invoked:
            self._invoked = True
            method()