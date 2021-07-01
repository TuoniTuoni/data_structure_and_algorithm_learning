# -*-coding:utf-8-*-
class Node(object):
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def is_left(self):
        return self.father.left == self

    def __str__(self):
        return str(self.freq)


def create_nodes(freqs):
    """
    创建叶子节点
    :param freqs:
    :return:
    """
    return [Node(freq) for freq in freqs]


def create_huffman_tree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq+node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


def huffman_encoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.is_left():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes


if __name__ == '__main__':
    chars_freq = [('A', 35), ('B', 10), ('C', 20), ('D', 20), ('E', 15)]
    nodes = create_nodes([item[1] for item in chars_freq])
    print(nodes)
    root = create_huffman_tree(nodes)
    print(root)
    """
    demo = Node(100)
    print(demo)
    """
    print(root == Node(100))
    print(type(root))
    codes = huffman_encoding(nodes, root)
    print(codes)
    for item in zip(chars_freq, codes):
        print('Char:{}freq:{}encoding:{}'.format(item[0][0], item[0][1], item[1])) 
        
 
output(ran in google colab):
[<__main__.Node object at 0x7fd6e31d5c50>, <__main__.Node object at 0x7fd6e31d56d0>, <__main__.Node object at 0x7fd6e31d5910>, <__main__.Node object at 0x7fd6e31d51d0>, <__main__.Node object at 0x7fd6e31d5b90>]
100
False
<class '__main__.Node'>
['11', '100', '00', '01', '101']
Char:Afreq:35encoding:11
Char:Bfreq:10encoding:100
Char:Cfreq:20encoding:00
Char:Dfreq:20encoding:01
Char:Efreq:15encoding:101
