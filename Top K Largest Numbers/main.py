# Create a class that records numbers and can return the top N largest unique numbers added so far.

# Methodology: Use a set or list to store unique numbers, then sort descending and slice the top N.
# For efficiency with large N, consider a min-heap, but sorting is fine for simplicity.

# Create class
# Initialize set
# Add function for recording numbers
# Sort set
# Return top N

class LargestNumber:
    def __init__(self):
        self.storage = []

    def record_number(self, value):
        if value not in self.storage:
            self.storage.append(value)

    
    def largest_number(self, n):
        self.storage.sort(reverse=True)

        count = 0
        for i in self.storage:
            if count >= n:
                break
            print(i)
            count += 1 

        

largestNumber = LargestNumber()
largestNumber.record_number(19210)
largestNumber.record_number(2932)
largestNumber.record_number(28)
largestNumber.record_number(18229)
largestNumber.record_number(100)
largestNumber.record_number(57)
largestNumber.record_number(1210)
largestNumber.record_number(2932)
largestNumber.record_number(228)
largestNumber.record_number(18229)
largestNumber.record_number(100)
largestNumber.record_number(57)
largestNumber.record_number(19210)
largestNumber.record_number(2932)
largestNumber.record_number(28)
largestNumber.record_number(18229)
largestNumber.record_number(100)
largestNumber.record_number(57)

largestNumber.largest_number(3)