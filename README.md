# ExpressCheck
### English
If there is a COVID-19 outbreak in your area, you may not be able to receive some express. You can use this tool to check the express status of your area.\
Usage:\
Firstly you should **cd** to your file address which has the ExpressCheck.py\
**python ExpressCheck.py [-h|--help]** to get help\
**python ExpressCheck.py [-p|--province] PROVINCE [-c|--city] CITY [-ar|--area] AREA [-ad|--address] ADDRESS** to check the status of your area

### 中文
如果您所在的地区出现新冠疫情，你可能会收不到一些快递公司的快递。您可以使用此工具来确认您所在地区的快递状态。\
用法：\
首先使用 cd 命令进入 ExpressCheck.py 文件所在的目录下\
**python -h** 命令可以获得使用帮助\
**python ExpressCheck.py [-p|--province] 省份 [-c|--city] 城市 [-ar|--area] 区 [-ad|--address] 详细地址** 启动脚本查询快递状态（直辖市省份与城市相同）

### 示例：
python ExpressCheck.py -p 重庆市 -c 重庆市 -ar 南岸区 -ad 重庆邮电大学
