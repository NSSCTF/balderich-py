from typing import Any, Dict, List
from balderich.models.resource import Collection
from balderich.utils.code import SUCCESS
from balderich.utils.exceptions import get_exception


class ProblemCollection(Collection):
    def get_problem_states(self, pids: List[int]) -> List[Dict[str, Any]]:
        """查询本人对 1 至 50 道题的解题及开题状态，按输入顺序去重。"""
        code, data = self.client._post('problem/statistics/state/', data={'pids': pids})
        if code != SUCCESS:
            raise get_exception(code)
        return data

    def get_problem_list_by_page(self, page: int, size: int=10) -> Dict[str, Any]:
        """
        获取题目列表。数据缓存10分钟。

        Args:
            page参数为页数，size参数为每页大小。

        Returns:
            {
                problems: [{
                    id: integer,
                    title: string,
                    tag: [string, ],
                    wp: boolean,
                    point: integer,
                    level: float
                },]
                total: integer
            }
        """
        code, data = self.client._get(f'problem/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data

    def get_problem_info(self, pid: int) -> Dict[str, Any]:
        """
        获取公开题目详细信息。

        Args:
            pid参数为题目ID。

        Returns:
            {
                id: interger,
                title: string,
                desc: string,
                point: number,
                tags: [string, ],
                hint: boolean,
                level: float,
                annex: boolean,
                docker: boolean,
                price: integer,
                likes: integer,
                date: integer,
                info: {
                    solved: integer,
                    wa: integer,
                }
                author: {
                    uid: integer,
                    name: string,
                    rating: integer
                }
            }
        """
        code, data = self.client._get(f'problem/{pid}/info/')

        if code != SUCCESS:
            raise get_exception(code)

        return data

    def get_problem_wp_list_by_page(self, pid: int, page: int, size: int=10) -> Dict[str, Any]:
        """
        分页获取题目题解（WP）列表及当前用户的点赞状态。

        Args:
            pid参数为题目ID，page参数为页数，size参数为每页大小，size最大为20。

        Returns:
            {
                wps: [{
                    id: integer,
                    nid: integer,
                    author: {
                        uid: integer,
                        username: string,
                        rating: integer,
                        avatar: string,
                    },
                    etags: [[string, integer], ],
                    is_like: boolean,
                    title: string,
                    date: integer,
                    desc: string,
                    tags: [string, ],
                    cover: string,
                    views: integer,
                    likes: integer,
                    comments: integer
                },],
                total: integer
            }
        """
        code, data = self.client._get(f'problem/{pid}/wp/list/{page}/{size}/')

        if code != SUCCESS:
            raise get_exception(code)

        return data

    def get_problem_daily_problem(self, date: str) -> List[Dict[str, Any]]:
        """
        获取指定日期的每日一题题目。数据缓存约 2 小时。

        Args:
            date: 日期字符串，格式 YYYY-MM-DD。仅允许当年且不晚于当天（UTC）。

        Returns:
            题目列表，每项为:
            {
                id: integer,
                title: string,
                tag: [string, ],
                wp: boolean,
                info: {
                    solved: integer,
                    wrong: integer,
                    no: integer
                },
                level: float
            }
        """
        code, data = self.client._get(f'problem/daily/{date}/problem/')

        if code != SUCCESS:
            raise get_exception(code)

        return data

    def get_problem_sheet_list_by_page(self, page: int, size: int=10) -> Dict[str, Any]:
        """
        分页获取公开、非战队题单的目录摘要。

        Args:
            page参数为页数，size参数为每页大小。

        Returns:
            {
                sheets: [{
                    id: integer,
                    title: string,
                    stars: integer,
                    count: integer,
                    author: {
                        uid: integer,
                        name: string,
                        rating: integer
                    }
                },]
                total: integer
            }
        """
        code, data = self.client._get(f'problem/sheet/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data

    def get_problem_sheet_info(self, psid: int) -> Dict[str, Any]:
        """
        获取当前用户可访问的题单详情。
        
        Args:
            psid参数为题单ID。

        Returns:
            其中type(0-2)代表题单类型，分别代表（历史比赛、官方精选、用户分享）。
            {
                id: integer,
                title: string,
                stars: integer,
                count: integer,
                type: integer,
                content: string,
                author: {
                    uid: integer,
                    name: string,
                    rating: integer
                }
            }
        """
        code, data = self.client._get(f'problem/sheet/{psid}/info/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data

    def get_problem_sheet_problem_list_by_page(self, psid: int, page: int, size: int=10) -> Dict[str, Any]:
        """
        分页获取题单中当前用户可读取的题目。

        Args:
            psid参数为题单ID。

        Returns:
            其中type(0-2)代表题单类型，分别代表（历史比赛、官方精选、用户分享）。
            {
                problems: [{
                    id: integer,
                    title: string,
                    point: integer,
                    solved: integer,
                    level: float,
                    tags: [string,],
                    index: integer
                },],
                total: integer
            }
        """
        code, data = self.client._get(f'problem/sheet/{psid}/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
