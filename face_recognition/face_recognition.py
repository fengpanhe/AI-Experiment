from PIL import Image
import os
import random
import matplotlib.pyplot as plt
import numpy as np

from Network import Network
from config import configs

DIRECTION = ['left', 'straight', 'up', 'right']
NAME = [
    'an2i', 'at33', 'boland', 'bpm', 'ch4f', 'cheyer', 'choon', 'danieln',
    'glickman', 'karyadi', 'kawamura', 'kk49', 'megak', 'mitchell', 'night',
    'phoebe', 'saavik', 'steffi', 'sz24', 'tammo'
]
SMILIES = ['neutral', 'angry', 'happy', 'sad']
SUNGLASSES = ['sunglasses', 'open']
FACETYPE = ['face_name', 'face_direction', 'face_smilies', 'face_sunglasses']


def read_img(img_path):
    im = Image.open(img_path).convert("L")
    arr = np.array(list(im.getdata()))
    return arr


pass


def get_imgs_path(dir_path):
    if not os.path.exists(dir_path):
        print("Error:IMGPATH is path not exists")
        exit()
    img_list = []
    list_dir = os.listdir(dir_path)
    for dir in list_dir:
        current_dir_path = dir_path + dir + '/'
        # 获取当前目录下的图片名
        dir_img_name_list = os.listdir(current_dir_path)
        for img_name in dir_img_name_list:
            strs = img_name.split('_')
            if not strs[0] in NAME:
                NAME.append(strs[0])
            if not strs[1] in DIRECTION:
                DIRECTION.append(strs[1])
                pass
            if not strs[2] in SMILIES:
                SMILIES.append(strs[2])
            if not strs[3] in SUNGLASSES:
                SUNGLASSES.append(strs[3])
            img_list.append(current_dir_path + img_name)

    print(DIRECTION)
    print(NAME)
    print(SMILIES)
    print(SUNGLASSES)
    return img_list


pass


def get_imgs(img_paths):
    imgs = []
    names = []
    directions = []
    smilies = []
    sunglasses = []
    # 取出要处理的img
    # print(img_paths)
    for img_path in img_paths:

        img_val = read_img(img_path)
        imgs.append(img_val)

        face_name = np.ones(len(NAME)) / 10
        face_direction = np.ones(len(DIRECTION)) / 10
        face_smilies = np.ones(len(SMILIES)) / 10
        face_sunglasses = np.ones(len(SUNGLASSES)) / 10

        strs = img_path.split('/')[-1].split('_')
        face_name[NAME.index(strs[0])] = 0.9
        face_direction[DIRECTION.index(strs[1])] = 0.9
        face_smilies[SMILIES.index(strs[2])] = 0.9
        face_sunglasses[SUNGLASSES.index(strs[3])] = 0.9

        names.append(face_name)
        directions.append(face_direction)
        smilies.append(face_smilies)
        sunglasses.append(face_sunglasses)
    pass

    return_val = {
        'imgs': np.array(imgs),
        'face_name': np.array(names),
        'face_direction': np.array(directions),
        'face_smilies': np.array(smilies),
        'face_sunglasses': np.array(sunglasses)
    }
    return return_val


pass


def train_test(train_data,
               test_data,
               train_type,
               hidden_sigmoid_num=3,
               eta=0.3,
               momentum=0.3,
               train_times=100):
    '''
    train_data：训练数据
    test_data：测试数据 
    train_type：训练类型 
    hidden_sigmoid_num：隐藏单元数目 
    eta：学习率 
    momentum：冲量 
    train_times：训练次数
    '''
    input_sigmoid_num = train_data['imgs'].shape[1]
    output_sigmoid_num = train_data[train_type].shape[1]
    #初始化网络
    network = Network(
        3, [input_sigmoid_num, hidden_sigmoid_num,
            output_sigmoid_num], eta, momentum)

    train_diff_vals = np.zeros(train_times)
    test_diff_vals = np.zeros(train_times)
    train_errors_times = np.zeros(train_times)
    test_errors_times = np.zeros(train_times)
    for i in range(train_times):
        train_result = network.train(train_data['imgs'],
                                     train_data[train_type])

        train_diff_vals[i] = train_result['diff_val']
        train_errors_times[i] = train_result['error_times']

        test_result = network.test(test_data['imgs'], test_data[train_type])

        test_diff_vals[i] = test_result['diff_val']
        test_errors_times[i] = test_result['error_times']
    pass
    result_data = {
        'train_name':
        '( ' + str(hidden_sigmoid_num) + ', ' + str(eta) + ', ' + str(momentum)
        + ')',
        'train_diff_vals':
        train_diff_vals,
        'train_errors_times':
        train_errors_times,
        'test_diff_vals':
        test_diff_vals,
        'test_errors_times':
        test_errors_times
    }
    return result_data


def draw(results, train_data_size, test_data_size):
    result_datas = results['result_datas']
    graph_name = results['graph_name']
    colormap = plt.cm.Paired
    i = 0
    plt.figure(graph_name)
    for result_data in result_datas:
        train_diff_vals = result_data['train_diff_vals'] / (
            2 * train_data_size)
        test_diff_vals = result_data['test_diff_vals'] / (2 * test_data_size)
        train_errors_rate = 1 - result_data['train_errors_times'] / train_data_size
        test_errors_rate = 1 - result_data['test_errors_times'] / test_data_size
        plt.subplot(121)
        plt.plot(
            range(train_diff_vals.shape[0]),
            train_diff_vals,
            color=colormap(3),
            label='train_diff' + result_data['train_name'])
        plt.plot(
            range(test_diff_vals.shape[0]),
            test_diff_vals,
            color=colormap(5),
            label='test_diff' + result_data['train_name'])
        plt.subplot(122)
        plt.plot(
            range(train_errors_rate.shape[0]),
            train_errors_rate,
            color=colormap(3),
            label='train_rate' + result_data['train_name'])
        plt.plot(
            range(test_errors_rate.shape[0]),
            test_errors_rate,
            color=colormap(5),
            label='test_rate' + result_data['train_name'])
        i += 1
    plt.subplot(121)
    # plt.figure(graph_name + '_diff')
    plt.xlabel('训练次数')  # 给 x 轴添加标签
    plt.ylabel('误差')  # 给 y 轴添加标签
    plt.title(graph_name + '-误差相对权值的变化曲线')  # 添加图形标题
    plt.grid()
    plt.legend()

    plt.subplot(122)
    # plt.figure(graph_name + '_rate')
    plt.xlabel('训练次数')  # 给 x 轴添加标签
    plt.ylabel('正确率')  # 给 y 轴添加标签
    plt.title(graph_name + '-正确率相对训练次数的变化曲线')  # 添加图形标题
    plt.grid()
    plt.legend()


def main():
    img_name_list = get_imgs_path(configs['IMGPATH'])
    random.shuffle(img_name_list)

    train_data = get_imgs(img_name_list[:300])
    test_data = get_imgs(img_name_list[300:])

    train_data_size = len(train_data['imgs'])
    test_data_size = len(test_data['imgs'])

    print('训练集大小: ' + str(train_data_size))
    print('测试集大小: ' + str(test_data_size))

    plt.rcParams['font.sans-serif'] = ['SimHei']

    train_type = 'face_direction'
    result_datas = []

    result = train_test(train_data, test_data, train_type, 20, 0.3, 0.3, 100)

    result_datas.append(result)
    print('train_diff_vals: ' + str(result['train_diff_vals']))
    print()
    print('train_errors_times: ' + str(result['train_errors_times']))
    print('test_diff_vals: ' + str(result['test_diff_vals']))
    print('test_errors_times: ' + str(result['test_errors_times']))
    draw({
        'graph_name': train_type,
        'result_datas': result_datas
    }, train_data_size, test_data_size)

    plt.show()


if __name__ == '__main__':
    main()
