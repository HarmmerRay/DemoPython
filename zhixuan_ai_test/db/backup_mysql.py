import os
import subprocess
from datetime import datetime

# MySQL配置信息
MYSQL_USER = "root"
MYSQL_PASSWORD = "Renyajun123456"
MYSQL_HOST = "172.21.0.10"  # 如果是远程数据库，请更改此值
MYSQL_DATABASE = "video"
MYSQL_PORT = 59547
# 备份文件路径和名称
BACKUP_DIR = os.path.expanduser("/home/ubuntu/mysql_backup")
TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H%M%S")
BACKUP_FILE = os.path.join(BACKUP_DIR, f"mysql_backup_{TIMESTAMP}.sql")
COMPRESSED_BACKUP_FILE = os.path.join(BACKUP_DIR, f"mysql_backup_{TIMESTAMP}.tar.gz")

# 确保备份目录存在
os.makedirs(BACKUP_DIR, exist_ok=True)


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
    backup_mysql()

# 0 * * * * /home/ubuntu/miniconda3/envs/py39/bin/python /home/ubuntu/backup_mysql.py >> /home/ubuntu/mysql_backup/1error.log 2>&1