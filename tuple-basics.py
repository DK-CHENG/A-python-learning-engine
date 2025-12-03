# tuple_basics.py - 元组基础
# 逆向应用：不可变证据

# 1. 创建元组 - 系统配置
config = ("Windows 10", "192.168.1.100", 8080)
print("系统配置:", config)

# 2. 访问元素
print("系统类型:", config[0])
print("IP地址:", config[1])

# 3. 尝试修改（会失败）
try:
    config[1] = "10.0.0.1"  # 这行会报错
except:
    print("❌ 元组不能被修改")

# 4. 元组解包
os_type, ip, port = config
print(f"解包: {os_type} | {ip}:{port}")

# 5. 与列表对比
list_data = ["动态", "可修改"]
tuple_data = ("静态", "不可修改")
print(f"列表可变: {list_data}")
print(f"元组不可变: {tuple_data}")