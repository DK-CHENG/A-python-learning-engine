"""
变量与对象模型：从“便利贴”比喻到Python实现
"""

def demonstrate_assignment_mechanics():
    """展示赋值操作的底层逻辑"""
    print("=== 变量赋值机制验证 ===\n")
    
    # 情景1：基础赋值
    print("1. 基础赋值:")
    a = 100
    print(f"a = 100 → id(a) = {id(a)}")
    
    # 情景2：引用传递
    print("\n2. 引用传递:")
    b = a  # 不是复制值，而是传递引用
    print(f"b = a → id(b) = {id(b)}")
    print(f"id(a) == id(b): {id(a) == id(b)}")
    
    # 情景3：重新赋值
    print("\n3. 重新赋值:")
    a = a + 1  # 创建新对象，重新绑定
    print(f"a = a + 1 → id(a) = {id(a)}")
    print(f"id(a) == id(b): {id(a) == id(b)}")
    print(f"b的值保持不变: {b}")

def demonstrate_mutable_vs_immutable():
    """对比可变与不可变对象的行为差异"""
    print("\n=== 可变 vs 不可变对象 ===\n")
    
    # 不可变对象示例
    print("1. 不可变对象 (整数):")
    x = 100
    y = x
    x = 200
    print(f"x = {x}, y = {y}")  # y不受影响
    
    # 可变对象示例  
    print("\n2. 可变对象 (列表):")
    list1 = [1, 2, 3]
    list2 = list1  # 指向同一个列表对象
    list1.append(4)  # 修改原对象
    print(f"list1 = {list1}")
    print(f"list2 = {list2}")  # list2也受到影响！
    print("→ 对可变对象的修改会影响所有引用")

if __name__ == "__main__":
    demonstrate_assignment_mechanics()
    demonstrate_mutable_vs_immutable()