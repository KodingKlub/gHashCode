import numpy as np
import philipp as p
import kordian as k
import anna as a
import parser
import sys
import itertools

def print_combination(combination):
    used_caches = sorted([k for k,v in combination.items() if v[0]!=0])
    print(len(used_caches))
    for used_cache in used_caches:
        videos_str = " ".join([str(c) for c in combination[used_cache][1]])
        print(used_cache, videos_str)


def make_sets(items, cache_ids, num_of_boxes=3):
    allpossible = []

    for tup in itertools.product(range(len(cache_ids)), repeat=len(items)):
        boxes = [list() for _ in range(len(cache_ids))]
        for item, box in zip(items, tup):
            # print (cache_ids[box])
            # itee = (, item)
            boxes[box].append({cache_ids[box]: (0, item)})

        # print(boxes)
        boxes_ = []
        boxes__ = []
        for b in boxes:
            ob = {}
            for e in b:
                for k in e:
                    if k not in ob:
                        ob[k] = (0,[])
                    ob[k][1].append(e[k][1])

            boxes_.append(ob)
            for k,v in ob.items():
                boxes__.append((k,ob[k][1]))

        # print(boxes__)
        # print(boxes_)
        allpossible.append(boxes__)

    return allpossible



if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
    problem = parser.get_problem(fname)


    # combination = {0:(80,[0,2]),1:(30,[1]),2:(0,[]),5:(10,[100])}
    # for k,v in combination.items():
    #     print(k,v)
    # print()
    # print()
    # print_combination(combination)
    make_sets(('A', 'B', 'C'), [0,1,8])
    # for p in make_sets(('A', 'B', 'C'), [0,1,8]):
    #     for box in p:
    #         print(str(box).ljust(20),)
    #     print()