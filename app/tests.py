from flask_testing import TestCase
from flask import Flask
from models import app, db, Currency, Exchange, Location, Company
import unittest

class MyTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        # pass in test configuration
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_currency_commits(self):
        one = Currency('us dollar', 'us dol', 9)
        db.session.add(one)
        db.session.commit()

        # assert currency is there
        assert one in db.session

    def test_location_commits(self):
        one = Location('USA', 'Washington D.C', 20, None)
        db.session.add(one)
        db.session.commit()

        # assert currency is there
        assert one in db.session

    def test_exchange_commits(self):
        one = Exchange('nasdaq', 200, -.04, None, None)
        db.session.add(one)
        db.session.commit()

        # assert currency is there
        assert one in db.session

    def test_company_commits(self):
        one = Company('Yahoo', 'YHD', None, None, None)
        db.session.add(one)
        db.session.commit()

        # assert currency is there
        assert one in db.session

if __name__ == "__main__" :
    unittest.main()
