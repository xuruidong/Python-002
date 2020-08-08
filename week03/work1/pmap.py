# -*- coding:utf-8 -*-
import sys
import getopt
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import socket
import struct
import time
import subprocess
import json


def handler_tcp(ip_num):
    print (ip_num)
    ip_str = socket.inet_ntoa(struct.pack("!I", ip_num))
    result = []
    
    for port in range(1, 1024):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((ip_str, port))
            
            client.close()
            result.append(port)
        except:
            client.close()
            
    return (ip_str, result)


def handler_ping(ip_num):
    ip_str = socket.inet_ntoa(struct.pack("!I", ip_num))
    result = subprocess.run(f"ping {ip_str} -n 1", timeout=10,
                       capture_output=True, text=True)
    
    output = result.stdout
    if("无法访问目标主机" in output or "100% 丢失" in output):
        return (ip_str, "error")
    
    return (ip_str, "ok")


def arg_parse(argv):
    arg_n = 1
    arg_f = "ping"
    arg_w = ""
    arg_m = "thread"
    arg_ip = "YOU MUST SET IP OR IP RANGE!!!"
    arg_v = False

    opts, args = getopt.getopt(argv[1:], "n:f:w:m:hv", [
                               "help", "ip="])
    for opt_name, opt_value in opts:
        if(opt_name in ('--ip')):
            arg_ip = opt_value
        elif(opt_name in ('-n')):
            try:
                arg_n = int(opt_value)
            except Exception as e:
                print ("invalid number: %s" % e)
                sys.exit(1)
        elif(opt_name in ('-f')):
            arg_f = opt_value
        elif(opt_name in ('-m')):
            arg_m = opt_value
        elif(opt_name in ('-v')):
            arg_v = True
        elif(opt_name in ('-w')):
            arg_w = opt_value
        elif(opt_name in ('-h', '--help')):
            print ("usage: help")

    if (arg_n < 0 or arg_n > 100):
        print ("invalide worker number")
        sys.exit(1)

    if (arg_m not in ("proc", "thread")):
        print ("invalid mode argument: %s" % arg_m)
        sys.exit(1)

    if (arg_f not in ("ping", "tcp")):
        print ("invalid test argument: %s" % arg_f)
        sys.exit(1)

    try:
        ip_list = arg_ip.split("-")
        if(len(ip_list) == 1):
            ip_num = int.from_bytes(socket.inet_aton(ip_list[0]), 'big')
            arg_ip_range = (ip_num, ip_num + 1)
        elif(len(ip_list) == 2):
            ip_num1 = int.from_bytes(socket.inet_aton(
                ip_list[0]), 'big')
            ip_num2 = int.from_bytes(socket.inet_aton(
                ip_list[1]), 'big')
            ip_num2 += 1
            arg_ip_range = (ip_num1, ip_num2)
        else:
            print ("invalid ip parameter")
            sys.exit(1)
    except Exception as e:
        print ("invalid ip parameter: %s, %s" % (arg_ip, e))
        sys.exit(1)

    return (arg_n, arg_f, arg_w, arg_m, arg_ip_range, arg_v)


def pmap_main(argv):
    t_start = time.time()
    arg_n, arg_f, arg_w, arg_m, arg_ip, arg_v = arg_parse(argv)

    if (arg_m == "proc"):
        pool = ProcessPoolExecutor(max_workers=arg_n)
    elif(arg_m == "thread"):
        pool = ThreadPoolExecutor(max_workers=arg_n)

    func_arg = [i for i in range(arg_ip[0], arg_ip[1])]

    if (arg_f == "tcp"):
        result_itor = pool.map(handler_tcp, func_arg)
    else:
        result_itor = pool.map(handler_ping, func_arg)

    pool.shutdown()
    json_result = {}
    for i in result_itor:
        json_result[i[0]] = i[1]
        print ("%s : %s" % (i[0], i[1]))

    if (arg_w):
        try:
            with open(arg_w, 'w') as save:
                json.dump(json_result, save)
        except Exception as e:
            print("save result to %s error: %s" % (arg_w, e))
    else:
        print (arg_w)
            
    if(arg_v):
        print ("time use: %f" % (time.time() - t_start))


if __name__ == "__main__":
    pmap_main(sys.argv)
