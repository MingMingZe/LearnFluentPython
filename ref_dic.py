def ref_dic():
    dic = {'1': 1, '2': [1, 3]}
    copy_dic = dic.copy()
    copy_dic['2'].append(3)
    print(dic)


def re_list():
    list = []
    list_copy = list.copy()
    list_copy.append([1,2])
    print(list)


if __name__ == '__main__':
    ref_dic()
    # re_list()
