import requests, redis, json
import datetime

db_conn = redis.ConnectionPool(host="127.0.0.1", port=6379, db=0)
redis_conn_0 = redis.Redis(connection_pool=db_conn, max_connections=10)


# 获取ipa接口
def add_ip_api():
    url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=0&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    res = requests.get(url).text
    data = json.loads(res)
    data_1 = data['data']
    for ip_1 in data_1:
        ip = ip_1['ip']
        port = ip_1['port']
        a = str(ip) + ':' + str(port)
        redis_conn_0.lpush('IP', a)
        print("已添加 %s %s ...ok" % (ip, port))


def get_num_ip():
    while True:
        num = redis_conn_0.llen("IP")
        if num < 11:
            add_ip_api()
        else:
            print(num)
            ip = get_random_ip()
            return ip
        continue


# 删除redis数据库里的ip
def remove_ip(ip):
    redis_conn_0.zrem("IP", ip)
    print("已删除 %s..." % ip)


# # 获取redis数据库里一共有多少ip
# def get_ip_num():
#     while True:
#         num = redis_conn_0.zcard("IP")
#         if num < 11:
#             add_ip_api()
#         else:
#             # print(num)
#             break
#     return num


# def get_port():
#     port = redis_conn.zscore("IP", ip)
#     port = str(port).replace(".0", "")
#     return port


def get_random_ip():
    aa = redis_conn_0.rpop("IP")
    random_ip = str(aa).replace("b", '').replace("'", "")
    # ip = redis_conn_0.lpush("IP", random_ip)
    print('从右弹出一个ip', random_ip)
    return random_ip
    # end_num = get_ip_num()
    # pop_ip = redis_conn_0.rpop(-1)
    # num = random.randint(0, end_num)
    # random_ip = redis_conn_0.zrange("IP", num, num)
    # if not pop_ip:
    #     return "", ""
    # random_ip = str(pop_ip[0]).replace("b", '').replace("'", "")
    # port = get_port(random_ip, redis_conn_0)
    # print(random_ip)
    # print(port)
    # return random_ip, port


def aps_detection_ip():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    while True:
        res = get_num_ip()
        print(res)
        ip = res.split(':')[0]
        port = res.split(':')[1]
        proxies = {
            'https': 'https://' + str(ip) + ':' + str(port),
            'http': 'http://' + str(ip) + ':' + str(port)
        }
        try:
            r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
            r.encoding = 'utf-8'
            print('可用', r.text)
            ip = res.split(':')[0] + ':' + res.split(':')[1]
            redis_conn_0.lpush('IP', ip)
            print('从左侧插入', ip)
        except Exception:
            print('删除', proxies)
            add_ip_api()


if __name__ == "__main__":
    aps_detection_ip()
