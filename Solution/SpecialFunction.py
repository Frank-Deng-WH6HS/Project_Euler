#Project Euler解题专用特殊函数库
#作者: Frank-Deng-WH6HS <enter_the_dragon@foxmail.com>

import math; 

#二项式系数
def binomial(n: int, r: int) -> int: 
    return(math.factorial(n) // math.factorial(n- r) // math.factorial(r)); 
