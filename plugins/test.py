class Plugin(object):
    """docstring for Plugin."""
    name = "Test-Plugin"

    def __init__(self):
        super(Plugin, self).__init__()

    def execute(self):
        print "Das ist ein test"

    def close(self):
        print "close test plugin"
