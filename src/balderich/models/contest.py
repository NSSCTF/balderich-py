from typing import Any, Dict, List
from balderich.models.resource import Collection
from balderich.utils.code import SUCCESS
from balderich.utils.exceptions import get_exception


class ContestCollection(Collection):
    def get_pending_contests(self) -> List[Dict[str, Any]]:
        """按开始时间获取尚未开始的主站公开赛事，时间戳单位为秒。"""
        code, data = self.client._get('contest/list/pending/')
        if code != SUCCESS:
            raise get_exception(code)
        return data

    def get_contest_list(self, type: int, page: int) -> Dict[str, Any]:
        """
        获取比赛列表。数据缓存10分钟。

        Args:
            type: 比赛类型
                0 -> 公开赛事
                1 -> 私密赛事
            page: 页面参数

        Returns:
            {
                contests: [{
                    id: integer,
                    cover: string,
                    title: string,
                    level: integer,
                    mode: integer,
                    start_date: integer,
                    ends_date: integer,
                    desc: integer,
                    state: integer,
                    count: integer
                },],
                total: integer
            }
        """
        code, data = self.client._get(f'contest/{type}/list/{page}/')
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_contest_info(self, cid: int) -> Dict[str, Any]:
        """
        获取当前用户可访问的比赛详细信息。

        Args:
            cid: 比赛ID
        
        Returns:
            {
                id: integer,
                title: string,
                level: integer,
                type: integer,
                mode: integer,
                desc: integer,
                cover: string,
                top_score: integer,
                descrease_score: integer,
                start_date: integer,
                ends_date: integer,
                is_team: boolean
            }
        """
        code, data = self.client._get(f'contest/{cid}/info/')
        if code != SUCCESS:
            raise get_exception(code)

        return data
    

    def get_contest_rank_list(self, cid: int, page: int) -> Dict[str, Any]:
        """
        获取当前用户可访问的比赛榜单。

        Args:
            cid: 比赛ID
        
        Returns:
            cetegory为类型列表，包含题目类型字符串，“1”->"10"分别代表WEB->实战。
            point为分数字段，键为题目PID，值为题目当前分数。
            problems为题目详细信息列表，每项元素都为一个包含三子元素的列表，分别为PID，解题数，题目名。
            top3为前3血字典，键为题目PID，值为前三血用户UID字符串列表。
            {
                category: [string, ],
                point: {
                    integer: integer,
                },
                problems: [[integer, integer, string], ],
                top3: {
                    integer: [string, ],
                },
                solves: [{
                    uid: integer,
                    username: string,
                    rating: integer
                    solved: string,
                    solved_time: string,
                    score: integer,
                }, ],
                team: boolean,
                total: integer
            }
        """
        code, data = self.client._get(f'contest/{cid}/rank/list/{page}/')
        if code != SUCCESS:
            raise get_exception(code)

        return data
