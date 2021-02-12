from linked_list import Linked_List as List
from Validator import Validator as Valid
import concurrent.futures


def negative_products(first, second):
    array_of_negatives = List()

    for i in first:
        for j in second:
            if Valid.check_int(i) * Valid.check_int(j) < 0:
                array_of_negatives.append(i * j)

    return array_of_negatives


def list_processing(op_list, minimal_element, maximal_element):
    op_list.change(minimal_element, 0)
    op_list.change(maximal_element, (-1) * maximal_element)

    return op_list


def find_min(op_list):
    min_el = op_list.peek()
    for x in op_list:
        if x < min_el:
            min_el = x

    return min_el


def find_max(op_list):
    max_el = op_list.peek()
    for x in op_list:
        if x > max_el:
            max_el = x

    return max_el


def the_task(first, second):
    if first.is_empty() or second.is_empty():
        print("One of the lists is empty")
        return
    resulting = negative_products(first, second)
    if len(resulting) <= 0:
        print("None negative products found")
        return

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(find_min, resulting)
        min_res = future.result()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(find_max, resulting)
        max_res = future.result()

    print("There are", len(resulting), "negative products of X(i) * Y(y)",
          "\n\nMinimal element is", min_res,
          "\nMaximal element is", max_res)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(list_processing, first, min_res, max_res)
        first = future.result()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(list_processing, second, min_res, max_res)
        second = future.result()
