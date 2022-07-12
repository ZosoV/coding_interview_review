
# CLASS definition
# I going to store a list of nodes, where each node is the absolute position
# with only alive cells

# Store also the left-top most position and right-bottom most position
# to plot and perform update rules

# PLOT
# To draw I want to take just the interest zone + a border bound
# but I have to move the left-top most point to 0.0


# UPDATES
# Always I have to check the rules with a previous copy of our environment
# to avoid bad updates

# Also, I have to consider just the interest zone + a border bound

# Update steps
# 1. iterate through all the interest zone + border bound
# 2. check rules -> check alive node if node in list_nodes
# 3. update add/remove nodes from list_nodes


class GameOfLife():

    def __init__(self, steps, list_nodes) -> None:
        
        self.steps = steps
        self.list_nodes = list_nodes

        self.corners()

    def corners(self):
    # Find the corners -> better way?
        min_sum = float('inf')
        max_sum = float('-inf')
        for (x,y) in self.list_nodes:
            
            if min_sum > x + y:
                min_sum = x + y
                left_top = (x,y)

            if max_sum < x + y:
                max_sum = x + y
                righ_bottom = (x,y)

        self.left_top = left_top
        self.righ_bottom = righ_bottom

    def plot():
        # plot with a border

    def update():
        # chec the rules and update