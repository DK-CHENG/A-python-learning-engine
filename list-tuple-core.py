# list/tuple 学习总结 

# 1. list基本操作（可变）
names = ['Alice', 'Bob', 'Charlie']  # 创建
names.append('David')     # 添加
names[1] = 'Bill'         # 修改
names.pop()               # 删除
print(names[0])           # 访问

# 2. tuple基本操作（不可变）
info = ('张三', 25, '工程师')  # 创建
print(info[0])                # 访问
# info[1] = 26  # ❌ 报错！不能修改

# 3. 核心区别
# list可变：[]定义，可增删改
# tuple不可变：()定义，创建后不能改

# 4. 使用场景
# list：需要变化的数据（如收集分析结果）
# tuple：固定不变的数据（如配置信息）