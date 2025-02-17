#Project Euler解题专用数论库
#作者: Frank-Deng-WH6HS <enter_the_dragon@foxmail.com>

import math; 

import numpy as np; 

#素数构建器对象
class Primes(): 
    
    def __init__(self): 
        self._container = np.ones(0, dtype=np.int8); 
        self.primes = {2: 1, 3: 1}; 
        
    def max_known_prime(self): 
        return(max(self.primes));  
        
    #利用Eratosthenes筛选法判定num是否为质数, 
    #并使用self.primes收集小于等于num的所有质数
    #在Intel Core i7-3740QM处理器上测试显示(单一线程, 频率3.5GHz): 
    #不大于一亿的所有素数全部筛选仅需不超过半分钟
    def sieve_of_eratosthenes(self, num: int) -> bool: 
        #特殊情况
        max_pri = self.max_known_prime(); 
        if num <= max_pri: #素数表中必定包含2
            return(bool(num in self.primes)); 
        #筛选法
        cont_len = num + 1 - max_pri; 
        self._container = np.ones(cont_len, dtype=np.int8); 
        for pri in self.primes.keys(): 
            if pri > cont_len: 
                break; 
            offset = pri - (max_pri % pri); 
            self._container[offset: : pri] = 0; 
        for idx in range(2, cont_len, 2): 
            sta = self._container[idx]; 
            if bool(sta): 
                self.primes[max_pri + idx] = 1; 
                offset = max_pri + 2 * idx; 
                self._container[offset: : max_pri + idx] = 0; 
        self._container = np.ones(0, dtype=np.int8); 
        return(bool(sta)); 
        
    #静态方法: 利用素数定义判定num是否为素数
    @staticmethod
    def prime_definition(num: int) -> bool:
        #特殊情况
        if num <= 1: 
            return(False); 
        elif num <= 3: 
            return(True); 
        elif num % 2 == 0: 
            return(False); 
        #试除法
        div, quot, rem = 1, num, 0; 
        while div <= quot: 
            div += 2; 
            quot, rem = divmod(num, div); 
            if rem == 0: 
                return(False); 
        return(True); 
    
    #静态方法: 利用Wilson定理判定num是否为素数
    @staticmethod
    def wilson_theorem(num: int) -> bool: 
        return(math.factorial(num - 1) % num == (num - 1)); 
  