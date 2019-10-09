import unittest

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    """Seeds the database."""
    db.session.add(User(username="ruslan", email="218.run@gmail.com"))
    db.session.add(User(username="fletcher", email="fletcher@notreal.com"))
    db.session.commit()


@cli.command("test")
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover("project/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
