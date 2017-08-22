def find_shortest_path(grid, start_node, end_node):
    current_node = None
    if len(grid) == 0:
        return []
    if len(grid) == 1:
        return [start_node]
    open = {}
    close = {}
    f = {}
    open[start_node] = ''
    neighbor = find_neighbor(start_node, grid, start_node)
    for i in neighbor:
        open[i] = start_node
    del open[start_node]
    close[start_node] = ''
    for i in neighbor:
        temp_fg = calc_fg(i, f, start_node, end_node)
        f[i] = {'g': temp_fg[1], 'f': temp_fg[0]}
    while True:
        min = 10000
        for i in open.keys():
            if f[i]['f'] < min:
                min = f[i]['f']
                current_node = i
        close[current_node] = open[current_node]
        del open[current_node]
        neighbor = find_neighbor(current_node, grid, start_node)
        for i in neighbor:
            if (not i.passable) or i in close.keys():
                continue
            if i not in open.keys():
                open[i] = current_node
                temp_fg = calc_fg(i, f, current_node, end_node)
                f[i] = {'g': temp_fg[1], 'f': temp_fg[0]}
            if i in open.keys():
                if temp_fg[1] < f[i]['g']:
                    open[i] = current_node
                    temp_fg = calc_fg(i, f, current_node, end_node)
                    f[i] = {'g': temp_fg[1], 'f': temp_fg[0]}
        if end_node in open.keys():
            close[end_node] = current_node
            break
            
    result = [end_node]
    current_node = end_node
    while True:
        result.append(close[current_node])
        current_node = close[current_node]
        if current_node == start_node:
            break
    return result[::-1]

def find_neighbor(current_node, grid, start_node):
    x = current_node.position.x
    y = current_node.position.y
    temp = []
    if x-1 >= 0:
        temp.append(grid[x-1][y])
    if x+1 < len(grid):
        temp.append(grid[x+1][y])
    if y-1 >= 0:
        temp.append(grid[x][y-1])
    if y+1 < len(grid[0]):
        temp.append(grid[x][y+1])
    if start_node in temp:
        temp.remove(start_node)
    return temp

def calc_fg(i, f, parent_node, end_node):
    g = abs(i.position.x - parent_node.position.x) + abs(i.position.y - parent_node.position.y)
    if parent_node in f.keys():
        g += f[parent_node]['g']
    h = abs(i.position.x - end_node.position.x) + abs(i.position.y - end_node.position.y)
    f = g + h
    return (f, g)