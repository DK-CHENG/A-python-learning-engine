，"""
if_else_core.py - 条件判断核心要点
Python条件判断必记内容
"""

# ==================== 核心语法格式 ====================
# 1. 基础if-else
age = 20
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# 2. 多条件 elif
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:    # 80 <= score < 90
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# ==================== 逻辑运算符 ====================
# and: 两个条件都成立
# or:  至少一个成立
# not: 条件取反

x = 10
if x > 5 and x < 15:    # 5 < x < 15
    print("x在5到15之间")

if x < 0 or x > 100:
    print("x超出正常范围")

if not x == 5:          # 等同于 x != 5
    print("x不等于5")

# ==================== 嵌套条件 ====================
is_login = True
is_admin = False

if is_login:
    if is_admin:
        print("管理员登录")
    else:
        print("普通用户登录")
else:
    print("请先登录")

# ==================== 简洁写法 ====================
# 一行if (不推荐复杂逻辑)
if x > 0: print("正数")

# 三元表达式
result = "偶数" if x % 2 == 0 else "奇数"

# ==================== 注意要点 ====================
# 1. 冒号不能少
# 2. 缩进必须一致（4个空格或1个tab）
# 3. elif 是 else if 的缩写
# 4. else 可以省略

# ==================== 常见错误 ====================
# 错误1: 用了 = 而不是 ==
# if x = 5:  # 语法错误
# if x == 5: # 正确

# 错误2: 忘记冒号
# if x > 5   # 语法错误
# if x > 5:  # 正确

# 错误3: 缩进不一致
# if x > 5:
#     print("A")
#   print("B")  # 缩进错误

# ==================== 实际示例 ====================
# BMI计算
height = 1.75
weight = 80.5
bmi = weight / (height ** 2)

if bmi < 18.5:
    level = "偏瘦"
elif bmi < 25:
    level = "正常"
elif bmi < 32:
    level = "肥胖"
else:
    level = "严重肥胖"

print(f"BMI: {bmi:.1f} - {level}")