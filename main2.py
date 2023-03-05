from queue import Queue

src = [2, 8, 3, 1, 6, 4, 7, -1, 5]
target = [1, 2, 3, 8, -1, 4, 7, 6, 5]


def h(state):
    res = 0
    for i in range(1, 9):
        if state.index(i) != target.index(i): res += 1
    return res


def gen(state, m, b):
    temp = state[:]
    if m == 'l': temp[b], temp[b - 1] = temp[b - 1], temp[b]
    if m == 'r': temp[b], temp[b + 1] = temp[b + 1], temp[b]
    if m == 'u': temp[b], temp[b - 3] = temp[b - 3], temp[b]
    if m == 'd': temp[b], temp[b + 3] = temp[b + 3], temp[b]
    return temp


def possible_moves(state, visited_states):
    b = state.index(-1)
    d = []
    pos_moves = []
    if b <= 5: d.append('d')
    if b >= 3: d.append('u')
    if b % 3 > 0: d.append('l')
    if b % 3 < 2: d.append('r')
    for i in d:
        temp = gen(state, i, b)
        if not temp in visited_states: pos_moves.append(temp)
    return pos_moves


def search(src, target, visited_states, g):
    if src == target: return visited_states
    visited_states.append(src),
    adj = possible_moves(src, visited_states)
    scores = []
    selected_moves = []
    for move in adj: scores.append(h(move) + g)
    if len(scores) == 0:
        min_score = 0
    else:
        min_score = min(scores)
    for i in range(len(adj)):
        if scores[i] == min_score: selected_moves.append(adj[i])
    for move in selected_moves:
        if search(move, target, visited_states, g + 1): return visited_states
    return None


def bfs_search(src, target, visited_states):
    #     // pseudocode
    # func bfs(src, dest)
    #  create a queue q
    #  q.push(src)
    #  while q is not empty:
    #     c = q.pop()
    #     if c is dest: return all visited states
    #     add c to visited states
    #     for move in all_possible_moves_from(c):
    #       if move not in visited states :
    #         q.push(c)
    #  return Not found

    q = Queue()
    q.put((src, 0))
    while not q.empty():
        curr, g = q.get()
        if target == curr: return visited_states
        visited_states.append(curr)
        adj = possible_moves(curr, visited_states)
        scores = []
        selected_moves = []
        for move in adj: scores.append(h(move) + g)
        if len(scores) == 0:
            min_score = 0
        else:
            min_score = min(scores)
        for i in range(len(adj)):
            if scores[i] == min_score: selected_moves.append(adj[i])
        for move in selected_moves: q.put((move, g + 1))
    return None


def dfs_stuff(src, dest, visited_states):
    if src == dest: return visited_states
    visited_states.append(src)
    adj = possible_moves(src, visited_states)
    scores = []
    selected_moves = []
    for move in adj: scores.append(h(move))
    if len(scores) == 0:
        min_score = 0
    else:
        min_score = min(scores)
    for i in range(len(adj)):
        if scores[i] == min_score: selected_moves.append(adj[i])
    for move in selected_moves: return dfs_stuff(move, dest, visited_states)


def iterative_dfs(src, dest, visited_states, max_depth, ):
    restNeg = 'Not Found'
    i = 0
    while i < max_depth:
        res = dfs_stuff(src, dest, visited_states)
        if res == dest:
            print('hello')
            return res
        i = i + 1
        return res


def solve(src, target, choice):
    visited_states = []

    if int(choice) == 1:
        print("through DFS")
        res = dfs_stuff(src, target, visited_states)

    elif int(choice) == 2:
        print("through BFS")
        res = bfs_search(src, target, visited_states)
    elif int(choice) == 3:
        print("through search")
        res = iterative_dfs(src, target, visited_states, 3)

    if res:
        i = 0
        for state in res:
            print('move :', i + 1, end="\n")
            print()
            display(state)
            i += 1
        print('move :', i + 1)
        display(target)


def display(state):
    print()
    for i in range(9):
        if i % 3 == 0: print()
        if state[i] == -1:
            print(state[i], end="\t")
        else:
            print(state[i], end="\t")
    print(end="\n")


def run():
    print('Initial State :')
    display(src)
    print('Goal State :')
    display(target)
    print('*' * 10)
    solve(src, target, 1)


run()
