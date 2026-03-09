from database import SessionLocal
import models

def main():
    db = SessionLocal()
    properties = db.query(models.Property).all()
    count = 0
    for p in properties:
        if not p.bgm_id:
            p.bgm_id = f"BGM-{p.id:04d}"
            count += 1
    db.commit()
    db.close()
    print(f"Updated {count} properties")

if __name__ == "__main__":
    main()
