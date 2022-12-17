# balderich-py

[![Issues](https://img.shields.io/github/issues/NSSCTF/balderich-py)](https://github.com/cryptography-wiki/cryptography-wiki.github.io/issues)
[![Forks](https://img.shields.io/github/forks/NSSCTF/balderich-py)](https://github.com/cryptography-wiki/cryptography-wiki.github.io/network/members)
[![Stars](https://img.shields.io/github/stars/NSSCTF/balderich-py)](https://github.com/cryptography-wiki/cryptography-wiki.github.io/stargazers)
![Size](https://img.shields.io/github/repo-size/NSSCTF/balderich-py)

* [NSSCTF](https://www.ctfer.vip/)平台API Python包，你可以使用此库来和Balderich后端进行快速交互。编写属于你的自动化bot。

## 安装

* 你可以直接使用pip来进行安装本包

    ```python
    pip install balderich
    ```

* **请注意**：你需要使用Python3.8及以上版本来安装本包。

## 使用

* 你可以通过以下方式来快速的创建一个客户端

    ```python
    import balderich

    # 直接传入字符串
    client = balderich.NSSClient(key='xxx',
                                 secret='xxxx')
    
    # 传入配置文件路径
    client = balderich.NSSClient(balderich.AuthConfig('config.json'))

    # 传入配置文件IO流
    client = balderich.NSSClient(balderich.AuthConfig(open('config.json', 'rb')))
    ```

    然后你便可以开始使用客户端下各模块API来进行交互，例如查询用户信息

    ```python
    data = client.user.get_user_info(1)
    print(data)
    ```
