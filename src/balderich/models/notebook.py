from typing import Any, Dict
from balderich.models.resource import Collection
from balderich.utils.code import SUCCESS
from balderich.utils.exceptions import get_exception


class NotebookCollection(Collection):
    def get_notebook_info(self, nid: int) -> Dict[str, Any]:
        """
        获取当前用户可访问的文章信息。

        Args:
            nid参数为文章ID。

        Returns:
            若文章文件为PDF，则content字段为Base64编码后的字符串；否则为文章正文内容。
            {
                id: integer,
                title: string,
                upload_date: integer,
                modify_date: integer,
                tag: [string, ],
                state: integer,
                content: string,
                author: {
                    uid: integer,
                    username: string,
                    rating: integer,
                    avatar: string
                },
                info: {
                    views: integer,
                    likes: integer
                },
                like: boolean
            }
        """
        code, data = self.client._get(f'notebook/{nid}/info/')

        if code != SUCCESS:
            raise get_exception(code)

        return data
