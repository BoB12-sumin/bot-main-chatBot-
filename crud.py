import hashlib
from sqlalchemy.orm import Session

import models
import schema

def write_access_data(access_id: str, access_item: schema.Access_Data, db: Session):
    """
    Make access id
      -- access_id = sha256(access_time + channel_id + user_id)
        Write access id to database
        Test data:
    {
        "user_id":"han",
        "channel_id":"hantest",
        "access_time":"2023-07-23T11:22:00.000000"
    }
    """
    query_result = db.query(models.Access_Table).filter(models.Access_Table.access_id == access_id).first()
    if query_result is None:
        # Homework: write access data to database fill all column
        return {"message": f"write access id {access_id}", 'result': True, 'access_id': access_id}
    else:
        return {"message": "already access id", 'result': False}