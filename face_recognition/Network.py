
import numpy as np
from Layer import Layer
class Network(object):

    def __init__(self, layer_num, layer_nodes_num, eta, momentum):
        self.layer_num = layer_num
        self.eta = eta
        self.momentum = momentum
        self.layer = []
        # 输入层
        self.layer.append(Layer('input_layer'))
        # 隐藏层
        for i in range(1, layer_num - 1):
            self.layer.append(
                Layer('hidden_layer',layer_nodes_num[i],layer_nodes_num[i-1])
                )
        pass
        # 输出层
        self.layer.append(
            Layer('output_layer',layer_nodes_num[layer_num - 1],layer_nodes_num[layer_num - 2])
            )
        pass
    pass


    def train(self, input_date, correct_result):
        error_times = 0
        diff_val = 0
        for input_val, out_put in zip(input_date, correct_result):
            # 正向传播
            self.layer[0].layer_predict(input_val)
            for j in range(1, self.layer_num):
                # print('j = ' + str(j))
                self.layer[j].layer_predict(self.layer[j - 1].outputs)
            pass
            # 反向求delta
            # print('output' + str(out_put))
            self.layer[self.layer_num - 1].calc_delta(out_put)
            for j in range(2, self.layer_num):
                # print('w')
                # print(self.layer[self.layer_num - j + 1].sigmoids[0].weights)
                # print(self.layer[self.layer_num - j + 1].sigmoids[1].weights)
                # print(self.layer[self.layer_num - j + 1].sigmoids[2].weights)
                # print(self.layer[self.layer_num - j + 1].sigmoids[3].weights)
                self.layer[self.layer_num - j].calc_delta(self.layer[self.layer_num - j + 1])
            pass
            # self.layer[1].print_delta()
            # self.layer[2].print_delta()
            # 更新权值
            for j in range(1, self.layer_num):
                self.layer[j].update_weights(self.layer[j - 1].outputs, self.eta, self.momentum)
            pass
            predict_val = self.layer[self.layer_num - 1].outputs
            
            if not np.argmax(predict_val) == np.argmax(out_put):
                # print(predict_val)
                # print(out_put)
                # print('---------')
                error_times += 1
                
            diff_val += np.sum(np.square(predict_val - out_put))
        pass
        # for layer in self.layer:
        #     layer.print_weights()
        # self.layer[self.layer_num - 1].print_weights()
        return {'error_times':error_times,"diff_val":diff_val}

    def test(self,input_date, correct_result):
        error_times = 0
        diff_val = 0
        for input_val, out_put in zip(input_date, correct_result):
            self.layer[0].layer_predict(input_val)
            for j in range(1, self.layer_num):
                # print('j = ' + str(j))
                self.layer[j].layer_predict(self.layer[j - 1].outputs)
            pass
            predict_val = self.layer[self.layer_num - 1].outputs

            if not np.argmax(predict_val) == np.argmax(out_put):
                error_times += 1
            diff_val += np.sum(np.square(predict_val - out_put))
        pass
        return {'error_times':error_times,"diff_val":diff_val}
pass