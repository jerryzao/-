#coding=utf8
#额...这是一个计算上海五险一金啊 个人所得税啊  税后的实际收入~
class GZJXQ():
    def __init__(self):
        pass

    def fivexianandonejing(self,x):
        if x >= 3022:
            n = float(x * 0.175)
        else:
            n = float(453.3 + x * 0.07)
        return n


    def koushui(self,m):
        if m < 3500:
            m = 0
        elif m - 3500 <= 1500:
            m = (m -3500) * 0.03
        elif 1500 < m - 3500 <= 4500:
            m = (m - 3500 - 1500) * 0.1 + 1500 * 0.03
        elif 4500 < m - 3500 <= 9000:
            m = (m - 3500 -4500) * 0.2 + 1500 * 0.03+3000 * 0.1
        elif 9000 < m - 3500 <= 35000:
            m = (m - 3500 -9000) * 0.25 + 1500 * 0.03 + 3000 * 0.1 + 4500 * 0.2
        elif 35000 < m -3500 <= 55000:
            m = (m - 3500 - 35000) * 0.3 + 1500 * 0.03 + 3000 * 0.1 + 4500 * 0.2 + 26000 * 0.25
        elif 55000 < m - 3500 <= 80000:
            m = (m -3500 - 55000) * 0.35 + 1500 * 0.03 + 3000 * 0.1 + 4500 * 0.2 + 26000 * 0.25 + 20000 * 0.3
        elif m - 3500 > 80000:
            m = (m -3500 -80000) * 0.45+ + 1500 * 0.03 + 3000 * 0.1 + 4500 * 0.2 + 26000 * 0.25 + 20000 * 0.3 + 25000 * 0.35
        return float(m)

    def go(self):
        x = input('输入你的基本工资:')
        y = input('输入你的奖金部分:')
        x = float(x)
        y = float(y)
        n = GZJXQ().fivexianandonejing(x)

        m = x + y - n
        m = GZJXQ().koushui(m)

        s = float(x + y - n - m)

        print u'税后实际收入:', s
        print u'个人缴纳五险一金部分:', n
        print u'需要缴纳个人所得税:', m



if __name__ == '__main__':
    GZJXQ().go()



