题目:简单主机批量管理工具

需求:

    主机分组
    主机信息配置文件用configparser解析
    可批量执行命令、发送文件，结果实时返回，执行格式如下 
        batch_run  -h h1  -g web_clusters,db_servers    -cmd  "df -h"　
        batch_scp   -h h1   -g web_clusters,db_servers  -action put  -local test.py  -remote /tmp/　
    主机用户名密码、端口可以不同
    执行远程命令使用paramiko模块
    批量命令需使用threading并发

	
	

实现：
命令参考： 
	执行命令   batch_run  -h h1  -g web_clusters,db_servers    -cmd  "df -h"
	上传	   batch_scp   -h h1   -g web_clusters,db_servers  -action put  -local  文件的绝对路径绝对路径   -remote /test.py
	下载	   batch_scp -h h1   -g web_clusters,db_servers  -action get  -remote /test.py  -local  文件的绝对路径绝对路径
端口，用户名密码在配置文件中写入，按格式。
只写了一台主机，需要请按格式添加