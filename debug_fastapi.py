from database import SessionLocal
import main
import schemas

db = SessionLocal()
try:
    visitors = main.get_visitors(db=db)
    print("Fetched visitors:", len(visitors))
    # Test pydantic validation
    for v in visitors:
        validated = schemas.VisitorResponse.model_validate(v)
        print("Validated:", validated.id)
except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    db.close()
