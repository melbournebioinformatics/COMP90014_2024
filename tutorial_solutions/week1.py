


def isort_mod(items):
    """
    Sorts a list in-place using insertion sort
    """
    for index in range(1, len(items)):
        current_item = items[index]
        while index >= 1 and (current_item < items[index - 1]):
            items[index] = items[index - 1]
            index -= 1
        items[index] = current_item
        print(items)
    return items


def selection_sort(unsorted):
    """
    Sorts a list using selection sort
    """
    sorted_list = []    
    
    # while the unsorted list is not exhausted
    while len(unsorted) > 0:
        
        # find the smallest item in the remaining list.
        # if a value is smaller than the current, update min_index. 
        min_index = 0
        for index in range(1, len(unsorted)):
            if unsorted[index] < unsorted[min_index]:
                min_index = index

        # remove the smallest item from unsorted list & add to the sorted list.
        item = unsorted.pop(min_index)
        sorted_list.append(item)
    
    return sorted_list


def merge(list1, list2):
    """
    merges two sorted lists into a single sorted list. 
    """

    merged = []
    
    # create variables which point to the active item in each input list. 
    ptr1, ptr2 = 0, 0
    
    # loop until we reach the end of *either* list.
    # eg if we reach the end of list1, we can just append the remaining 
    # items in list2 & be done.
    while ptr1 < len(list1) and ptr2 < len(list2):

        # check which active item is smaller & should be added next.
        # after adding, need to advance pointer for that list. 
        if list1[ptr1] < list2[ptr2]:
            merged.append(list1[ptr1])
            ptr1 += 1
        else:
            merged.append(list2[ptr2])
            ptr2 += 1
        
    # Append remaining elements of list1, if any
    while ptr1 < len(list1):
        merged.append(list1[ptr1])
        ptr1 += 1
        
    # Append remaining elements of list2, if any
    while ptr2 < len(list2):
        merged.append(list2[ptr2])
        ptr2 += 1

    return merged

    """
    #Alternative solution using pop
    def merge(top, bottom):
        # Replace the code below so that we merge the lists properly
        # instead of just appending one after the other

        merged = []
        while len(bottom) >= 1 and len(top) >= 1:
            if bottom[0] <= top[0]:
                merged.append(bottom.pop(0))
            else:
                merged.append(top.pop(0))
        merged += top + bottom
        return merged
    """

