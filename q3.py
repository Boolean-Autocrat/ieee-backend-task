# a class to generate distinct subsets of a set


class Subset:
    def __init__(self, set):
        self.set = set
        self.subsets = []

    def generate(self):
        self.subsets = self.generate_subsets(self.set)
        return self.subsets

    def generate_subsets(self, set):
        if len(set) == 0:
            return [[]]
        else:
            subsets = []
            for subset in self.generate_subsets(set[1:]):
                subsets += [subset]
                subsets += [[set[0]] + subset]
            return subsets


# test cases
subset = Subset([1, 2, 3])
print(subset.generate(), end="\n\n")
subset = Subset([1, 2, 3, 4])
print(subset.generate(), end="\n\n")

# user input
set = list(map(int, input("Enter the set of numbers (separated by spaces): ").split()))
subset = Subset(set)
print(subset.generate())
