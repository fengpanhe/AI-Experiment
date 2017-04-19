import numpy as np
import math

class Sigmoid(object):


    def __init__(self, weight_num):
        """
        weight_num:输入值个数
        """
        self.weights = np.random.random(weight_num + 1)/5 - 0.1
        self.dif_val = np.zeros(weight_num + 1)
        self.output = 0
        self.delta = 0

    def predict(self, input_val):
        """
        预测
        input:input_val(输入样本向量)
        output:预测结果
        """
        dot_val = np.dot(input_val, self.weights[1:]) + self.weights[0]
        self.output = 1/(1 + math.pow(math.e, -1 * dot_val))
        return self.output

    def calc_hidden_sigmoid_delta(self, next_layer_wd_sum):
        """
        计算隐藏单元的 误差delta
        """
        self.delta = self.output * (1 - self.output) * next_layer_wd_sum

    def calc_output_sigmoid_delta(self, label):
        """
        计算输出单元的 误差delta
        """
        self.delta = self.output * (1 - self.output) * (label - self.output)

    def update_weight(self, input_val, eta, momentum):
        """
        更新权值
        """
        self.dif_val[1:] = eta * self.delta * input_val + momentum * self.dif_val[1:]
        self.dif_val[0] = eta * self.delta + momentum * self.dif_val[0]
        self.weights += self.dif_val
pass