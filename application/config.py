from application import app

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///sns_orm?instance=team-9203:team-9209',
    migration_directory = 'migrations'
))
