import torch.nn as nn
import torch
import torch.utils.data
import torch.optim as optim
from torch.autograd import Variable
import matplotlib.pyplot as plt

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.nn = nn.Sequential(
            nn.Linear(1,50),
            nn.ReLU(),
            nn.Linear(50, 10),
            nn.ReLU(),
            nn.Linear(10,1),
        )
    def forward(self, input):
        return self.nn(input)

if __name__ == '__main__':
    n = Net()
    print(n)
    input = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
    output = torch.pow(input,2) + 1
    ds = torch.utils.data.TensorDataset(input,output)
    loader = torch.utils.data.DataLoader(ds,batch_size=20, shuffle=True)
    optimizer = optim.SGD(n.parameters(), lr=0.2)
    loss = torch.nn.MSELoss()
    for i in range(100):
        for batch_idx, (data, target) in enumerate(loader):
            data, target = Variable(data), Variable(target)
            out = n(data)
            optimizer.zero_grad()
            l = loss(out,target)

            l.backward()
            optimizer.step()
            print('loss[%d/100]:%f' % (i, l))
        out = n(Variable(input,requires_grad = False))
        if i % 5 == 0:
            # plot and show learning process
            plt.cla()
            plt.scatter(input.numpy(), output.numpy())
            plt.plot(input.numpy(), out.data.numpy(),'r-')
            plt.text(0.5, 0, 'Round %d,Loss=%.4f' % (i,l.data[0]), fontdict={'size': 20, 'color':  'red'})
            plt.pause(0.5)
    plt.cla()
    input2 = torch.unsqueeze(torch.linspace(-2, 2, 100), dim=1)
    out_real = torch.pow(input2,2) + 1
    out2 = n(Variable(input2)).data
    plt.scatter(input2.numpy(), out_real.numpy())
    plt.plot(input2.numpy(), out2.numpy(), 'r-')
    plt.pause(5)
    #plt.show()
