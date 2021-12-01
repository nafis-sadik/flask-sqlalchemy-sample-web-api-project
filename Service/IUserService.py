from WebApplication.Models.User import User
import abc

class IUserService(abc.ABC):
    def sign_up(user: User) -> bool:
        raise NotImplementedError

    def log_in(user: User) -> bool:
        raise NotImplementedError