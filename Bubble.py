class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

def bubble_sort(arr, key=None, reverse=False):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            # By default, compare elements directly. If a key is provided, use it.
            if key is None:
                compare_a, compare_b = arr[j], arr[j + 1]
            else:
                compare_a, compare_b = getattr(arr[j], key), getattr(arr[j + 1], key)

            if (compare_a > compare_b) if not reverse else (compare_a < compare_b):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

# Example usage:
people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35), Person("David", 20)]

print("Original list of people:")
for person in people:
    print(person)

# Sort the list of people by age in ascending order
bubble_sort(people, key="age")

print("\nSorted list of people by age (ascending):")
for person in people:
    print(person)

# Sort the list of people by name in descending order
bubble_sort(people, key="name", reverse=True)

print("\nSorted list of people by name (descending):")
for person in people:
    print(person)
