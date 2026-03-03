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
import random
import string

# 密钥
AES_KEY = "HDOeKZpg6IUAOjd+"

def get_db_config(database_name):
    return {
        'host': '139.198.16.201',
        'user': 'poweriot',
        'password': 'power_iot456',
        'database': database_name,
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
        加密函数
        """
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add).encode('utf-8')
        ciphertext = cryptor.encrypt(text)
        return b2a_hex(ciphertext)

    def decrypt(self, text):
        """
        解密函数
        """
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')

    def generate_and_encrypt_password(self, return_plain=False):
        """
        生成并加密密码
        """
        length = random.randint(8, 20)

        # 定义字符集
        letters = string.ascii_letters  # 大小写字母
        digits = string.digits  # 数字
        symbols = string.punctuation  # 特殊字符

        # 随机选择密码格式（两种方案二选一）
        format_choice = random.choice(['letter_digit', 'symbol_digit'])

        if format_choice == 'letter_digit':
            # 方案1：字母 + 数字
            # 确保至少有一个字母和一个数字
            password = [
                random.choice(letters),  # 至少一个字母
                random.choice(digits)  # 至少一个数字
            ]
            # 剩余字符从字母和数字中随机选择
            remaining_pool = letters + digits
        else:
            # 方案2：特殊字符 + 数字
            # 确保至少有一个特殊字符和一个数字
            password = [
                random.choice(symbols),  # 至少一个特殊字符
                random.choice(digits)  # 至少一个数字
            ]
            # 剩余字符从特殊字符和数字中随机选择
            remaining_pool = symbols + digits

        # 补充剩余长度的字符
        for _ in range(length - len(password)):
            password.append(random.choice(remaining_pool))

        # 打乱顺序，避免固定格式
        random.shuffle(password)

        # 组合成最终密码
        raw_password = ''.join(password)
        encrypted_s = self.encrypt(raw_password)

        if return_plain:
            return raw_password, encrypted_s
        return encrypted_s

    def save_password_to_mysql(self, plain_text, encrypted_text):
        """
        保存密码到 micro_grid 数据库
        """
        try:
            self.conn = pymysql.connect(**get_db_config('micro_grid'))
            self.cursor = self.conn.cursor()
            sql = "UPDATE micro_grid.user SET password = %s, name = %s WHERE phone_number = '19925374637'"
            self.cursor.execute(sql, (encrypted_text, plain_text))
            self.conn.commit()
            print("密码已保存到 micro_grid 数据库。")
        except Exception as e:
            print("micro_grid 数据库操作失败:", e)
        finally:
            self.cursor.close()
            self.conn.close()

    def save_password_to_vpp_db(self, encrypted_text):
        """
        保存密码到 vpp 数据库
        """
        try:
            self.conn = pymysql.connect(**get_db_config('vpp'))
            self.cursor = self.conn.cursor()
            sql = "UPDATE vpp.user SET password = %s WHERE phone_number = '19925374637'"
            self.cursor.execute(sql, encrypted_text)
            self.conn.commit()
            print("密码已保存到 vpp 数据库。")
        except Exception as e:
            print("vpp 数据库操作失败:", e)
        finally:
            self.cursor.close()
            self.conn.close()

    def save_password_to_vpp_agg_db(self, encrypted_text):
        """
        保存密码到 vpp_agg 数据库
        """
        try:
            self.conn = pymysql.connect(**get_db_config('vpp_agg'))
            self.cursor = self.conn.cursor()
            sql = "UPDATE vpp_agg.user SET password = %s WHERE phone_number = '19925374637'"
            self.cursor.execute(sql, encrypted_text)
            self.conn.commit()
            print("密码已保存到 vpp_agg 数据库。")
        except Exception as e:
            print("vpp_agg 数据库操作失败:", e)
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
    pc.save_password_to_mysql(plain, encrypted_str)
    pc.save_password_to_vpp_db(encrypted_str)
    pc.save_password_to_vpp_agg_db(encrypted_str)
