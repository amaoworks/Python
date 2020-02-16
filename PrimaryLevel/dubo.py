from random import randint

user_money = int(input('请输入你要多少钱? \n'))
host_money =50000


while user_money > 0 and host_money > 0:
    print('你的总资产为:', user_money)
    print('庄家的总资产为', host_money)

    debt = int(input('请下注: '))
    while debt > user_money:
            debt = int(input('请重新下注: '))
    user = randint(1, 10)
    host = randint(1, 10)
    print('乐乐摇出了%d点' % user)
    print('庄家摇出了%d点' % host)
    
    if user >= host:
        print('乐乐大')
        user_money += debt
        host_money -= debt
    else:
        print('庄家大')
        user_money -= debt
        host_money += debt

if host_money <= 0:
    print('乐乐你赢了')

if user_money <= 0:
    print('乐乐你输了')