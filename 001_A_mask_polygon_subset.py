all_polygons = [[0,1,2],[1,2,3],[2,3,4],[3,4,5],[5,6,7]]
subset_polygons = [[0,1,2],[3,4,5]]


def make_subset_mask(polygons, subset):
    sset = set(tuple(s) for s in subset)
    return [int(tuple(p) in sset) for p in polygons]


right_answer = [1,0,0,1,0]
assert(right_answer == make_subset_mask(all_polygons, subset_polygons))
