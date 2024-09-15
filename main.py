import numpy as np

if __name__ == "__main__":
    number_list = []
    for number in range(1, 11):
        number_list.append(number)

    numpy_array = np.array(number_list)
    print(numpy_array)
