#Project Euler解题专用Fibonacci库
#作者: Frank-Deng-WH6HS <enter_the_dragon@foxmail.com>

import numbers; 
from fractions import Fraction; 
from SpecialFunction import binomial; 

#定义对象: 有理数域被根号5扩充形成的域 Q(sqrt(5)) 中的元素
#域的每个元素都可以表示为 q1 + q2 * sqrt(5)的形式, 其中q1, q2均为有理数. 
class ExtendedFieldSqrt5(): 

    #实例方法: 初始化域中的元素
    def __init__(self, q1: int or Fraction, q2: int or Fraction=0): 
        if type(q1) is ExtendedFieldSqrt5 and q2 == 0: 
            self.coefficient = q1.coefficient; 
        else: 
            self.coefficient = (Fraction(q1), Fraction(q2), ); 

    #实例方法: 指定输出形式
    def __repr__(self): 
        return("%s + %s * sqrt(5)" % self.coefficient)

    #实例方法: 转化为浮点数
    def __float__(self): 
        q1, q2 = self.coefficient; 
        return(q1 + q2 * math.sqrt(5)); 

    #实例方法: 二元四则远算执行前的有理系数提取
    def __coeff_extract(self, efs): 
        q11, q12 = self.coefficient; 
        if type(efs) is ExtendedFieldSqrt5: 
            q21, q22 = efs.coefficient; 
        elif isinstance(efs, numbers.Number): 
            q21, q22 = efs, 0; 
        return((q11, q12, q21, q22)); 

    #实例方法: 加法, 减法(重载二元"+", "-"运算符)
    def __add__(self, 
        efs: int or ExtendedFieldSqrt5): 
        q11, q12, q21, q22 = self.__coeff_extract(efs); 
        result = ExtendedFieldSqrt5(
            q11 + q21, q12 + q22
        ); 
        return(result); 

    def __radd__(self, efs):
        return(self + efs); 

    def __sub__(self, 
        efs: int or ExtendedFieldSqrt5): 
        q11, q12, q21, q22 = self.__coeff_extract(efs); 
        result = ExtendedFieldSqrt5(
            q11 - q21, q12 - q22
        ); 
        return(result); 

    def __rsub__(self, efs): 
        return(ExtendedFieldSqrt5(efs) - self); 

    #实例方法: 乘法, 除法(重载"*", "/"运算符)
    def __mul__(self, 
        efs: int or ExtendedFieldSqrt5): 
        q11, q12, q21, q22 = self.__coeff_extract(efs); 
        result = ExtendedFieldSqrt5(
            q11 * q21 + 5 * q12 * q22, q11 * q22 + q12 * q21
        ); 
        return(result); 

    def __rmul__(slf, efs):
        return(self * efs); 

    def __truediv__(self, 
        efs: int or ExtendedFieldSqrt5): 
        q11, q12, q21, q22 = self.__coeff_extract(efs); 
        numera_1 = q11 * q21 - 5 * q12 * q22; 
        numera_2 = q12 * q21 - q11 * q22; 
        denomina = q21 ** 2 - 5 * q22 ** 2
        result = ExtendedFieldSqrt5(
            Fraction(numera_1, denomina), 
            Fraction(numera_2, denomina), 
        ); 
        return(result); 

    def __rtruediv__(self, efs): 
        return(ExtendedFieldSqrt5(efs) / self); 

    #实例方法: 整数次幂(重载"**"运算符)
    def __pow__(self, exp: int): 
        q1, q2, n1, n2 = self.__coeff_extract(exp); 
        if n1 == 0: 
            return(ProjectEuler00002.ExtendedFieldSqrt5(1)); 
        elif n1 == 1: 
            return(self); 
        elif n1 >= 2: 
            #需要使用二项式定理, 因此前文中定义了二项式系数的函数
            result = ExtendedFieldSqrt5(
                sum(binomial(n1, i) \
                    * q1 ** (n1 - i) * q2 ** i * 5 ** (i // 2)
                    for i in range(0, n1 + 1, 2)
                ), 
                sum(binomial(n1, i) \
                    * q1 ** (n1 - i) * q2 ** i * 5 ** (i // 2)
                    for i in range(1, n1 + 1, 2)
                )
            ); 
            return(result); 
        else: #负数指数幂
            return(1 / self ** -n1); 

class FibonacciSequence(): 
    
    SQRT_5 = ExtendedFieldSqrt5(0, 1); 
    PHI = (1 + SQRT_5) / 2; 
    PHI_MINOR = (1 - SQRT_5) / 2; 

    #静态方法: 使用通项公式, 计算Fibonacci数列的第n项, 过程保留根号
    @staticmethod
    def general_term(n: int) -> int: 
        fib_1 = FibonacciSequence.PHI ** n; 
        fib_2 = FibonacciSequence.PHI_MINOR ** n; 
        fib = (fib_1 - fib_2).coefficient[1].numerator; 
        return(fib);  

    #实例初始化(存储递推数列的前若干项)
    def __init__(self): 
        self._fib_ls = [0, 1]; 
        
    #实例方法: 使用递推公式, 计算Fibonacci数列的第n项, 并存储中间项
    def recursive_term(self, n: int) -> int: 
        if n <= len(self._fib_ls) - 1: 
            return(self._fib_ls[n]); 
        else: 
            for i in range(len(self._fib_ls), n + 1): 
                self._fib_ls.insert(
                    i, self._fib_ls[i - 1] + self._fib_ls[i - 2]
                ); 
            return(self._fib_ls[n]); 