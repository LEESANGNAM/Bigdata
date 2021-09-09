
# coding: utf-8

# In[1]:


def test(a,b):
    c = a+b
    return c
a,b = map(int,input().split())
# 두개의 정수입력받고 더하기 함수
print(test(a,b))


# In[12]:


import math
a= 10
b= math.sqrt(a)
print(b)


# In[14]:


print("{:.5f}".format(math.pi))


# In[16]:


dir(math)
# 목록확인


# In[35]:


import random

a = random.random()
print(a)


# In[36]:


a = random.randint(1,100)
print(a)


# In[46]:


a = random.randrange(10,100,2)
print(a)


# In[56]:


t1=[1,2,3,4,5]
print(t1)
print("###########################")
random.shuffle(t1)
print(t1)
print("###########################")
t1.sort()
print(t1)


# In[51]:


t1=[1,2,3,4,5]
a = random.choice(t1)
print(a)


# In[52]:


import statistics
a=10
b=statistics.math.sqrt(a)
print(b)


# In[53]:


t1=[2,3,5,7,11]
a = statistics.mean(t1)
print(a)


# In[55]:


t1=[2,3,5,7,11]
a=statistics.median(t1)
print(a)
# 홀수면 중앙값
print("###################")
t1 = [2,3,5,7]
a=statistics.median(t1)
print(a)
# 짝수면 중앙 2개의값의 평균


# In[57]:


import os #  OS 관련 모듈
a = os.getcwd() # 현재 작업중인 디렉토리 위치 
print(a)


# In[61]:


import copy
t=[1,2,3]
a=copy.copy(t)
print(a==t) # 값이 같은지 본다
print(a is t) # 메모리 주소가 같은지 본다 (같은 객체인가)
print("#############DEEPCOPPY#########")

t=[1,2,3]
a=copy.deepcopy(t)
print(a is t)


# In[82]:


a=[1,2,3]
b=a
print("####### 변경전 ########")
print(a)
print(b)
b[0]=999 # 복사가 아닌 참조를 확인하기 위한 값 변경
print("####### 변경후 ########")
print(a)
print(b)

c= [1,2,3]
d=copy.copy(c)
# 리스트와 사전 이용
#  d = list(c)
#  d = c[:]
print("#########  복사 #######")
print('c =',c)
print('d =',d)
d[0]=999 # 복사 확인을 위한 값 변경
print("####### 변경후 ########")
print('c =',c)
print('d =',d)


# In[84]:


print("################ 얕은복사 ################")
c = [1,2,3,[4,5]]
d=copy.copy(c)
print("########### 얕은복사 변경전 ###########")
print('c =',c)
print('d =',d)
d[-1].append(6)
print("########### 얕은복사 변경후 ##########")
print('c =',c)
print('d =',d)

print("############## 깊은복사 ##################")
c = [1,2,3,[4,5]]
d=copy.deepcopy(c)
print("########### 깊은복사 변경전 ###########")
print('c =',c)
print('d =',d)
d[-1].append(6)
print("########### 깊은복사 변경후 ##########")
print('c =',c)
print('d =',d)


# #### 모듈 삭제하는법
# + del 모듈의 이름
# ```python
# import math
# a = math.sqrt(10)
# print(a)
# ```
# ```python
# del math
# b=math.sqrt(25)
# print(b)
# ```

# In[87]:


import random as r # 별명 설정
a = r.randint(10,20)
print(a)


# ### 모듈에서 일부함수만 불러오기
# ```python
# from math import sqrt, pi
# a= sqrt(10)
# print(a)
# ```

# In[89]:


from math import sqrt, pi
a= sqrt(10)
print(a)


# In[94]:


import mymodule
mymodule.notice("홍길동")

a,b = map(int,input().split())
result = mymodule.myfunc(a,b)
print(result)

mymodule.myvar +=1
print(mymodule.myvar)

