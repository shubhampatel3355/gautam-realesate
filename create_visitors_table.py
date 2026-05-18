from database import engine
import models

print("Creating visitors table if it doesn't exist...")
# This will only create missing tables, it won't drop existing ones or modify existing schema
models.Visitor.__table__.create(bind=engine, checkfirst=True)
print("Done!")
