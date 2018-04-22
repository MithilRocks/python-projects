from decorators import time_taken

class Sort:
    input_list = []

    # initialize list
    def __init__(self, input_list):
        self.input_list = input_list

    @time_taken  # calls the decorated. this will display time taken to execute the function
    # bubble sort list!
    def bubble_sort(self):
        swap = True
        while swap:
            # if no swaps occur, get out of while loop
            swap = False
            for indx in range( 0, len(self.input_list) - 1):
                if self.input_list[indx] > self.input_list[indx + 1]:
                    self.input_list[indx], self.input_list[indx + 1] = self.input_list[indx + 1], self.input_list[indx] 
                    swap = True

        return self.input_list 
