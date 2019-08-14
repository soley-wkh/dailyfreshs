# -*- coding:utf-8 -*-
"""
    version:
    author : wkh
    time   : 2019/8/4 14:03
    file   : storage.py

"""
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings


class FDFSStorage(Storage):
    """fast dfs文件存储类"""

    def __init__(self, client_conf=None, base_url=None):
        if client_conf is None:
            client_conf = settings.FDFS_CLENT_CONF
        self.client_conf = client_conf

        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        """打开文件时使用"""
        pass

    def _save(self, name, content):
        """保存文件时使用"""
        # 创建一个fdfs_client对象
        clent = Fdfs_client(self.client_conf)
        ret = clent.upload_by_buffer(content.read())
        # dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }

        if ret.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fdfs失败')
        # 获取返回文件的id
        filename = ret.get('Remote file_id')
        return filename

    def exists(self, name):
        """django判断文件名是否可用"""
        return False

    def url(self, name):
        return self.base_url + name
