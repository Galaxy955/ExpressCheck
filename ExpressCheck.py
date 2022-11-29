# Check the status of express deliveries.
import requests
import re
import argparse
from tabulate import tabulate

def DisplayResult(result: dict, province: str, city: str, area: str, address: str, command: int):
    result_table = [
        ["快递公司", "配送状态"]
    ]
    express_names = list(result.keys())
    for i in range(len(result)):
        result_table.append([express_names[i], result[express_names[i]]])
    if command == 0:
        if province == city:
            print("{}{}{}的快递状态：".format(city, area, address))
        else:
            print("{}{}{}{}的快递状态：".format(province, city, area, address))
        print(tabulate(result_table, headers="firstrow"))
    else:
        return tabulate(result_table, headers="firstrow")

def main(province=None, city=None, area=None, address=None, command=0):
    if command == 0:
        # Get the address parameters.
        parser = argparse.ArgumentParser()
        parser.description = "Please input province, city, area and address."
        parser.add_argument("-p", "--province", help="Input your province name.", type=str, default="重庆市")
        parser.add_argument("-c", "--city", help="Input your city name.", type=str, default="重庆市")
        parser.add_argument("-ar", "--area", help="Input your area name.", type=str, default="南岸区")
        parser.add_argument("-ad", "--address", help="Input your detail address.", type=str, default="重庆邮电大学")
        args = parser.parse_args()
        province = args.province
        city = args.city
        area = args.area
        address = args.address
    else:
        province = province
        city = city
        area = area
        address = address

    # Build the url.
    url = "https://p.kuaidi100.com/apicenter/order.do?method=expressStopInquiries&platform=WWW&toProvince="+province+\
          "&toCity="+city+"&toArea="+area+"&toAddress="+address

    # Get the response.
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/4G Language/zh_CN",

    }
    response = requests.get(url=url, headers=headers)
    status = response.ok
    # Check the status of the request.
    if status is False:
        raise RuntimeError("Request Error.")
    else:
        response = response.text
        express_names = re.findall(re.compile('"expressCode":"([a-z]*)?",'), response)
        express_status = re.findall(re.compile('"reachable":([0|1]),'), response)
        # Check the length of the names and the express status.
        if len(express_names) != len(express_status):
            raise RuntimeError("The length is not equal.")
        else:
            # Build the result dictionary.
            name_reflect_dict = {
                "yuantong": "圆通快递",
                "shentong": "申通快递",
                "zhongtong": "中通快递",
                "yunda": "韵达快递",
                "jtexpress": "极兔快递",
                "debangkuaidi": "德邦快递",
                "jd": "京东快递",
                "shunfeng": "顺丰快递",
                "youzhengguonei": "邮政国内"
            }
            if command == 0:
                status_reflect_dict={
                    "0": "\033[28;31m×\033[0m",
                    "1": "\033[28;32m√\033[0m"
                }
            else:
                status_reflect_dict = {
                    "0": "×",
                    "1": "√"
                }
            result_dict = {}
            for i in range(len(express_names)):
                if express_status[i] not in ("0", "1"):
                    result_dict[name_reflect_dict[express_names[i]]] = "状态未知"
                else:
                    result_dict[name_reflect_dict[express_names[i]]] = status_reflect_dict[express_status[i]]
            result = DisplayResult(result_dict, province, city, area, address, command)
            return result

if __name__ == "__main__":
    main()