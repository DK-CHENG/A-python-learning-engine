# list_vs_tuple_simple.py - 简单对比
# 学习总结：什么时候用什么

print("=== list 和 tuple 选择指南 ===")

# 场景对比
print("\n1. 动态收集数据 → 用 list")
suspicious_ips = []  # 空列表
suspicious_ips.append("185.215.113.66")  # 可以添加
print("可疑IP列表:", suspicious_ips)

print("\n2. 固定证据 → 用 tuple")
evidence = ("2024-11-27", "192.168.1.100", "恶意行为")
print("证据记录:", evidence)
print("证据日期:", evidence[0])

print("\n总结:")
print("- list: 数据会变化时用（如分析过程中的发现）")
print("- tuple: 数据固定时用（如取证时间戳）")