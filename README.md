# quadraticfu_function_fitting_pytorch
A quadraticfu function fitting using pytorch



#
用一个全连接的二层隐藏层的神经网络去拟合一个二次函数的实验
训练数据是从`$y = x^2+1$`中在`$x \in [-1，1]$`范围内同间距采样的100个点
最后的测试数据是从`$x \in [-5，5]$`采样的200个点。
采用不同隐藏层激活函数的训练结果如下：

ReLU+ ReLU
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/relu.png)

Tanh + Tanh
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/tank*2.png)

Tanh + ReLU
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/tanh+relu.png)

Sigmoid + Tanh
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/sigmoid+tanh.png)

Sigmoid + Sigmoid
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/sigmoid*2.png)

