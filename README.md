# balderich-py

[![Issues](https://img.shields.io/github/issues/NSSCTF/balderich-py)](https://github.com/cryptography-wiki/cryptography-wiki.github.io/issues)
[![Forks](https://img.shields.io/github/forks/NSSCTF/balderich-py)](https://github.com/cryptography-wiki/cryptography-wiki.github.io/network/members)
[![Stars](https://img.shields.io/github/stars/NSSCTF/balderich-py)](https://github.com/cryptography-wiki/cryptography-wiki.github.io/stargazers)
![Size](https://img.shields.io/github/repo-size/NSSCTF/balderich-py)

* [NSSCTF](https://www.nssctf.cn/)平台API Python包，你可以使用此库来和Balderich后端进行快速交互。编写属于你的自动化bot。

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
    client = balderich.NSSClient(balderich.AuthConfig.load_config_file('config.json'))

    # 传入配置文件IO流
    with open('config.json', 'rb') as config_file:
        client = balderich.NSSClient(balderich.AuthConfig.load_config_file(config_file))
    ```

    然后你便可以开始使用客户端下各模块API来进行交互，例如查询用户信息

    ```python
    data = client.user.get_user_info(1)
    print(data)
    ```

    获取当前 API Key 所属账号的 UID（整数）

    ```python
    uid = client.user.get_self_uid()
    ```

    查询本人解题状态和未开始的公开赛事

    ```python
    states = client.problem.get_problem_states([12, 34])
    pending_contests = client.contest.get_pending_contests()
    ```

    解题状态支持每次查询 1 至 50 个题目 ID。未开始赛事的时间戳单位为秒。

    查询图床用量、图片列表和战队比赛榜单

    ```python
    usage = client.user.get_user_picturebed_used()
    pictures = client.user.get_user_picturebed_list(page=1, size=10)
    rankings = client.team.get_team_contest_rank_list_by_page(cid=42, page=1, size=15)
    ```
