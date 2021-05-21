from tkinter import *
from tkinter import ttk
import time
import random


# Define the interface
lst1 = [2, 3, 45, 2, 12, 3, 32, 1, 23, 43, 2, 12, 124, 56, 32]
temp_list = lst1.copy()
window = Tk()
window.title('Sorting Algorithm Visualizer')
window.maxsize(1000, 600)

window.config(bg='black')
algorithm = StringVar()
speed = StringVar()


# Small toolbox bar
UI_frame = Frame(window, width=600, height=200, bg='yellow')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# The main function which draws the blue bars


def drawData(data, colorr):
    data = [i / max(data) for i in data]
    list_window.delete("all")
    for e, i in enumerate(data):
        first_x = 20*(e+1)
        second_x = 20*e
        first_y = 300-(i*300)
        second_y = 300
        list_window.create_rectangle(
            first_x, first_y, second_x, second_y, fill=colorr[e])
    window.update_idletasks()

# When the user presses the button sort


def select_algo():
    val = (list_of_algorithms.get())
    return val

# When the user selects the speed


def select_speed():
    if speeds.get() == 'Slow':
        return 0.5
    elif speeds.get() == 'Medium':
        return 0.1
    elif speeds.get() == 'Fast':
        return 0.001


def bogo_sort(lst, drawData, speed):  # slowest algorithm
    random.shuffle(lst)   # randomly shuffle list
    # count = 0
    while lst != sorted(lst):  # if shuffled lst != sorted list
        random.shuffle(lst)  # shuffle again
        # count += 1
        drawData(lst, ['red' for x in range(len(lst))])
        time.sleep(speed)
    drawData(lst, ['blue' for x in range(len(lst))])


def bubble_sort(lst1, drawData, sleep):
    for i in range(len(lst)-1):
        for j in range(size-i-1):
            if lst1[j] > lst1[j+1]:
                lst1[j], lst1[j+1] = lst1[j+1], lst1[j]
                drawData(lst1, ['red' if x == j or x == j +
                                1 else 'blue' for x in range(len(lst1))])
                time.sleep(sleep)
    drawData(lst1, ['blue' for x in range(len(lst1))])


def selection_sort(lst, drawData, speed):
    for i in range(len(lst)-1):
        minimum_value = i

        # (i+1) is our starting index since we already chose the first 'i' as our minimum value
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minimum_value]:
                minimum_value = j

        if minimum_value != i:  # if j is the minimum value
            lst[i], lst[minimum_value] = lst[minimum_value], lst[i]  # swap indexes
            drawData(
                lst, ['red' if x == minimum_value else 'blue' for x in range(len(lst))])
            time.sleep(speed)
    drawData(lst, ['blue' for x in range(len(lst))])


def insertion_sort(lst, drawData, timeTick):

    for i in range(1, len(lst)):
        value = lst[i]

        while lst[i-1] > value and i > 0:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1
            drawData(lst, ['red' if x == value
                           else 'blue' for x in range(len(lst))])
            time.sleep(timeTick)
    drawData(lst, ['blue' for x in range(len(lst))])


def partition(lst1, fromm, to, drawData, timeTick):

    pivot = lst1[to]

    for i in range(fromm, to):
        if lst1[i] < pivot:
            lst1[fromm], lst1[i] = lst1[i], lst1[fromm]
            fromm += 1
    lst1[fromm], lst1[to] = lst1[to], lst1[fromm]
    return fromm


def quick_sort(lst1, fromm, to, drawData, timeTick):
    if fromm < to:
        index = partition(lst1, fromm, to, drawData, timeTick)
        quick_sort(lst1, fromm, index-1, drawData, timeTick)
        quick_sort(lst1, index+1, to, drawData, timeTick)

        drawData(lst1, ['purple' if x >= fromm and x < index else 'yellow' if x ==
                        index else 'green' if x > index and x <= to else 'blue' for x in range(len(lst1))])
        time.sleep(timeTick)

    drawData(lst1, ['blue' for x in range(len(lst1))])


def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)

        p = start
        q = mid + 1
        tempArray = []

        for i in range(start, end+1):
            if p > mid:
                tempArray.append(data[q])
                q += 1
            elif q > end:
                tempArray.append(data[p])
                p += 1
            elif data[p] < data[q]:
                tempArray.append(data[p])
                p += 1
            else:
                tempArray.append(data[q])
                q += 1

        for p in range(len(tempArray)):
            data[start] = tempArray[p]
            start += 1

            drawData(data, ['purple' if x >= start and x < mid else 'yellow' if x == mid
                            else 'green' if x > mid and x <= end else 'blue' for x in range(len(data))])
            time.sleep(timeTick)

        drawData(data, ['blue' for x in range(len(data))])

# Define function of the shuffle button


def initialize(drawData):
    drawData(lst1, ['blue' for x in range(len(lst1))])

# To call all the functions once the sorting algorithm has been selected


def sort():
    global lst1
    speed = select_speed()
    if select_algo() == "Bubble Sort":
        bubble_sort(lst1, drawData, speed)
    if select_algo() == "Selection Sort":
        selection_sort(lst1, drawData, speed)
    if select_algo() == "Bogo Sort":
        bogo_sort(lst1, drawData, speed)
    if select_algo() == 'Quick Sort':
        quick_sort(lst1, 0, len(lst1)-1, drawData, speed)
    if select_algo() == 'Merge Sort':
        merge_sort(lst1, 0, len(lst1)-1, drawData, speed)
    if select_algo() == 'Insertion Sort':
        insertion_sort(lst1, drawData, speed)


# To shuffle our sorted list into our original list
def shuffle():
    global lst1
    lst1 = temp_list.copy()
    initialize(drawData)


# Creating Buttons for Functions to Perform in the UI frame
Button(UI_frame, text='Sort', command=sort,
       bg='white').grid(row=3, column=0, padx=5, pady=5)

Button(UI_frame, text='Shuffle', command=shuffle,
       bg='white').grid(row=3, column=1, padx=5, pady=5)


# Box for choosing algorithms
Label(UI_frame, text='Choose an Algorithm:', bg='grey').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
list_of_algorithms = ttk.Combobox(UI_frame, textvariable=algorithm, values=[
                                  'Bubble Sort', 'Bogo Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort'])
list_of_algorithms.grid(row=0, column=1, padx=5, pady=5)
list_of_algorithms.current(0)   # for keeping Bubble Sort as our Default option

# Box for choosing speed
Label(UI_frame, text='Choose Speed:', bg='grey').grid(
    row=1, column=0, padx=5, pady=5, sticky=W)
speeds = ttk.Combobox(UI_frame, textvariable=speed,
                      values=['Slow', 'Medium', 'Fast'])
speeds.grid(row=1, column=1, padx=5, pady=5)
speeds.current(0)

#                                               Setting up the User Interface Area


# Visualizing Area
list_window = Canvas(window, width=600, height=300, bg='white')
list_window.grid(row=1, column=0, padx=5, pady=5)


# Generating window to draw the lists
drawData([2, 3, 45, 2, 12, 3, 32, 1, 23, 43, 2, 12, 124, 56, 32],
         ['blue' for x in range(len(lst1))])

window.mainloop()  # for running the whole code
