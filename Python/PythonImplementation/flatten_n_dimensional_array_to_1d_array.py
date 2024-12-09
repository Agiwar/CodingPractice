def flatten_array(array):
    if not array: return []

    res = []

    def dfs(sub_array, res):
        for item in sub_array:
            if isinstance(item, list):
                dfs(item, res)
            else:
                res.append(item)

    dfs(array, res)
    return res