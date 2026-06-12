# from abc import ABC, abstractmethod
# class Problem(ABC):
#
#     @abstractmethod
#     def initial_state(self):
#         pass
#
#     @abstractmethod
#     def is_goal(self, node_state) -> bool:
#         return False 
#


class Problem:
    def __init__(self, graph, initial_state, goal):
        self.graph: dict = graph 
        self.initial_state: str|int = initial_state 
        self.goal: str|int = goal 


    def is_goal(self, node_value) -> bool:
        return True if node_value == self.goal else False


class Node:
    def __init__(self, value, parent, action, cost) -> None:
        self.value: str|int = value 
        self.parent: Node|None = parent 
        self.action = action 
        self.cost = cost


# Search algorithms 
from collections import deque

def breadth_first_search(problem: Problem) -> Node | None:
    """FIFO queue searching width of the problem space"""
    # Initial node is set with the problems initial state, no parents, no action, no cost
    start_node: Node = Node(problem.initial_state, None, None, 0)

    if problem.is_goal(start_node.value):
        return start_node

    frontier: deque[Node] = deque()
    frontier.append(start_node)
    reached: set = {start_node.value}

    while frontier:
        node = frontier.popleft()

        if problem.is_goal(node.value):
            return node 

        children: list[Node] = expand(problem, node)
        for child in children:
            if child.value not in reached:
                frontier.append(child)
                reached.add(child.value)

    return None


def expand(problem: Problem, node: Node) -> list[Node]:
    children = []

    for child_value in problem.graph.get(node.value, []):
        child = Node(child_value, node, None, node.cost + 1)
        children.append(child)

    return children


def print_solution(result: Node|None) -> None:
    path: list = []
    while result is not None:
        path.append(result.value)
        result = result.parent

    path.reverse()
    for node in path:
        print(node)


# Main
if __name__ == "__main__":

    graph: dict[str, list[str]] = {
            "A":["B","C"],
            "B":["D","E"],
            "C":["F","G"],
            "F":["H","I"],
            "H":["J","K"],
            "I":["L","M"],
            "J":["N","O"],
            "K":["P","Q"],
            "L":["R","S"],
            "M":["T","U"],
            "N":["V","W"],
            "O":["X","Y"],
            "P":["Z"]
            }

    alphabet: Problem = Problem(graph, "A", "Z")
    result = breadth_first_search(alphabet)
    print_solution(result)


# # # # # # # # # #

# import heapq
# # Unsure what the evaluation function will be yet
# def best_first_search(problem: Problem, evaluation) -> Node | bool:
#     """Priority queue searching returning the """
#     start_node = Node(problem.initial_state(), None, None, 0)
#
#     frontier = []
#     heapq.heappush(frontier, (evaluation, start_node))
#     reached: dict = {start_node: start_node.cost}
#
#     while frontier:
#         priority, node = heapq.heappop(frontier)
#
#         if problem.is_goal(node.state):
#             return node 
#
#         children: list[Node] = expand(problem, node)
#         for child in children:
#             if child not in reached or child.cost < reached[child].cost:
#                 reached[child] = child.cost 
#                 frontier.append(child)
#
#     return False
#
#
#
# # # TODO
# # def uniform_search() -> None: 
# #     pass 
# #
# #
# # # TODO
# # def depth_first_search() -> None:
# #     pass 
# #
# #
