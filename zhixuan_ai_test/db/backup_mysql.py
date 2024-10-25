import ipaddress
import os
import socket
import subprocess
from datetime import datetime

import psutil

# MySQL配置信息
MYSQL_USER = "root"
MYSQL_PASSWORD = "Renyajun123456"
MYSQL_HOST = "bj-cdb-boh4uk3y.sql.tencentcdb.com"  # 如果是远程数据库，请更改此值
MYSQL_DATABASE = "video"
MYSQL_PORT = 59547
# 备份文件路径和名称
BACKUP_DIR = os.path.expanduser("/home/ubuntu/mysql_backup")
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H%M%S")
BACKUP_FILE = os.path.join(BACKUP_DIR, f"mysql_backup_{TIMESTAMP}.sql")
COMPRESSED_BACKUP_FILE = os.path.join(BACKUP_DIR, f"mysql_backup_{TIMESTAMP}.tar.gz")

# 确保备份目录存在
os.makedirs(BACKUP_DIR, exist_ok=True)


def get_local_ip_method1():
    try:
        # 获取所有网络接口的信息
        addrs = psutil.net_if_addrs()
        for interface, addresses in addrs.items():
            for addr in addresses:
                # 检查是否为IPv4地址
                if addr.family == socket.AF_INET:
                    ip = ipaddress.ip_address(addr.address)
                    # 检查是否在指定的子网范围内
                    if ip.is_private and str(ip).startswith('172.21.'):
                        return str(ip)
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""


def backup_mysql():
    try:
        # 导出MySQL表
        command = f"mysqldump -u{MYSQL_USER} -p'{MYSQL_PASSWORD}' -h{MYSQL_HOST} -P{MYSQL_PORT} {MYSQL_DATABASE} users list account payments > {BACKUP_FILE}"
        subprocess.run(command, shell=True, check=True)
        print("MySQL dump completed.")

        # 压缩备份文件
        command = f"tar czf {COMPRESSED_BACKUP_FILE} {BACKUP_FILE}"
        subprocess.run(command, shell=True, check=True)
        print("Backup file compressed.")

        # 删除原始SQL文件以节省空间
        os.remove(BACKUP_FILE)
        print("Original SQL file removed.")

    except subprocess.CalledProcessError as e:
        print(f"Error during backup process: {e}")


if __name__ == "__main__":
    if "172.21.16.2" == get_local_ip_method1():
        print("Local IP is 172.21.16.2")
        backup_mysql()

# 0 * * * * /home/ubuntu/miniconda3/envs/py39/bin/python /home/ubuntu/backup_mysql.py >> /home/ubuntu/mysql_backup/1error.log 2>&1