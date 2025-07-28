
from fastapi import APIRouter, HTTPException
from models.user import Train
from Auth.depend import get_current_user
from schemas.user import trainEntity, trainsEntity
from core.database import collectiontrain
from fastapi import Depends



train = APIRouter(tags=["Train"])

@train.get("/train")
def get_trains():
    trains = collectiontrain.find()
    return trainsEntity(trains)

@train.get("/trains/by-day", response_model=list[Train])
def get_trains_by_day(day: str):
    trains_cursor = collectiontrain.find({"day": day})
    trains = [trainEntity(train) for train in trains_cursor]
    return trains

@train.post("/train", response_model=Train,dependencies=[Depends(get_current_user)])
def create_train(train: Train):
    train_dict = train.dict()
    collectiontrain.insert_one(train_dict)
    return trainEntity(train_dict)

@train.put("/{train_id}", response_model=Train,dependencies=[Depends(get_current_user)])
def update_train(train_id: int, train: Train):
    update_data = train.dict()
    update_data.pop("id", None)

    result = collectiontrain.update_one({"id": train_id}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Train not found")

    updated_train = collectiontrain.find_one({"id": train_id})
    return trainEntity(updated_train)

@train.delete("/{train_id}",dependencies=[Depends(get_current_user)])
def delete_train(train_id: int):
    result = collectiontrain.delete_one({"id": train_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Train not found")
    return {"message": f"Train with ID {train_id} deleted"}