# list_basics.py - 列表基础
# 逆向应用：动态数据收集

# 1. 创建列表 - 恶意软件特征
features = ["修改注册表", "创建隐藏进程"]
print("特征列表:", features)

# 2. 添加新发现
features.append("连接可疑IP")
print("添加后:", features)

# 3. 访问和修改
print("首个特征:", features[0])
features[1] = "注入系统进程"  # 可以修改
print("修改后:", features)

# 4. 删除特征
features.remove("连接可疑IP")
print("删除后:", features)

# 5. 列表长度
print("特征数量:", len(features))