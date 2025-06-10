#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
密码加密
@Project ：CommonUseCase
@File ：PrpCrypt.py
@Author ：xie.xiaolan
@Date ：2022/7/6 14:06
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import pymysql

# 密钥
AES_KEY = "HDOeKZpg6IUAOjd+"

# 数据库配置
DB_CONFIG = {
    # 'host': '172.16.0.253',   #内网地址
    'host': '139.198.16.201',   #外网地址
    'user': 'poweriot',
    'password': 'power_iot456',
    'database': 'micro_grid',
    'port': 4000,
    'charset': 'utf8mb4'
}

class PrpCrypt(object):

    def __init__(self, key=AES_KEY):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.conn = None
        self.cursor = None


    def encrypt(self, text):
        """
        加密函数，如果text不足16位就用空格补足为16位，
        如果大于16当时不是16的倍数，那就补足为16的倍数。
        :param text: 加密密码
        :return: 加密后的字符串
        """
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(ciphertext)


    def decrypt(self, text):
        """
        解密后，去掉补足的空格用strip() 去掉
        :param text: 待解密字符串
        :return: 解密密码
        """
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip('\0')

    # noinspection PyShadowingNames
    def generate_and_encrypt_password(self, return_plain=False):
        """
        生成一个8~20位的随机密码（包含至少两种类型：字母、数字、符号），并加密返回。
        :param return_plain: 是否同时返回明文密码（默认否）
        :return: 加密后的密码（如 return_plain 为 True，则返回元组：明文, 密文）
        """
        import random
        import string

        length = random.randint(8, 20)
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        char_types = [letters, digits, symbols]
        selected_types = random.sample(char_types, 2)

        password = [random.choice(t) for t in selected_types]
        all_chars = ''.join(char_types)
        password += [random.choice(all_chars) for _ in range(length - len(password))]
        random.shuffle(password)

        raw_password = ''.join(password)
        encrypted = self.encrypt(raw_password)

        if return_plain:
            return raw_password, encrypted
        return encrypted

    def save_password_to_mysql(self,plain_text, encrypted_text):
        """
        将明文和加密密码保存到 MySQL 数据库
        :param plain_text: 明文
        :param encrypted_text: 加密密文
        :return:
        """
        try:
            self.conn = pymysql.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
            # 假设表名为 passwords，字段为 plain 和 encrypted
            sql = "UPDATE micro_grid.user SET password = %s,name = %s WHERE phone_number = '19925374637'"
            self.cursor.execute(sql, (encrypted_text,plain_text))
            self.conn.commit()
            print("密码已保存到数据库。")
        except Exception as e:
            print("数据库操作失败:", e)
        finally:
            self.cursor.close()
            self.conn.close()




if __name__ == '__main__':
    pc = PrpCrypt()  # 初始化
    # e = pc.encrypt("Longgang123..")  # 加密
    # print("加密:", e)
    # b = str(e, encoding='utf-8')
    # print(b)
    # e = "b56c91edc3ecdee432cd5e541e0f2a7b"
    # d = pc.decrypt(e)  # 解密
    # print("解密:", d)
    plain, encrypted = pc.generate_and_encrypt_password(return_plain=True)
    encrypted_str = str(encrypted, encoding='utf-8')
    print("明文密码:", plain)
    print("加密密码:", encrypted_str)
    pc.save_password_to_mysql(plain,encrypted_str)
