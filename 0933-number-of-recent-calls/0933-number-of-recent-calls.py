class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        # Remove timestamps that are more than 3000 milliseconds old
        while self.q and self.q[0] < t - 3000:
            self.q.pop(0)

        # Add the current timestamp to the queue
        self.q.append(t)

        # Return the number of elements in the queue, which represents
        # the number of pings in the last 3000 milliseconds
        return len(self.q)

# Example usage:
# obj = RecentCounter()
# param_1 = obj.ping(t1)
# param_2 = obj.ping(t2)
# ...
