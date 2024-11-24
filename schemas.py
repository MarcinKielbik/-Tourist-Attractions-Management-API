from pydantic import BaseModel

class TouristAttractionBase(BaseModel):
    name: str
    description: str

class TouristAttractionCreate(TouristAttractionBase):
    pass

class TouristAttraction(TouristAttractionBase):
    id: int

    class Config:
        orm_mode = True
