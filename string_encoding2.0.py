"""
字符串编码安全分析 - 逆向工程基础
完成日期: 2024-11-26
"""

# 1. 编码基础验证
def encoding_basics():
    text = "王者荣耀"
    print("原始文本:", text)
    print("GBK编码:", text.encode('gbk'))
    print("UTF-8编码:", text.encode('utf-8'))
    print("ASCII尝试:", text.encode('ascii', errors='ignore'))

# 2. 外挂分析场景
def cheat_analysis():
    cheat_terms = ["自动瞄准", "透视", "无敌模式", "加速"]
    print("\n外挂术语编码分析:")
    for term in cheat_terms:
        gbk_bytes = term.encode('gbk')
        print(f"{term} -> GBK: {gbk_bytes} -> 长度: {len(gbk_bytes)}")

# 3. 编码异常检测（反外挂技术）
def encoding_anomaly_detection():
    print("\n编码异常检测模拟:")
    
    # 正常情况
    normal_text = "游戏开始"
    normal_encoded = normal_text.encode('gbk')
    
    # 可疑情况：混合编码
    mixed_data = b'\xcd\xf5' + '者'.encode('utf-8')  # 故意混合GBK和UTF-8
    
    try:
        decoded = mixed_data.decode('gbk')
    except UnicodeDecodeError as e:
        print(f"🔍 检测到编码异常: {e}")
        print("这正是反外挂系统要捕获的模式！")

# 4. 字符串格式化实战
def string_formatting_demo():
    print("\n字符串格式化实战:")
    
    # 游戏日志模板
    logs = [
        ("玩家%s使用了%s", ("小明", "透视外挂")),
        ("IP:%s 行为:%s 风险等级:%d", ("192.168.1.1", "异常移动", 3)),
        ("检测到%s在%s地图的%s行为", ("玩家A", "王者峡谷", "作弊"))
    ]
    
    for template, data in logs:
        result = template % data
        print(f"日志: {result}")

if __name__ == "__main__":
    encoding_basics()
    cheat_analysis() 
    encoding_anomaly_detection()
    string_formatting_demo()