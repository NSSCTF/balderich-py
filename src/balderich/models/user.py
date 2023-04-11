import io
from balderich.models.resource import Collection
from balderich.utils.code import SUCCESS
from balderich.utils.exceptions import get_exception
from typing import IO, Any, Dict, List

class UserCollection(Collection):
    def get_user_info(self, name: str) -> Dict[str, Any]:
        """
        获取用户个人信息。相同的路径数据缓存60分钟。

        Args:
            name参数可以为用户名或用户UID。
            
        Returns:
            {
                uid: integer,
                bio: string,
                intro: string,
                username: string,
                solves: integer,
                rating: integer,
                avatar: string,
                cover: string,
                register_date: integer,
                last_login_date: integer,
                email: string,
                followers: integer,
                following: integer,
                tid: integer
                team: string,
                is_vip: boolean
            }
        """
        code, data = self.client._get(f'user/{name}/info/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
        
    def get_user_statistics_active(self, uid: int) -> Dict[str, Any]:
        """
        获取用户解题活跃数据。相同的路径数据缓存60分钟。

        Args:
            uid参数为用户UID。

        Returns:
            从当年1月1日至当天的每日解题数据。

            {
                start_date: integer,
                ends_date: integer,
                count: [
                    [string, integer],
                    ...
                ]
            }
        """
        code, data = self.client._get(f'user/{uid}/statistics/active/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_user_statistics_solves(self, uid: int) -> List[Any]:
        """
        获取用户解题曲线。相同的路径数据缓存60分钟。

        Args:
            uid参数为用户UID。

        Returns:
            分类返回用户解题时间时间戳数据。

            [
                {
                    type: 0,
                    name: "WEB",
                    data: [integer, ...]
                }, {
                    type: 1,
                    name: "PWN",
                    data: [integer, ...]
                }, {
                    type: 2,
                    name: "REVERSE",
                    data: [integer, ...]
                }, {
                    type: 3,
                    name: "CRYPTO",
                    data: [integer, ...]
                }, {
                    type: 4,
                    name: "MISC",
                    data: [integer, ...]
                }, {
                    type: 5,
                    name: "MOBILE",
                    data: [integer, ...]
                }, {
                    type: 6,
                    name: "ETH",
                    data: [integer, ...]
                }, {
                    type: 7,
                    name: "IOT",
                    data: [integer, ...]
                }, {
                    type: 8,
                    name: "AI",
                    data: [integer, ...]
                }, {
                    type: 9,
                    name: "实战",
                    data: [integer, ...]
                },
            ]
        """
        code, data = self.client._get(f'user/{uid}/statistics/solves/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_user_statistics_rating(self, uid: int) -> Dict[str, Any]:
        """
        获取用户积分曲线。相同的路径数据缓存60分钟。

        Args:
            uid参数为用户UID。

        Returns:
            返回用户参加的每场比赛排名以及积分变动数据。

            [
                {
                    date: integer,
                    rating: integer,
                    title: string,
                    rank: integer,
                    unrated: boolean,
                    nums: integer
                }
            ]
        """
        code, data = self.client._get(f'user/{uid}/statistics/rating/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_user_statistics_radar(self, uid: int) -> Dict[str, Any]:
        """
        获取用户能力雷达图数据。相同的路径数据缓存60分钟。

        Args:
            uid参数为用户UID。

        Returns:
            返回一个列表，包含用户各方向解题数据，其中一共六项，分别代表WEB、PWN、REVERSE、CRYPTO、MISC、OTHER方向解题数据，每项数据都为[解题数, 总题数]的列表

            [
                {
                    date: integer,
                    rating: integer,
                    title: string,
                    rank: integer,
                    unrated: boolean,
                    nums: integer
                }
            ]
        """
        code, data = self.client._get(f'user/{uid}/statistics/radar/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_user_article_list(self, uid: int, page: int, size: int) -> Dict[str, Any]:
        """
        获取用户文章列表。相同的路径数据缓存5分钟。

        Args:
            uid参数为用户UID。page参数为页数，size参数为每页大小。

        Returns:
            返回指定页的文章数据和文章总数，文章数据按照文章ID排降序。

            {
                articles: [
                    {
                        id: integer
                        title: string,
                        date: integer,
                        type: integer
                    }, ...
                ],
                total: integer
            }
        """
        code, data = self.client._get(f'user/{uid}/article/list/{page}/{size}/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_user_following_list(self, uid: int, page: int, size: int) -> Dict[str, Any]:
        """
        获取用户关注列表。相同的路径数据缓存10分钟。

        Args:
            uid参数为用户UID。page参数为页数，size参数为每页大小。

        Returns:
            返回指定页的关注列表数据，数据按照关注时间排降序。

            [
                {
                    uid: integer,
                    username: string,
                    bio: string,
                    avatar: string
                },
            ]
        """
        code, data = self.client._get(f'user/{uid}/following/list/{page}/{size}/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_user_follower_list(self, uid: int, page: int, size: int) -> Dict[str, Any]:
        """
        获取用户粉丝列表。相同的路径数据缓存10分钟。

        Args:
            uid参数为用户UID。page参数为页数，size参数为每页大小。

        Returns:
            返回指定页的粉丝列表数据，数据按照关注时间排降序。

            [
                {
                    uid: integer,
                    username: string,
                    bio: string,
                    avatar: string
                },
            ]
        """
        code, data = self.client._get(f'user/{uid}/follower/list/{page}/{size}/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_user_picturebed_used(self) -> Dict[str, Any]:
        """
        获取图床使用情况。数据缓存10分钟。

        Returns:
            返回图床使用情况。
            
            {
                used_mem: integer,
                max_mem: integer,
                total: integer,
            }
        """
        code, data = self._get(f'user/picturebed/used/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_user_picturebed_used(self, page: int, size: int) -> Dict[str, Any]:
        """
        获取图床列表。数据缓存10分钟。
        
        Args:
            page参数为页数，size参数为每页大小。

        Returns:
            返回指定页的图床列表数据，数据按照id排降序。

            {
                pictures: [
                    {
                        id: integer,
                        name: string,
                        date: integer,
                        size: integer,
                        src: string
                    }, ...
                ],
                total: integer
            }
        """
        code, data = self.client._get(f'user/picturebed/list/{page}/{size}/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def post_user_picturebed_upload(self, filename: str, image: IO) -> Dict[str, Any]:
        """
        图床上传图片

        Args:
            filename: 文件名
            image: 文件IO流

        Returns:
            {
                id: integer,
                name: string,
                date: integer,
                size: integer,
                url: string
            }
        """
        code, data = self.client._post(f'user/picturebed/upload/', files={
            'image': (filename, image.read())
        })
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def post_user_picturebed_download(self, pid: int) -> io.BytesIO:
        """
        图床下载图片

        Args:
            pid参数为图片ID。

        Returns:
            bytes IO流
        """
        res = self.client._post(f'user/picturebed/{pid}/download/', parse=False)

        if res.headers['Content-Type'] != 'application/octet-stream':
            raise get_exception(res.json()['code'])

        return io.BytesIO(res.content)
