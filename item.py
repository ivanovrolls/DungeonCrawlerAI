class item:
    def __init__(self, name, stats, active):
        self.name = name
        self.stats = stats
        self.active = active

    @abstractmethod
    def stats(self, player):
        """Each item type must implement this method."""
        pass

    @abstractmethod
    def active(self, player):
        """Each item type must implement this method."""
        pass
