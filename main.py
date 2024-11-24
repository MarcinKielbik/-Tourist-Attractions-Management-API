from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from . import models, schemas, database
import models, schemas, database


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/attractions/", response_model=schemas.TouristAttraction)
def create_attraction(attraction: schemas.TouristAttractionCreate, db: Session = Depends(database.get_db)):
    db_attraction = models.TouristAttraction(**attraction.dict())
    db.add(db_attraction)
    db.commit()
    db.refresh(db_attraction)
    return db_attraction

@app.get("/attractions/{attraction_id}", response_model=schemas.TouristAttraction)
def read_attraction(attraction_id: int, db: Session = Depends(database.get_db)):
    db_attraction = db.query(models.TouristAttraction).filter(models.TouristAttraction.id == attraction_id).first()
    if db_attraction is None:
        raise HTTPException(status_code=404, detail="Attraction not found")
    return db_attraction

@app.put("/attractions/{attraction_id}", response_model=schemas.TouristAttraction)
def update_attraction(attraction_id: int, updated_attraction: schemas.TouristAttractionCreate, db: Session = Depends(database.get_db)):
    db_attraction = db.query(models.TouristAttraction).filter(models.TouristAttraction.id == attraction_id).first()
    if db_attraction is None:
        raise HTTPException(status_code=404, detail="Attraction not found")

    db_attraction.name = updated_attraction.name
    db_attraction.description = updated_attraction.description
    db.commit()
    db.refresh(db_attraction)
    return db_attraction

@app.delete("/attractions/{attraction_id}")
def delete_attraction(attraction_id: int, db: Session = Depends(database.get_db)):
    db_attraction = db.query(models.TouristAttraction).filter(models.TouristAttraction.id == attraction_id).first()
    if db_attraction is None:
        raise HTTPException(status_code=404, detail="Attraction not found")

    db.delete(db_attraction)
    db.commit()
    return {"detail": "Attraction deleted successfully"}
