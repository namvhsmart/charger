from app.common.database import SessionLocal


def validate_unique(table, field, **kwargs):
    session = SessionLocal()
    q = session.query(getattr(table, field)).filter_by(**kwargs).scalar()
    session.close()
    if q:
        raise ValueError(f"""'{q}' already exist""")
    return kwargs[field]


def validate_id(table, field, **kwargs):
    session = SessionLocal()
    q = session.query(getattr(table, field)).filter_by(**kwargs).scalar()
    session.close()
    if not q:
        raise ValueError(f"""'{kwargs[field]}' does not exist""")
    return kwargs[field]
