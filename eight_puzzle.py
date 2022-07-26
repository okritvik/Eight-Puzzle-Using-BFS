"""
@author Kumara Ritvik Oruganti
@brief This code is written as part of the project 1 of ENPM 661 to solve the 8 puzzle problem using Breadth First Search Algorithm.
"""
import copy

def print_matrix(state):
    """
    @brief This function prints the node in matrix form
    :parameter string type of node state
    :return none
    """
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")

def convert_to_2d_array(initial_state,state):
    """
    @brief: This function converts input string format to 2D array. It uses call by reference concept
    :param initial_state: 2D array
    :param state: string to be converted
    :return: none
    """
    for i in range(0,len(state)):
        initial_state[i%3].append(int(state[i]))

def check_validity_of_input(state):
    """
    @brief: Checks if the inputs are valid.
    :param state: input in string
    :return: boolean
    """
    sum = (8*9)/2
    if(len(state)>9):
        return False
    else:
        for i in range(len(state)):
            sum = sum - int(state[i])
        if(sum==0):
            return True
        else:
            return False

def take_inputs():
    """
    @brief: This function takes the initial node state and final node state to solve the puzzle
    :return: Initial state and final state of the puzzle to be solved
    """
    initial_state = [[],[],[]]
    print("Enter the initial State as String (Column - Wise)")
    while True:
        state = input()
        if(check_validity_of_input(state)):
            break
        else:
            print("Enter Valid Initial State")
    # print_matrix(state)

    convert_to_2d_array(initial_state,state)
    # print(initial_state)
    final_state = [[],[],[]]
    print("Enter the Final State as String (Column - Wise)")
    while True:
        state = input()
        if(check_validity_of_input(state)):
            break
        else:
            print("Enter Valid Final State")
    convert_to_2d_array(final_state,state)
    return initial_state,final_state

def convert_to_string(state):
    """
    @brief: This function converts 2D array to string format
    :param state: 2D array format of the node state
    :return: string format of the node state
    """
    s = ""
    for i in range(3):
        for j in range(3):
            s+=str(state[j][i])
    # print(s)
    return s

def find_position(curr_node):
    """
    @brief: This function finds the position of the blank tile.
    :param curr_node: Node state
    :return: Position of the blank tile
    """
    for i in range(0,3):
        for j in range(0,3):
            if(curr_node[i][j]) == 0:
                return i,j

def print_to_file(string_node, file):
    """
    @brief: This function prints the node to file
    :param string_node: string representation of the node state
    :param file: file to which the node state has to be written
    :return: None
    """
    for i in range(len(string_node)):
        file.write(string_node[i]+" ")
    file.write("\n")

def print_to_file_node_index(string_node,nodes_info,dict,idx):
    """
    @brief: This function writes the node index and parent index of the node state to the file
    :param string_node: string representation of the node
    :param nodes_info: file to which the node state has to be written
    :param dict: dictionary of node states as key with corresponding node indices and parent node indices as the values
    :param idx: node index of the node_state
    :return: None
    """
    _, pi = dict[string_node]
    nodes_info.write("        "+str(idx)+"           "+str(pi))
    nodes_info.write("\n")

def action_move_up(node):
    """
    @brief: This function checks if the upward movement is possible for the blank tile current position
    :param node: present node state
    :return: boolean (true if upward movement is possible, false otherwise) and the generated node(same state if next state is not possible)
    """
    current_node = copy.deepcopy(node)
    x,y = find_position(current_node)
    # print(x,y)
    if((x-1)<3 and (x-1)>=0):
        current_node[x][y], current_node[x-1][y] = current_node[x-1][y], current_node[x][y]
        return True,current_node
    else:
        return False,current_node

def action_move_down(node):
    """
    @brief: This function checks if the downward movement is possible for the blank tile current position
    :param node: present node state
    :return: boolean (true if downward movement is possible, false otherwise) and the generated node(same state if next state is not possible)
    """
    current_node = copy.deepcopy(node)
    x,y = find_position(current_node)
    if((x+1)<3 and (x+1)>=0):
        current_node[x][y], current_node[x+1][y] = current_node[x+1][y], current_node[x][y]
        return True,current_node
    else:
        return False,current_node

def action_move_left(node):
    """
    @brief: This function checks if the left movement is possible for the blank tile current position
    :param node: present node state
    :return: boolean (true if left movement is possible, false otherwise) and the generated node(same state if next state is not possible)
    """
    current_node = copy.deepcopy(node)
    x,y = find_position(current_node)
    if((y-1)<3 and (y-1)>=0):
        current_node[x][y], current_node[x][y-1] = current_node[x][y-1], current_node[x][y]
        return True,current_node
    else:
        return False,current_node

def action_move_right(node):
    """
    @brief: This function checks if the right movement is possible for the blank tile current position
    :param node: present node state
    :return: boolean (true if upward movement is possible, false otherwise) and the generated node(same state if next state is not possible)
    """
    current_node = copy.deepcopy(node)
    x,y = find_position(current_node)
    # print(x,y)
    if((y+1)<3 and (y+1)>=0):
        current_node[x][y], current_node[x][y+1] = current_node[x][y+1], current_node[x][y]
        return True,current_node
    else:
        return False,current_node

def perform_actions(node,final_string,node_index,parent_node_index,queue,dict):
    """
    @brief: This function performs four possible actions (Left, Right, Up, Down) movement of the blank tile
    :param node: present node state
    :param final_string: goal state in string type
    :param node_index: present node index
    :param parent_node_index: parent node index of the present state
    :param queue: queue to store the valid generated children
    :param dict: dictionary to store the key value pair
    :return: boolean flag and the node index
    """
    status, ret_node = action_move_left(node)
    if status:
        # print("Left Node generated")
        if (convert_to_string(ret_node) == final_string):
            # print("GOAL REACHED Left")
            dict[final_string] = [node_index + 1, parent_node_index]
            return True,node_index
        if convert_to_string(ret_node) not in dict:
            queue.append(ret_node)
            # print("Appended",ret_node)
            # print("QUEUE NOW",queue)
            node_index = node_index + 1
            # print("Present Node Index : ", node_index)
            dict[convert_to_string(ret_node)] = [node_index, parent_node_index]

    status, ret_node = action_move_right(node)
    if status:
        # print("Right node generated")
        if (convert_to_string(ret_node) == final_string):
            # print("GOAL REACHED Right")
            dict[final_string] = [node_index + 1, parent_node_index]
            return True,node_index
        if convert_to_string(ret_node) not in dict:
            queue.append(ret_node)
            # print("Appended", ret_node)
            node_index = node_index + 1
            # print("Present Node Index : ", node_index)
            dict[convert_to_string(ret_node)] = [node_index, parent_node_index]

    status, ret_node = action_move_up(node)
    if status:
        # print("Up node generated")
        if (convert_to_string(ret_node) == final_string):
            # print("GOAL REACHED Up")
            dict[final_string] = [node_index + 1, parent_node_index]
            return True,node_index
        if convert_to_string(ret_node) not in dict:
            queue.append(ret_node)
            # print("Appended", ret_node)
            # print("QUEUE NOW", queue)
            node_index = node_index + 1
            # print("Present Node Index : ", node_index)
            dict[convert_to_string(ret_node)] = [node_index, parent_node_index]

    status, ret_node = action_move_down(node)
    if status:
        # print("Down node generated")
        if (convert_to_string(ret_node) == final_string):
            # print("GOAL REACHED Down")
            dict[final_string] = [node_index + 1, parent_node_index]
            return True,node_index
        if convert_to_string(ret_node) not in dict:
            queue.append(ret_node)
            # print("Appended", ret_node)
            node_index = node_index + 1
            # print("Present Node Index : ", node_index)
            dict[convert_to_string(ret_node)] = [node_index, parent_node_index]
    return False,node_index

def solve_puzzle(initial,final):
    """
    @brief: This function searches for the final goal state using the BFS algorithm.
    :param initial: Initial state (START State)
    :param final: Final state (GOAL State)
    :return:None
    """
    back_tracking = False
    final_string = convert_to_string(final)
    visited_nodes = []
    queue = []
    node_index = 0
    parent_node_index = 0
    node_to_back_track = None
    dict = {}
    # print(dict)
    queue.append(initial)
    if(convert_to_string(initial) == final_string):
        print("GOAL IS SAME AS START NODE")
    else:
        while True:
            if(len(visited_nodes)==0):
                node_state = queue.pop(0)
                dict[convert_to_string(node_state)] = [node_index,parent_node_index]
                visited_nodes.append(convert_to_string(node_state))
                # Actions start
                found_goal,index = perform_actions(node_state,final_string,node_index,parent_node_index,queue,dict)
                node_index = index
                #print(node_index)
                if(found_goal):
                    back_tracking = True
                    visited_nodes.append(final_string)
                    break
            else:
                # print("Else Queue",queue)
                if(len(queue) != 0):
                    node_state = queue.pop(0)
                    n_i,_ = dict[convert_to_string(node_state)]
                    parent_node_index = n_i
                    visited_nodes.append(convert_to_string(node_state))
                    found_goal,index = perform_actions(node_state, final_string, node_index, parent_node_index, queue,dict)
                    node_index = index
                    #print(node_index)
                    if (found_goal):
                        back_tracking = True
                        visited_nodes.append(final_string)
                        break
                else:
                    #print("Cannot find the required goal")
                    print("Number of nodes searched: ",node_index)
                    break
    back_track(final_string,dict,visited_nodes,back_tracking)

    #Printing to files
    nodes = open("Nodes.txt","w")
    nodes_info = open("NodesInfo.txt","w")
    nodes_info.write("Node_Index    Parent_Node_Index"+"\n")
    for i in range(len(visited_nodes)):
        string_node = visited_nodes[i]
        print_to_file(string_node,nodes)
        print_to_file_node_index(string_node,nodes_info,dict,i)
    nodes_info.close()
    nodes.close()
def back_track(final_string,dict,visited_nodes,back_tracking):
    node_path = open("nodePath.txt", "w")
    if(back_tracking):
        # print(dict)
        node = final_string
        stack = []
        stack.append(node)

        while True:
            _,p_n = dict[node]
            if(p_n == 0):
                stack.append(visited_nodes[p_n])
                break
            else:
                stack.append(visited_nodes[p_n])
                node = visited_nodes[p_n]
        while(len(stack)>0):
            node_string = stack.pop()
            print_matrix(node_string)
            print_to_file(node_string,node_path)
    else:
        print("The puzzle cannot be solved")
    node_path.close()

def control_flow():
    initial,final = take_inputs()
    solve_puzzle(initial,final)

if __name__ == '__main__':
    control_flow()