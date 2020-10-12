"""
2020/10/9_ChanWJ_GDUT   HeXF_GDUT
"""
import random
import fractions
import copy
"""
a + b
(a+b)+c
a+(b+c)  a b c称之为因子
"""


def operation_Chan_He(a, b, operation_symbol):
    #生成两位数的运算基础块，以后在此基础上生成多位数的运算
    P = "NOT"
    if (operation_symbol == "+"):
        result = a + b
        return result
    if (operation_symbol == "-"):
        if (a >= b):
            result = a - b
            return result
        else:
            return  P
    if (operation_symbol == "*"):
        result = a * b
        return result
    if (operation_symbol == "/"):
        result = a / b
        return result


# 产生因子
def factor_Chan_He():
    # 随机生成 自然数、真分数
    global max
    while (True):
        index = random.randint(1, 2)  # 随机生成1或者2  1就生成自然数因子，2就生成真分数因子
        if (index == 1):
            # 自然数,先设置为1到10
            int_cwj = random.randint(1, max)
            int_cwj_0 = fractions.Fraction(int_cwj)
            return int_cwj_0
            break
        if (index == 2):
            fenzi = random.randint(1, max)
            fenmu = random.randint(1, max)

            true_fraction = fractions.Fraction(fenzi, fenmu)
            if (true_fraction < 1):
                return true_fraction
                break


def product():
    #调用operation_Chan_He,factor_Chan_He函数生成两位数的式子
    two_index = []
    a = factor_Chan_He()
    b = factor_Chan_He()
    while (True):
        operation_symbol = random.choice('+-*/')
        # print(a, b, operation_symbol)
        result = operation_Chan_He(a, b, operation_symbol)
        # print(result)
        if(result != "NOT"):
            # print("可以")
            two_index.extend((a,b,operation_symbol))
            break

    return result,two_index


def start_Chan_He():
    #主体函数，设置随机flag，flag = 0时调用product生成两位数的式子
    #flag为其他数时生成不同类型的多位数式子（有的有括号，有的没括号）
    flag = random.randint(0,2)
    # flag = 2
    if (flag == 0):
        result,two_index = product()
        there.append(two_index)
        result_list.append(result)
        type_list.append(2)
        check.append(0)
        return result
    if (flag == 1):
        unio,two_index = product()
        #此时two_index = [1,2,"+"]
        # print("---------------------")
        c = factor_Chan_He()
        while (True):
            operation_symbol = random.choice('+-*/')
            pos = random.randint(0, 1)  # 0代表是unio + c 1代表c + unio
            # print(unio, c, operation_symbol)
            if (operation_symbol == "+"):
                result = unio + c
                break
            if (operation_symbol == "-"):
                if (pos == 0):
                    if (unio >= c):
                        result = unio - c
                        break
                elif (pos == 1):
                    if (c >= unio):
                        result = c - unio
                        break
                else:
                    continue
            if (operation_symbol == "*"):
                result = unio * c
                break
            if (operation_symbol == "/"):
                if (pos == 0 and c!=0):
                    result = unio / c
                    break
                if (pos == 1and unio!=0):
                    result = c / unio

                    break
        if(pos == 0):#括号在左边，即[2,1,3,"hav","left","-","/"]
            two_index.insert(2,c)
            two_index.insert(3,"hav")
            two_index.insert(4,"left")
            two_index.insert(6,operation_symbol)
            there.append(two_index)
        if(pos == 1):#括号在右边
            two_index.insert(0,c)
            two_index.insert(3,"hav")
            two_index.insert(4,"right")
            two_index.insert(5,operation_symbol)
            there.append(two_index)
        result_list.append(result)
        type_list.append(3)
        check.append(0)
        return result
    if (flag == 2):
        #a+b*c先右后左，其他按顺序来
        a = factor_Chan_He()
        b = factor_Chan_He()
        c = factor_Chan_He()
        there_index = []
        result = "NOT"
        while (True):
            #[2,1,3,"nohav","none","-","/"]
            operation_symbol_1 = random.choice('+-*/')  # 第一次运算符
            operation_symbol_2 = random.choice('+-*/')  # 第二次运算符
            # print(a, b, c, operation_symbol_1, operation_symbol_2)
            if ((operation_symbol_1 == "+" or operation_symbol_1 == '-') and (operation_symbol_2 == "*" or operation_symbol_2 == "/")):
                cwj = operation_Chan_He(b,c,operation_symbol_2)
                #先右后左
                if (cwj != "NOT"):

                    result = operation_Chan_He(a,cwj,operation_symbol_1)
            else:
                cwj = operation_Chan_He(a,b,operation_symbol_1)
                if(cwj != "NOT"):
                    result = operation_Chan_He(cwj,c,operation_symbol_2)

            if (result != "NOT"):
                there_index.extend((a,b,c,"nohav","none",operation_symbol_1,operation_symbol_2))
                there.append(there_index)
                break
        type_list.append(3)
        result_list.append(result)
        check.append(0)
        return result

def repeat_Chan_He(m):
    #查询重复率
    there_copy =[]
    there_copy = copy.deepcopy(there)
    repeat = []
    repeat_index = []
    length = len(result_list)
    for u in range(length):

        if(len(there_copy[u]) == 7):
            del there_copy[u][4]  #!!!!!!!!!!1111
            del there_copy[u][3]

        len1 = len(there_copy[u])
        for t in range(len1):
            there_copy[u][t] = str(there_copy[u][t])
    # print(there_copy)
    for j in range(length):
        # print(j,there_copy[j])
        repeat_j = []
        repeat_j.append(j)
        if(check[j] == 0):

            for k in range(0,length):

                d1 = sorted(there_copy[j])
                d2 = sorted(there_copy[k])

                if(result_list[j] == result_list[k] and type_list[j] == type_list[k] and j!=k):
                    # print(j,k)
                    #结果相同且位数相同
                    if(d1 == d2):
                        repeat_j.append(k)
                        # there_copy[k] = "nothing"
                        check[k] = 1
            check[j] = 1

        repeat.append(repeat_j)

    for q in range(length):
        if(len(repeat[q]) > 1):
            # print(q)
            len_o = len(repeat[q])
            for y in range(1,len_o):
                index_o = repeat[q][y]
                # print(index_o)
                repeat[index_o] = str(0)
                repeat_index.append(index_o)
    repeat_index.sort(reverse=True)
    for jj in range(len(repeat_index)):
        del there[repeat_index[jj]]
        del result_list[repeat_index[jj]]
        del type_list[repeat_index[jj]]
        del check[jj]
        m = m-1

    return m
def reset_result():
    #结果进行转化（假分数转化成真分数，并存储结果）
    a0 = open('Answers.txt', 'w', encoding='utf-8')
    a0.write('答案如下' + '\n')
    a0.close()
    result_list_new = copy.deepcopy(result_list)
    len_result = len(result_list_new)
    for i in range(len_result):
        i_1 = i+1
        result_list_A_kid = result_list_new[i]
        result_list_A_kid_up = result_list_A_kid.numerator #分子
        result_list_A_kid_down = result_list_A_kid.denominator #分母
        if (result_list_A_kid_up>result_list_A_kid_down):
            #假分数
            result_int = result_list_A_kid_up//result_list_A_kid_down #带分数整数部分
            result_list_A_kid_up_new = result_list_A_kid_up%result_list_A_kid_down  #新的分子
            if(result_list_A_kid_up_new == 0):
                result_list_new[i] = str(result_int)
            else:
                result_list_new[i] = str(result_int) + str("'") + str(fractions.Fraction(result_list_A_kid_up_new, result_list_A_kid_down))
            a0 = open('Answers.txt', 'a', encoding='utf-8')
            a0.write("第%d题答案    "%i_1)
            a0.write(result_list_new[i] + '\n')
        else:
            #真分数
            result_list_new[i] = str(result_list[i])
            a0 = open('Answers.txt', 'a', encoding='utf-8')
            a0.write("第%d题答案    " % i_1)
            a0.write(result_list_new[i] + '\n')



def start(n):
    #启动函数，开始生成式子和查重

    for i in range(n):
        a = start_Chan_He()
    n_0 = repeat_Chan_He(n)


    while(True):
        if(n_0 == n):
            break
        else:
            for oo in range(n-n_0):
                start_Chan_He()

            n_0 = repeat_Chan_He(n)


if __name__ == '__main__':
    n = int(input("生成题目的个数:"))
    max = int(input("请输入题目中数值的范围:"))

    there = []# 式子的具体信息    [2,1,3,"hav","left","-","*",1]
                                #there[3] = hav有括号 nohav无括号
                                #there[4] = left代表括号将第一第二个数括起来
                                #(2-1)*3  最后一位代表序号
    result_list = []            #结果的信息，但没经过转化，包含假分数
    type_list = []              #式子的项数
    result_list_new = []        #最终结果，此时元素全是str类型（为了拼接最终表达式）
    there_kid_str = [None]*n    #最终式子，此时元素全是str类型（为了拼接最终表达式）
    check = []                  #查询标志，0是表示没被查过，1代表已经查询过，避免重复查询
    start(n)
    # print(there)
    # print(result_list)
    # print(type_list)
    len_list = len(there)
    # print(len_list)
    b0 = open('Exercises.txt', 'w', encoding='utf-8')
    b0.write('题目如下，一共%d道题目'%n + '\n')
    b0.close()
    for index in range(len_list):
        #[[Fraction(8, 1), Fraction(1, 7), Fraction(5, 1), 'hav', 'left', '*', '/'],
        # [Fraction(1, 2), Fraction(1, 5), Fraction(3, 5), 'nohav', 'none', '-', '*']
        #[Fraction(4, 1), Fraction(1, 1), '+']
        index_1 = index+1
        index_pro = "第%d题:      " % index_1
        there_kid = there[index]
        there_kid_len = len(there_kid)  #7  3
        if(there_kid_len == 7):
            #处理三位数
            there_kid_a = there_kid[0]              #a
            there_kid_b = there_kid[1]              #b
            there_kid_c = there_kid[2]              #c
            there_kid_operation1 = there_kid[5]     #运算符1
            there_kid_operation2 = there_kid[6]     #运算符2
            if(there_kid_operation1 == "/"):
                there_kid_operation1 = "÷"
            if(there_kid_operation1 == "*"):
                there_kid_operation1 = "×"
            if (there_kid_operation2 == "/"):
                there_kid_operation2 = "÷"
            if (there_kid_operation2 == "*"):
                there_kid_operation2 = "×"
            if(there_kid[3] == "hav"):
                #有括号
                if(there_kid[4] == "left"):
                    #括号在左边 如(a+b)*c
                    there_kid_str[index] = index_pro+str("(")+str(there_kid_a)+there_kid_operation1+str(there_kid_b)+str(")")\
                                    +there_kid_operation2+str(there_kid_c)+str(" ")+str("=")+str(" ")
                    b0 = open('Exercises.txt', 'a', encoding='utf-8')
                    b0.write(there_kid_str[index] + '\n')
                    print(there_kid_str[index])

                else:
                    #括号在右边 如a/(b-c)
                    there_kid_str[index] = index_pro+str(there_kid_a)+there_kid_operation1+str("(")+str(there_kid_b)\
                                    +there_kid_operation2+str(there_kid_c)+str(")")+str(" ")+str("=")+str(" ")
                    b0 = open('Exercises.txt', 'a', encoding='utf-8')
                    b0.write(there_kid_str[index] + '\n')
                    print(there_kid_str[index])

            else:
                #没有符号
                there_kid_str[index] = index_pro+str(there_kid_a)+there_kid_operation1+str(there_kid_b)+there_kid_operation2+str(there_kid_c)+str(" ")+str("=")+str(" ")
                b0 = open('Exercises.txt', 'a', encoding='utf-8')
                b0.write(there_kid_str[index] + '\n')
                print(there_kid_str[index])


        if(there_kid_len == 3):
            #两位数
            there_kid_a = there_kid[0]
            there_kid_b = there_kid[1]
            there_kid_operation = there_kid[2]
            there_kid_str[index] = index_pro+str(there_kid_a)+there_kid_operation+str(there_kid_b)+str(" ")+str("=")+str(" ")
            b0 = open('Exercises.txt', 'a', encoding='utf-8')
            b0.write(there_kid_str[index] + '\n')
            print(there_kid_str[index])
    reset_result()
