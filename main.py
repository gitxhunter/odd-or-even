# 第一个repo 有点紧张

print("=== 奇数还是偶数 ===")

while True:
    user_input = input("输入数字 (q退出): ")
    
    if user_input.lower() == 'q':
        print("谢谢使用")
        break
    
    try:
        num = int(user_input)
    except:
        print("请输入数字好吗")
        continue
    
    if num % 2 == 0:
        print(f"{num} 是偶数 ✨")
    else:
        print(f"{num} 是奇数 🌟")
    
    if num == 0:
        print("0是特殊的偶数。数学真有趣。")
