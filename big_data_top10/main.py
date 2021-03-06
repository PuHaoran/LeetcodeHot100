""" 编程题1
前序遍历二叉树，遍历过程中记录遍历的路径，若递归终止则判断当前路径和是否最大并记录最大值和路径信息。
"""
class TreeNode(object):
    """ 定义二叉树节点 """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def main(tree):
    global _sum, res  # 当前路径和的最大值
    res, path = [], []
    _sum = float('-inf')

    def dfs(root, path):
        global _sum, res
        if not root:
            t = sum(path)
            if t > _sum:
                _sum = t
                res = path.copy()
            return
        path.append(root.val)
        dfs(root.left, path)
        dfs(root.right, path)
        path.pop()
    dfs(tree, path)
    return res


tree = TreeNode(1)
l = TreeNode(3)
r = TreeNode(2)
tree.left = l
tree.right = r
l.left = TreeNode(5)
r.left = TreeNode(6)
print(main(tree))

""" 编程题2
先将文件分成25份，然后存在磁盘上，再25路做归并，对归并后得文件进行一遍遍历即可找出前Top10的URL。
"""
def split_file(org_file_path, file_count=3):
    """ 将原始文件划分为多个小文件 """
    i = 0
    with open(org_file_path, mode="r", encoding="utf-8") as f:
        for line in f:
            with open('./data/split_data{}.txt'.format(i % file_count), 'a') as outfile:
                outfile.write(line)
            i += 1


def sorted_file_data(file_count=3):
    """ 将小文件内的数据进行排序操作 """
    for i in range(file_count):
        with open('./data/split_data{}.txt'.format(i), mode="r", encoding="utf-8") as f:
            lines = f.readlines()
        # 排序
        lines = sorted(lines)
        with open('./data/split_data{}.txt'.format(i), mode="w", encoding="utf-8") as f:
            f.seek(0)
            f.truncate()
        # 保存到小文件中
        for line in lines:
            with open('./data/split_data{}.txt'.format(i % file_count), 'a') as outfile:
                outfile.write(line)


def merge_file(file_count=3):
    """ 多路归并并返回top_k多的url """
    input_files = [open('./data/split_data{}.txt'.format(f)) for f in range(file_count)]
    output_file = open('./data/result.txt', 'a+')
    data_dict = {}  # 存储当前指针指向值
    for f in input_files:
        line = f.readline()
        if line:
            data_dict[f] = line
    while data_dict:
        f, data = min(data_dict.items(), key=lambda x: x[1])
        output_file.write(data)
        line = f.readline()
        if line:
            data_dict[f] = line
        else:
            del data_dict[f]
    output_file.write('end')


def get_top_k(top_k=3):
    result_file = open('./data/result.txt', 'r')
    pre = '-1'
    cnt = 0
    d = {}
    for line in result_file:
        if line != pre:
            if len(d) < top_k:
                d[pre] = cnt
            else:
                _data, _count = min(d.items(), key=lambda x: x[1])
                if cnt > _count:
                    del d[_data]
                    d[pre] = cnt
            cnt = 1
            pre = line
        else:
            cnt += 1
    return list(d.keys())


def main():
    org_file_path = "./data.txt"
    split_file(org_file_path)
    sorted_file_data(file_count=3)
    merge_file(file_count=3)
    result = get_top_k(top_k=3)
    return result


main()
""" 数学题目1
随机在线段上标p1,p2类似在一个直角坐标系上找到|x-y|<=0.5的值，即x-y<=0.5(x<=y)，(y-x)<=0.5(x<y)；在图像上绘制后可得面积为3/4.
"""

""" 数学题目2
1）先对药瓶编号，依次取出对应编号数量的药品(eg:1,2,3...10)，然后对这些药品称重得到重量m，result = (55-m)/0.1，然后找到编号为result的一个瓶子。
2）核心思路同上，先对药品编号，但要保证药品的两两编号和与其他两两药品编号和不重复（eg:1 2 3 5 8 13 21 34 55 89)，result = (取出的药品数量-取出的药品和)/0.1，然后找到编号和为result的两个瓶子。
"""