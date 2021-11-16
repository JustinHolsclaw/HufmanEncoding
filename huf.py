
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    
def sort_dict(new_dict):
    unsorted_dict = new_dict
    make_dict = sorted(unsorted_dict.items(), key=lambda x:x[1])
    sortdict = dict(make_dict)
    return sortdict

def create_node_list_from_dictionary(dictionary):
    nodes = []
    for item in dictionary.items():
        key, freq = item
        n = node(freq, key, None, None)
        nodes.append(n)
    return nodes

def sort_list(new_list):
    unsorted_list = new_list
    sorted_list = sorted(unsorted_list, key=lambda x:x.freq)
    return sorted_list

def HufCodec(new_dict):
    sorted_dict = sort_dict(new_dict)
    node_list = create_node_list_from_dictionary(sorted_dict)
    while(len(node_list) > 1):
        node_list=sort_list(node_list)
        high_freq = node_list[0].freq + node_list[1].freq
        node_list.append(node(high_freq, None, node_list[0], node_list[1]))
        node_list.pop(0)
        node_list.pop(0)
    return node_list        
    

practice = HufCodec(dict(
       h=1,
       b=2,
       j=2,
       a=3,
       e=4,
       g=5
    ))
for x in practice:
    print(x.freq)





    
#FOR ENCODING
def split_string(recieved_string):
    return [char for char in recieved_string]
