"""
字符串编码与内存分析
探究不同编码方案在安全场景下的行为差异
"""

def analyze_encoding_behavior():
    """分析不同字符串的编码特征"""
    
    test_cases = [
        "admin",
        "user_input",
        "路径遍历",
        "normal_text"
    ]
    
    for text in test_cases:
        utf8_bytes = text.encode('utf-8')
        gbk_bytes = text.encode('gbk') if not any(ord(c) > 127 for c in text) else b'unsupported'
        
        print(f"字符串: {text}")
        print(f"UTF-8: {utf8_bytes} (长度: {len(utf8_bytes)}字节)")
        if gbk_bytes != b'unsupported':
            print(f"GBK: {gbk_bytes} (长度: {len(gbk_bytes)}字节)")
        print("---")

def detect_anomalous_patterns():
    """检测潜在的异常编码模式"""
    
    patterns = {
        "空字节注入": "admin\x00",
        "URL编码": "%2e%2e%2f", 
        "Unicode混淆": "ａｄｍｉｎ"  # 全角字符
    }
    
    for desc, pattern in patterns.items():
        original_len = len(pattern)
        encoded_len = len(pattern.encode('utf-8'))
        print(f"{desc}: '{pattern}'")
        print(f"视觉长度: {original_len}, 实际字节: {encoded_len}")
        print("---")

if __name__ == "__main__":
    analyze_encoding_behavior()
    detect_anomalous_patterns()