from typing import Any, Dict
from balderich.models.resource import Collection
from balderich.utils.code import SUCCESS
from balderich.utils.exceptions import get_exception


class ProblemCollection(Collection):
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
                    point: integer,
                    tags: [string,],
                    level: float,
                    author: {
                        uid: integer,
                        name: string,
                        rating: integer
                    }
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
        获取题目详细信息。数据缓存10分钟。

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

    def get_problem_sheet_list_by_page(self, page: int, size: int=10) -> Dict[str, Any]:
        """
        获取题单列表。数据缓存10分钟。

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
        获取题单详细数据。数据缓存10分钟。
        
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
        获取题单题目列表。数据缓存10分钟。

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
