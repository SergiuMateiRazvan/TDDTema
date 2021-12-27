def get_no_of_equals(elems, given_element):
    counter = 0
    for elem in elems:
        if elem == given_element:
            counter += 1
    if counter == 0:
        raise Exception("Element not found")
    return counter


if __name__ == "__main__":
    print(get_no_of_equals([1, 2, 3, 4, 5, 3, 4, 2, 7, 4], 4))
