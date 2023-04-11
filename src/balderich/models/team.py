from balderich.models.resource import Collection
from balderich.utils.code import SUCCESS
from balderich.utils.exceptions import get_exception
from typing import Any, Dict, List

class TeamCollection(Collection):
    def get_team_list_by_page(self, page: int, size: int=10) -> Dict[str, Any]:
        """
        获取团队列表。数据缓存10分钟。
        
        Args:
            page参数为页数，size参数为每页大小。

        Returns:
            {
                teams: [{
                    id: integer,
                    name: string,
                    bio: integer,
                    date: integer,
                    user: {
                        uid: integer,
                        rating: integer,
                        username: string
                    },
                    nums: integer
                },],
                total: integer
            }
        """
        code, data = self.client._get(f'team/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_info(self, tid: int) -> Dict[str, Any]:
        """
        获取团队详细信息。数据缓存10分钟。
        
        Args:
            tid参数为团队ID。

        Returns:
            {
                id: integer,
                name: string,
                bio: integer,
                date: integer,
                avatar: string,
                user: {
                    uid: integer,
                    rating: integer,
                    username: string
                },
                nums: integer
            }
        """
        code, data = self.client._get(f'team/{tid}/info/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_notice(self) -> Dict[str, Any]:
        """
        获取团队通知信息。数据缓存10分钟。

        Returns:
            {
                notice: string
            }
        """
        code, data = self.client._get(f'team/notice/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def put_team_clockin(self) -> Dict[str, Any]:
        """
        团队每日打卡

        Returns:
            {
                state: boolean,
                nums: integer
            }
        """
        code, data = self.client._put(f'team/clockin/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_problem_list_by_page(self, page: int, size: int=10) -> Dict[str, Any]:
        """
        获取团队题目列表。数据缓存10分钟。

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
                    solves: integer,
                },]
                total: integer
            }
        """
        code, data = self.client._get(f'team/problem/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_problem_info(self, pid: int) -> Dict[str, Any]:
        """
        获取团队题目详细信息。数据缓存10分钟。

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
        code, data = self.client._get(f'team/problem/{pid}/info/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_contest_list_by_page(self, page: int, size: int=10) -> Dict[str, Any]:
        """
        获取团队比赛列表。数据缓存10分钟。

        Args:
            page参数为页数，size参数为每页大小。

        Returns:
            其中state的值从[0-2]，分别代表未开始、进行中和已结束。
            {
                contests: {
                    [
                        id: integer,
                        cover: string,
                        title: string,
                        start_date: integer,
                        ends_date: integer,
                        is_team: boolean,
                        desc: string,
                        state: integer
                    ],
                },
                total: integer
            }
        """
        code, data = self.client._get(f'team/contest/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_contest_info(self, cid: int) -> Dict[str, Any]:
        """
        获取团队比赛详细信息。数据缓存10分钟。

        Args:
            cid参数为比赛ID。
            
        Returns:
            其中level分别为[0-4]代表个人公开赛、个人密码赛、团队公开赛和团队密码赛。
            {
                title: string,
                level: integer,
                type: integer,
                mode: integer,
                desc: string,
                cover: string,
                top_score: integer,
                decrease_score: integer,
                start_date: integer,
                ends_date: integer,
            }
        """
        code, data = self.client._get(f'team/contest/{cid}/info/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_contest_rank_list_by_page(self, cid: int, page: int) -> Dict[str, Any]:
        """
        获取团队比赛榜单列表。相同的路径数据缓存60秒。

        Args:
            cid参数为比赛ID。page参数为页数。

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
        code, data = self.client._get(f'team/contest/{cid}/rank/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_user_list_by_page(self, page: int, size: int=10) -> Dict[str, Any]:
        """
        获取团队成员列表。数据缓存10分钟。
        
        Args:
            page参数为页数，size参数为每页大小。

        Returns:
            返回内容中role为用户角色，其中[0,1,2]分别代表[成员，管理员，队长]
            {
                users: [{
                    id: integer,
                    uid: integer,
                    username: string,
                    rating: integer,
                    alias: string,
                    date: integer,
                    role: integer
                },],
                total: integer
            }
        """
        code, data = self.client._get(f'team/user/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_apply_list_by_page(self, page: int, size: int=10) -> Dict[str, Any]:
        """
        获取团队申请列表，访问此API需要团队管理员及以上权限。数据缓存10分钟。

        Args:
            page参数为页数，size参数为每页大小。

        Returns:
            {
                users: [{
                    id: integer,
                    uid: integer,
                    username: string,
                    rating: integer,
                    msg: string,
                    date: integer
                },],
                total: integer
            }
        """
        code, data = self.client._get(f'team/user/apply/list/{page}/{size}/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_analysis_use(self) -> Dict[str, Any]:
        """
        获取团队使用情况，访问此API需要团队管理员及以上权限。数据缓存10分钟。

        Returns:
            {
                problem: {
                    now: integer,
                    max: integer
                },
                contest: {
                    now: integer,
                    max: integer
                },
                memory: {
                    now: float,
                    max: integer
                },
                person: {
                    now: integer,
                    max: integer
                },
                level: integer,
                state: integer
            }
        """
        code, data = self.client._get(f'team/analysis/use/')
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def post_team_analysis_solves_curve(self, uids: List[int]) -> Dict[str, Any]:
        """
        获取团队解题曲线数据，访问此API需要团队管理员及以上权限。数据缓存10分钟。

        Args:
            uids: [integer, ]

        Returns:
            获取最近三月做题时间戳列表
            {
                integer: [interger, ]
            }
        """
        code, data = self.client._post(f'team/analysis/solves/curve/', data={
            'uids': uids
        })
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
    
    def get_team_statistics_day(self, uids: str) -> Dict[str, Any]:
        """
        获取团队每日解题数据，访问此API需要团队管理员及以上权限。数据缓存10分钟。

        Args:
            uids: [integer, ]

        Returns:
            {
                integer: {
                    count: integer,
                    sum_score: integer,
                    team_count: integer,
                    team_sum_score: integer
                }
            }
        """
        code, data = self.client._post(f'team/statistics/day/', data={
            'uids': uids
        })
        
        if code != SUCCESS:
            raise get_exception(code)

        return data
