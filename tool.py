import ciede2000
import numpy as np

from matplotlib import pyplot as plt

def isNeihbor(region1, region2):
    for i in range(region1):
        for j in range(region2):
            if( distBtwR(region1[i], region2[j]) <= 2):
                return True
    return False

#D4距离
def distBtwR(A, B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])

#skimage function
def show_img(img):
    width = 10.0
    height = img.shape[0]*width/img.shape[1]
    f = plt.figure(figsize=(width, height))
    plt.imshow(img)

def _weight_mean_color(graph, src, dst, n):
    """Callback to handle merging nodes by recomputing mean color.
    The method expects that the mean color of `dst` is already computed.
    Parameters
    ----------
    graph : RAG
        The graph under consideration.
    src, dst : int
        The vertices in `graph` to be merged.
    n : int
        A neighbor of `src` or `dst` or both.

    Returns
    -------
    data : dict
        A dictionary with the `"weight"` attribute set as the absolute
        difference of the mean color between node `dst` and `n`.
    """
    # diff = graph.nodes[dst]['mean color'] - graph.nodes[n]['mean color']
    diff = ciede2000.CIEDE2000(graph.nodes[dst]['mean color'],graph.nodes[n]['mean color'])
    diff = np.linalg.norm(diff)
    return {'weight': diff}

def merge_mean_color(graph, src, dst):
    """Callback called before merging two nodes of a mean color distance graph.
    This method computes the mean color of `dst`.
    Parameters
    ----------
    graph : RAG
        The graph under consideration.
    src, dst : int
        The vertices in `graph` to be merged.
    """
    graph.nodes[dst]['total color'] += graph.nodes[src]['total color']
    graph.nodes[dst]['pixel count'] += graph.nodes[src]['pixel count']
    graph.nodes[dst]['mean color'] = (graph.nodes[dst]['total color'] /
                                      graph.nodes[dst]['pixel count'])