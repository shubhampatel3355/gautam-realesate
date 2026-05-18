from database import SessionLocal
import models
db = SessionLocal()
try:
    visitors = db.query(models.Visitor).all()
    print("Visitors found:", len(visitors))
    for v in visitors:
        print(v.__dict__)
except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    db.close()
