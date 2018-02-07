__author__ = 'Administrator'
# -*- coding: utf-8 -*-

# dict1 = {
#     "batch_run":
#     "batch_scp":
#
#
# }


def parse(cmd):  #[batch_run  -h h1,h2   -g web_clusters,db_servers  -cmd "df -h"]
    print(cmd)    #[batch_scp -h h1,h2,h3   -g web_clusters,db_servers  -action put  -local test.py  -remote /tmp/]
    ip_l = []
    g_l = []
    c_l = []
    a_l = []
    l_l = []
    r_l = []
    cmd_l = cmd.split()
    for i in cmd_l:
        if i == '-h':
            index = cmd_l.index("-h")
            ip_l.append(cmd_l[(index+1)])
        elif i == '-g':
            index = cmd_l.index("-g")
            g_l.append(cmd_l[(index + 1)])
        elif i == '-cmd':
            print(cmd)
            a = cmd.split("-cmd")
            print("aaaaaaaaaaaaaaa",a)

            c_l.append(a[1].strip())
            print("cccccccccc",c_l)
        elif i == '-action':
            index = cmd_l.index("-action")
            a_l.append(cmd_l[(index + 1)])
        elif i == '-local':
            index = cmd_l.index("-local")
            l_l.append(cmd_l[(index + 1)])
        elif i == '-remote':
            index = cmd_l.index("-remote")
            r_l.append(cmd_l[(index + 1)])

    if cmd_l[0] == 'batch_run':
        return [ip_l,g_l,c_l]
    else:
        return [ip_l,g_l,c_l,a_l,l_l,r_l]

#batch_scp -h h1   -g web_clusters,db_servers  -action put  -local F:\pycharm\python\day9\test.py  -remote /test.py
# batch_scp -h h1   -g web_clusters,db_servers  -action get  -remote /test.py  -local F:\pycharm\python\day9\etc
#batch_scp -h h1   -g web_clusters,db_servers  -action get  -remote /test.py  -local F:\\pycharm\\python\\day9\\get\\test.py
#F:\pycharm\python\day9\etc\setting.py