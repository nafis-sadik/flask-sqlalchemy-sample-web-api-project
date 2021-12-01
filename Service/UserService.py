from Repository.RepositoryBase import RepositoryBase
from Service.IUserService import IUserService
from WebApplication.Models.User import User
from Repository.Entities import Users


class UserService(IUserService):
    def __init__(self) -> None:
        super().__init__()

        self.user_repo = RepositoryBase(Users)

    def sign_up(self, user: User) -> bool:
        try:
            user.id = self.user_repo.max(Users.id) + 1

            user_entity: Users = Users()
            user_entity.id = user.id
            user_entity.UserName = user.UserName
            user_entity.FirstName = user.FirstName
            user_entity.LastName = user.LastName
            user_entity.Password = user.Password

            self.user_repo.add(user_entity)
            return True
        except Exception as e:
            print(str(e))

    def log_in(self, user: User) -> bool:
        print(user.UserName)