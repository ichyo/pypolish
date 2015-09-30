from collections import defaultdict


def _empty_adj_lists(n):
    return [[] for _ in range(n)]


def _update_adj_lists(adj_lists, theta, sim):
    n = len(adj_lists)
    res = _empty_adj_lists(n)
    for u, Nu in enumerate(adj_lists):
        intersection = defaultdict(int)
        for w in Nu:
            for v in adj_lists[w]:
                if v >= u:
                    break
                intersection[v] += 1

        for v, I in intersection.items():
            val = sim(I, len(adj_lists[u]), len(adj_lists[v]), n)
            if val >= theta:
                res[v].append(u)
                res[u].append(v)
    return res


def _make_adj_lists_from_dictgraph(graph):
    dictionary = graph.keys()
    converter = {}
    n = len(dictionary)
    for i, v in enumerate(dictionary):
        converter[v] = i
    res = _empty_adj_lists(n)

    for k, v in graph.items():
        a = converter[k]
        for nk in v:
            b = converter[nk]
            res[a].append(b)

    for i in range(n):
        res[i].sort()

    return res, dictionary


def _make_adj_lists(graph):
    if isinstance(graph, dict):
        return _make_adj_lists_from_dictgraph(graph)
    else:
        raise TypeError('Unknown graph type')


def _restore_dictgraph_from_adj_lists(adj_lists, dictionary):
    res = defaultdict(list)
    for u, Nu in enumerate(adj_lists):
        a = dictionary[u]
        for v in Nu:
            b = dictionary[v]
            res[a].append(b)
    return dict(res)


def _polishing_adj_lists(adj_lists, theta, iteration, sim):
    for _ in range(iteration):
        adj_lists = _update_adj_lists(adj_lists, theta, sim)
    return adj_lists


def _polishing_dictgraph(graph, theta, iteration, sim):
    adj_lists, dictionary = _make_adj_lists(graph)
    adj_lists = _polishing_adj_lists(adj_lists, theta, iteration, sim)
    graph = _restore_dictgraph_from_adj_lists(adj_lists, dictionary)
    return graph


def graph_polishing(graph, theta, iteration, sim):
    if isinstance(graph, list):
        return _polishing_adj_lists(graph, theta, iteration, sim)
    elif isinstance(graph, dict):
        return _polishing_dictgraph(graph, theta, iteration, sim)
    else:
        raise TypeError('Unknown graph type')
