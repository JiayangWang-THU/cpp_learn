def div_big_by_one_digit_with_decimal(num_str: str, digit_char: str, decimal_places=2):
    """
    高精度除法：num_str(很大) ÷ digit_char(单个字符 '1'~'9')
    返回：带小数的字符串结果（截断，不四舍五入）

    整体思路：
    1. 用秦九韶 / 竖式除法算【整数部分】
    2. 得到最终余数 rem
    3. 对 rem 继续做 decimal_places 次“补 0 再除”，得到小数部分
    """

    # ---------- 0. 校验除数 ----------
    if len(digit_char) != 1 or not ('0' <= digit_char <= '9'):
        raise ValueError("divisor must be a single digit character '0'..'9'")

    B = ord(digit_char) - ord('0')
    if B == 0:
        raise ZeroDivisionError("division by zero")

    # ---------- 1. 整数部分 ----------
    rem = 0
    out = []
    start = False  # 控制前导 0

    for c in num_str:
        # 当前字符 -> 数字
        d = ord(c) - ord('0')

        # Horner / 秦九韶：构造当前被除数
        x = rem * 10 + d

        # 当前商位
        q = x // B
        # 更新余数（始终 < B）
        rem = x % B

        # 处理前导 0
        if q != 0 or start:
            out.append(chr(q + ord('0')))
            start = True

    # 如果整数部分全是 0
    integer_part = "".join(out) if out else "0"

    # ---------- 2. 小数部分 ----------
    decimal_part = []

    for _ in range(decimal_places):
        # 竖式除法：余数补 0
        rem *= 10

        # 当前小数位
        digit = rem // B
        rem = rem % B

        decimal_part.append(chr(digit + ord('0')))

    # ---------- 3. 拼接结果 ----------
    return integer_part + "." + "".join(decimal_part)


# ====== ACM 输入输出示例 ======
if __name__ == "__main__":
    # A = input().strip()       # 例如: 123456789123456789
    # b = input().strip()       # 例如: 7   (注意是单字符)
    A="1234567891234567890123456789"
    b="7"
    result = div_big_by_one_digit_with_decimal(A, b)
    print(result)                  # 题目只要商就打印这个
    print(float(A) // float(b)) 
    # 如果题目还要余数，取消下一行注释
    # print(r)
