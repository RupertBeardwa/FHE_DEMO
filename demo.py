from Pyfhel import Pyfhel, PyCtxt

# 初始化 Pyfhel 对象
HE = Pyfhel()
HE.contextGen(p=65537, m=2048)     # p 是明文模数（越大可表示的整数越大），m 是多项式模数
HE.keyGen()                        # 生成公钥、私钥
HE.relinKeyGen()                   # 生成重线性化密钥，用于乘法操作

# 明文数据
a, b = 15, 27
print(f"Original values: a={a}, b={b}")

# 加密
enc_a = HE.encryptInt(a)
enc_b = HE.encryptInt(b)

# 同态加法
enc_sum = enc_a + enc_b

# 同态乘法
enc_mul = enc_a * enc_b

# 解密
decrypted_sum = HE.decryptInt(enc_sum)
decrypted_mul = HE.decryptInt(enc_mul)

# 输出结果
print(f"Decrypted sum: {decrypted_sum}")
print(f"Decrypted product: {decrypted_mul}")
