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
