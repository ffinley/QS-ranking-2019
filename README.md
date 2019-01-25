# QS-ranking-2019
用requests库通过ajax接口抓取了QS官网上2019年的世界大学排名，最终以excel文档形式导出

1. 登录https://www.topuniversities.com/，即QS大学排名官网，到达2019年世界大学排名子页面
2. 通过开发者工具network发现其xhr文件中第四个为我们需要的json文件，但因为其命名是动态变化的，获取该文件的url
3. 通过该url实现抓取。因为其为json文件，可以用在线解析工具查看键值。
4. 用requests实现抓取，将json文件转为dict数据类型，再进行切割转化为数组，新建excel并填入其中。

QS官网排名数据为js动态生成，无法使用静态网页数据抓取的方式，只能通过其ajax接口。

如有问题，欢迎联系


