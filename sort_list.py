from decorators import time_taken

class Sort:
    input_list = []

    # initialize list
    def __init__(self, input_list):
        self.input_list = input_list

    @time_taken  # calls the decorator. this will display time taken to execute the function
    # bubble sort list!
    def bubble_sort(self):
        swap = True
        while swap:
            # if no swaps occur, get out of while loop
            swap = False
            for indx in range( 0, len(self.input_list) - 1 ):
                if self.input_list[indx] > self.input_list[indx + 1]:
                    self.input_list[indx], self.input_list[indx + 1] = self.input_list[indx + 1], self.input_list[indx] 
                    swap = True

        return self.input_list 

class Quick_sort(Sort):
    input_list = []

    def __init__(self, input_list):
        # a way to call parent constructor in python
        super().__init__(input_list)

    @time_taken
    # main quick sort function
    def quick_sort(self):
        self.quick_sort_helper(0, len(self.input_list) - 1 )
        return self.input_list

    # calls partition and calls itself recursively
    def quick_sort_helper(self, first, last):
        if first < last:
            parition = self.partition(first, last)
            self.quick_sort_helper(first, parition - 1)
            self.quick_sort_helper(parition + 1, last)
    
    # divides the list in two parts to recursively quick sort each list
    def partition(self, first, last):
        
        # set the first element as pivot
        pivot = self.input_list[first]

        # initialize left and right markers
        left = first + 1
        right = last

        while True:
            # keep the pointer moving right till a number greater or equal to pivot is not discovered
            while self.input_list[left] <= pivot and left <= right:
                left += 1

            # keep the pointer moving left till a number less than or equal to pivot is not discovered
            while self.input_list[right] >= pivot and right >= left:
                right -= 1

            # when the pointers cross
            if left > right:
                break
            # swap left and right
            else:
                self.input_list[left], self.input_list[right] = self.input_list[right], self.input_list[left]
        
        # swap right and pivot once right and left pointers cross
        self.input_list[first], self.input_list[right] = self.input_list[right], self.input_list[first]

        return right
