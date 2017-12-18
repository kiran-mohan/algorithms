def insertion_sort(vector):
    for j in range(1,len(vector)):
        key = vector[j]
        i = j - 1
        while (i >= 0) and (vector[i] > key):
            vector[i+1] = vector[i]
            i = i - 1
        vector[i+1] = key

if __name__ == "__main__":
    vector = [8,6,4,8,9,5,1,3,2]
    insertion_sort(vector)
    print vector
