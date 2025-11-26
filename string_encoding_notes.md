# 字符串和编码

## 1. 编码发展
- ASCII编码升级Unicode（语言种类更多）
- 升级UTF-8（更简便）

## 2. 编码使用场景  
- 在计算机内存中统一使用Unicode编码
- 当需要保存到硬盘或者需要传输的时候，就会转换成UTF-8编码

## 3. 核心函数
- `ord()`函数把字符转换成整数表示（这个字的身份证）
- `chr()`函数把编码转换成对应的字符（通过身份证找到这个字）  
- `encode()`函数是一段话的身份证

## 4. 编码关系比喻
- 完整文字是整列火车（str）
- 计算机的存储是一节节车厢（bytes）
- 文字到计算机是把火车拆成车厢（encode()）
- 计算机到文字是把车厢组装成火车（decode()）

## 5. bytes显示规则
- 在bytes中，无法显示为ASCII字符的字节，用`\x##`表示

## 6. 编解码实战
'ABC'.encode('utf-8') → b'ABC'
b'ABC'.decode('utf-8') → 'ABC'

- bytes无法解码时报错
- 忽略错误：decode('utf-8', errors='ignore')

## 7. 长度计算
len('ABC') = 3 (字符数)
len('中文'.encode('utf-8')) = 6 (字节数)

## 8. Python源代码编码
开头添加：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 9. 字符串格式化
占位符：%s=字符串 %d=整数 %f=小数

'hello, %s' % 'world'
'Hi, %s, you have $%d.' % ('Michael', 1000000)

步骤：
1. 准备模板：template = 'Hi, %s, you have $%d.'
2. 准备答案：answers = ('Michael', 1000000)  
3. 执行填空：result = template % answers
4. 得到结果：'Hi, Michael, you have $1000000.'