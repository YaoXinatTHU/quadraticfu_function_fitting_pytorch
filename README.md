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
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/tanh*2.png)

Tanh + ReLU
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/tanh+relu.png)

Sigmoid + Tanh
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/sigmoid+tanh.png)

Sigmoid + Sigmoid
![image](https://github.com/YaoXinatTHU/quadraticfu_function_fitting_pytorch/blob/master/images_folder/sigmoid*2.png)

蓝色的点是真实函数中采样出来的，红色的线是神经网络拟合出来的结果。

很容易看到的是：

1、在训练集的区域内[-1,1]，除了sigmoid + sigmoid 激活函数组合外，其他都拟合得很好。

2、在训练集的区间外几乎无一例外的GG了。

3、sigmoid + sigmoid的激活函数组合直接失败了，跑了好几次基本都是这个结果，所以应该不是网络的初始值的问题。

从这个有限规模的实验上来看，有如下结论：
1、“神经网络有理论上能拟合任何函数的的能力”在数据空间比较小的时候是没问题的（数据范围比较大的时候等main2.py的分析）。但是这个拟合其实是很盲目的，参见2。

2、而在训练数据看不见的地方（[-1,1]以外的区域），模型就表现得辣眼睛了。这应该是因为神经网络拟合出来的函数其实并不是`$y=x^2+1$`本身，而是在训练集的区域内，用了很多模型能表示的分段函数去近似它。（很明显的是relu+relu的模型中，拟合出来的线其实是由几条直线构成的），这种拟合其实有点记住训练数据的意思，泛化能力不好是正常的。毕竟在数据量有限的情况下，模型不太好预测真实数据的分布（就[-1,1]区间的数据，从`$y=x^2+1$`采样的数据和从`$y=|x|+1$`采样的数据并没有太大差别）。随后会扩大数据范围看看模型的表现。目测只用很多分段函数来近似的方法都不会好。

3、sigmoid + sigmoid的函数表现不好的原因暂时没想到，照例来说它和tanh应该差不多。目前猜测是因为sigmoid的取值范围只在[0,1]之间吧？但是为什么拟合出的总是一条直线(？或者是近似直线？)这个还是没想清楚。
