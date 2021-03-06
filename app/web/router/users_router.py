from app.application.usecases.users.create_user_usecase import CreateUserRequest, CreateUserUsecase
from app.application.usecases.users.delete_user_usecase import DeleteUserRequest, DeleteUserUsecase
from app.application.usecases.users.find_all_users_usecase import FindAllUsersUsecase
from app.application.usecases.users.find_user_usecase import FindUserRequest, FindUserUsecase
from app.application.usecases.users.update_user_usecase import UpdateUserRequest, UpdateUserUsecase
from app.domain.entities.user import User
from typing import List
from fastapi import APIRouter, Depends

users_router = APIRouter()


@users_router.get("", response_model=List[User])
async def find_all_users(usecase: FindAllUsersUsecase = Depends()) -> List[User]:
    return await usecase.invoke()


@users_router.get("/{user_id}", response_model=User)
async def find_user(user_id: str, usecase: FindUserUsecase = Depends()) -> User:
    req = FindUserRequest(user_id=user_id)
    return await usecase.invoke(req)


@users_router.post("", response_model=User, status_code=201)
async def create_user(req: CreateUserRequest, usecase: CreateUserUsecase = Depends()) -> User:
    return await usecase.invoke(req)


@users_router.patch("/{user_id}", response_model=User, status_code=201)
async def update_user(user_id: str, req: UpdateUserRequest, usecase: UpdateUserUsecase = Depends()) -> User:
    req.user_id = user_id
    return await usecase.invoke(req)


@users_router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: str, usecase: DeleteUserUsecase = Depends()) -> None:
    req = DeleteUserRequest(user_id=user_id)
    await usecase.invoke(req)
