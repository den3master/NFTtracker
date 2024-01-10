class Snake(object):
    def __init__(self, name, toxicity, aggression):
        self.name = name
        self.toxicity = toxicity
        self.aggression = aggression
    
    def __repr__(self):
        return "<%s>" % self.name