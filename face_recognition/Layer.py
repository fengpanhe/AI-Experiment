from Sigmoid import Sigmoid
import numpy as np
class Layer(object):

    def __init__(self, layer_type, sigmoid_num=0, weight_num=0):
        self.layer_type = layer_type
        self.sigmoid_num = sigmoid_num
        self.sigmoids = []
        self.outputs = np.zeros(sigmoid_num)
        if not layer_type == 'input_layer':
            for i in range(self.sigmoid_num):
                self.sigmoids.append(Sigmoid(weight_num))

    def layer_predict(self, input_val):
        '''' 
        通过感知单元计算预测值，保存到outputs
        '''
        if self.layer_type == 'input_layer':
            self.outputs = input_val/255
        else:
            for i in range(self.sigmoid_num):
                self.outputs[i] = self.sigmoids[i].predict(input_val)

    def calc_delta(self, param):
        ''' 调用感知单元的calc_delta函数计算delta'''
        if self.layer_type == 'hidden_layer':
            for i in range(self.sigmoid_num):
                next_layer_wd_sum = 0
                for next_layer_sigmoid in param.sigmoids:
                    # print(str(i) + 'next_layer_sigmoid: ' + str(next_layer_sigmoid.weights) + str(next_layer_sigmoid.delta))
                    next_layer_wd_sum += next_layer_sigmoid.weights[i + 1] * next_layer_sigmoid.delta
                # print('next_layer_wd_sum' + str(i) + str(next_layer_wd_sum))
                self.sigmoids[i].calc_hidden_sigmoid_delta(next_layer_wd_sum)
        elif self.layer_type == 'output_layer':
            
            for i in range(self.sigmoid_num):
                # print('param' + str(param) + str(param[i]))
                self.sigmoids[i].calc_output_sigmoid_delta(param[i])
            # self.print_delta()

    def update_weights(self, input_val, eta, momentum):
        ''' 更新权值'''
        # if self.layer_type == 'output_layer':
        #     print(input_val)
        for i in range(self.sigmoid_num):
            self.sigmoids[i].update_weight(input_val, eta, momentum)

    def print_weights(self):
        weights = []
        for sigmoid in self.sigmoids:
            weights.append(sigmoid.weights)
        print('w' + str(weights))

    def print_delta(self):
        deltas = []
        for sigmoid in self.sigmoids:
            deltas.append(sigmoid.delta)
        print(self.layer_type + 'deltas' + str(deltas))
pass