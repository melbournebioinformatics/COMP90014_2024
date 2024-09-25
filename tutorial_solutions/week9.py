

##############
# Exercise 1 #
##############

def get_neighbours(all_points: list[Datapoint], point: Datapoint, eps: float):
    """
    Find all data points that occur within a maximum of eps distance of point p.
    Return as list of index positions corresponding to each neighbour in the input data point list.
    """
    ### BEGIN SOLUTION
    neighbours = []
    for i in range(len(all_points)):
        if euclidean_distance(all_points[i], point) <= eps:
            neighbours.append(all_points[i])
    
    return neighbours
    ### END SOLUTION


##############
# Exercise 2 #
##############

def get_point_type(all_points: list[Datapoint], point: Datapoint, min_pts: int, eps: float) -> str:
    """
    Identifies the 'type' of a given Datapoint. 
    
    Return point label as: 
    - 'core' if number of points within eps radius >= min_pts, including self.
    - 'border' if within eps distance of a core point
    - 'noise' if not within eps distance of a core point

    Use your 'get_neighbours()' function to help. 
    """
    ### BEGIN SOLUTION
    # get neighbours  
    neighbours = get_neighbours(all_points, point, eps)
    
    # is this a core point? 
    if len(neighbours) +1 >= min_pts: 
        return 'core'
    
    # is this a border point?
    for p in neighbours:
        p_neighbours = get_neighbours(all_points, p, eps) 
        if len(p_neighbours) >= min_pts:
            return 'border'
    
    # if haven't returned yet, this point is noise. 
    return 'noise'
    ### END SOLUTION


##############
# Exercise 3 #
##############

def traverse(all_points: list[Datapoint], point: Datapoint, eps: float, cluster_id: int) -> None:
    """
    Assigns cluster_id to point.cluster.
    Handles neighbouring points in the following manner: 
        - If the neighbour point already has a valid 'cluster' assigned, ignore.
        - If the neighbour point is 'noise', ignore. 
        - If the neighbour point is 'core', <small>`traverse()`</small> from this next core node. 
        - If the neighbour point is 'border', update its 'cluster' attribute and continue.  
    """
    ### BEGIN SOLUTION
    # add core point to cluster
    point.cluster = cluster_id
    
    # get neighbour points
    neighbours = get_neighbours(all_points, point, eps)
    
    for n in neighbours:
        # already discovered
        if n.cluster is not None or n.ptype == 'noise':
            continue 
        
        # if core, traverse
        elif n.ptype == 'core':
            traverse(all_points, n, eps, cluster_id)

        # if border, update cluster & continue
        elif n.ptype == 'border':
            n.cluster = cluster_id
        
        else:
            raise RuntimeError
    ### END SOLUTION


##############
# Exercise 4 #
##############

def dbscan(datapoints: list[Datapoint], min_pts: int, eps: float) -> None:
    """
    performs DBSCAN clustering. 
    """
    for point in datapoints:
        point.ptype = get_point_type(datapoints, point, min_pts, eps)

    ### BEGIN SOLUTION
    cluster_id = 0
    for point in datapoints:
        
        # ignore if cluster already assigned. 
        if point.cluster is not None:
            continue

        # noise point
        elif point.ptype == 'noise':
            point.cluster = -1

        # border point:
        elif point.ptype == 'border':
            continue 

        # core point
        elif point.ptype == 'core':
            cluster_id += 1
            traverse(datapoints, point, eps, cluster_id)
        
        else:
            raise RuntimeError
    ### END SOLUTION
    
    