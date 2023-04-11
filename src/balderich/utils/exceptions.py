from balderich.utils.code import *

class AuthNoneException(Exception): ...
class AuthNotExistException(Exception): ...
class AuthErrorSignException(Exception): ...
class AuthTimeoutException(Exception): ...
class AuthCalcErrorException(Exception): ...
class AuthRequestFastException(Exception): ...
class RequestPramInvaildException(Exception): ...

class UserNotExistException(Exception): ...
class UserCloseFollowException(Exception): ...
class UserImageNoneException(Exception): ...
class UserImageFormatErrorException(Exception): ...
class UserImageOpenErrorException(Exception): ...
class UserMemoryNotEnoughException(Exception): ...
class UserImageNotExistException(Exception): ...

class ProblemNotExistException(Exception): ...
class ProblemPermissionDeniedException(Exception): ...
class ProblemSheetNotExistException(Exception): ...
class ProblemSheetPermissionDeniedException(Exception): ...

class ContestNotExistException(Exception): ...
class ContestPermissionDeniedException(Exception): ...

class TeamNotExistException(Exception): ...
class TeamPermissionDeniedException(Exception): ...
class TeamNoMemberException(Exception): ...
class TeamMethodPermissionDeniedException(Exception): ...
class TeamProblemNotExistException(Exception): ...
class TeamProblemPermissionDeniedException(Exception): ...
class TeamContestNotExistException(Exception): ...
class TeamContestPermissionDeniedException(Exception): ...


def get_exception(code: int, msg: str='') -> Exception:
    if code == AUTH_NONE:
        return AuthNoneException(msg)
    elif code == AUTH_NOT_EXIST:
        return AuthNotExistException(msg)
    elif code == AUTH_NOT_EXIST:
        return AuthErrorSignException(msg)
    elif code == AUTH_ERROR_SIGN:
        return AuthErrorSignException(msg)
    elif code == AUTH_TIMEOUT:
        return AuthTimeoutException(msg)
    elif code == AUTH_CALC_ERROR:
        return AuthCalcErrorException(msg)
    elif code == AUTH_REQUEST_FAST:
        return AuthRequestFastException(msg)
    elif code == REQUEST_PARAM_INVALID:
        return RequestPramInvaildException(msg)

    elif code == USER_NOT_EXIST:
        return UserNotExistException(msg)
    elif code == USER_CLOSE_FOLLOW:
        return UserCloseFollowException(msg)
    elif code == USER_IMAGE_NONE:
        return UserImageNoneException(msg)
    elif code == USER_IMAGE_FORMAT_ERROR:
        return UserImageFormatErrorException(msg)
    elif code == USER_IMAGE_OPEN_ERROR:
        return UserImageOpenErrorException(msg)
    elif code == USER_MEMORY_NOT_ENOUGH:
        return UserMemoryNotEnoughException(msg)
    elif code == USER_IMAGE_NOT_EXIST:
        return UserImageNotExistException(msg)
    
    elif code == PROBLEM_NOT_EXIST:
        return ProblemNotExistException(msg)
    elif code == PROBLEM_PEMISSION_DENIED:
        return ProblemPermissionDeniedException(msg)
    elif code == PROBLEM_SHEET_NOT_EXIST:
        return ProblemSheetNotExistException(msg)
    elif code == PROBLEM_SHEET_PEMISSION_DENIED:
        return ProblemSheetPermissionDeniedException(msg)
    
    elif code == CONTEST_NOT_EXIST:
        return ContestNotExistException(msg)
    elif code == CONTEST_PERMISSION_DENIED:
        return ContestPermissionDeniedException(msg)
    
    elif code == TEAM_NOT_EXIST:
        return TeamNotExistException(msg)
    elif code == TEAM_PERMISSION_DENIED:
        return TeamPermissionDeniedException(msg)
    elif code == TEAM_NO_MEMBER:
        return TeamNoMemberException(msg)
    elif code == TEAM_METHOD_PERMISSION_DENIED:
        return TeamMethodPermissionDeniedException(msg)
    elif code == TEAM_PROBLEM_NOT_EXIST:
        return TeamProblemNotExistException(msg)
    elif code == TEAM_PROBELM_PERMISSION_DENIED:
        return TeamProblemPermissionDeniedException(msg)
    elif code == TEAM_CONTEST_NOT_EXIST:
        return TeamContestNotExistException(msg)
    elif code == TEAM_CONTEST_PERMISSION_DENIED:
        return TeamContestPermissionDeniedException(msg)
