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
        currency = Currency('us dollar', 'us dol', 9)
        db.session.add(currency)
        db.session.commit()

        # assert currency is in db
        assert currency in db.session

    def test_currency_returns(self):
        currency = Currency('us dollar', 'us dol', 9)
        db.session.add(currency)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Currency \'us dollar\'>', str(Currency.query.first()))

    def test_currency_relations(self):
        currency = Currency('us dollar', 'us dol', 9)
        exchange = exchange = Exchange('nasdaq', 200, -.04, None, currency)
        location = location = Location('USA', 'Washington D.C', 20, currency)
        db.session.add(currency)
        db.session.add(exchange)
        db.session.add(location)
        db.session.commit()

        #assert currency is on other models
        self.assertEqual('<Exchange \'nasdaq\'>', str(Currency.query.first().exchanges.first()))

        self.assertEqual('<Location \'USA\'>', str(Currency.query.first().locations.first()))

    def test_location_commits(self):
        location = Location('USA', 'Washington D.C', 20, None)
        db.session.add(location)
        db.session.commit()

        # assert location is in db
        assert location in db.session

    def test_location_returns(self):
        location = Location('USA', 'Washington D.C', 20, None)
        db.session.add(location)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Location \'USA\'>', str(Location.query.first()))

    def test_location_relations(self):
        currency = Currency('us dollar', 'us dol', 9)
        location = Location('USA', 'Washington D.C', 20, currency)
        exchange = Exchange('nasdaq', 200, -.04, location, currency)
        db.session.add(location)
        db.session.add(currency)
        db.session.add(exchange)
        db.session.commit()

        #assert it returns correct data
        self.assertEqual('<Currency \'us dollar\'>', str(Location.query.first().currency))

        self.assertEqual('<Exchange \'nasdaq\'>', str(Location.query.first().exchanges.first()))

    def test_exchange_commits(self):
        exchange = Exchange('nasdaq', 200, -.04, None, None)
        db.session.add(exchange)
        db.session.commit()

        # assert exchange is in db
        assert exchange in db.session

    def test_exchange_returns(self):
        exchange = Exchange('nasdaq', 200, -.04, None, None)
        db.session.add(exchange)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Exchange \'nasdaq\'>', str(Exchange.query.first()))

    def test_exchange_relations(self):
        currency = Currency('us dollar', 'us dol', 9)
        location = Location('USA', 'Washington D.C', 20, currency)
        exchange = Exchange('nasdaq', 200, -.04, location, currency)
        db.session.add(exchange)
        db.session.add(currency)
        db.session.add(location)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Currency \'us dollar\'>', str(Exchange.query.first().currency))

        self.assertEqual('<Location \'USA\'>', str(Exchange.query.first().location))

    def test_company_commits(self):
        company = Company('Yahoo', 'YHD', None, None, None)
        db.session.add(company)
        db.session.commit()

        # assert company is in db
        assert company in db.session

    def test_company_returns(self):
        company = Company('Yahoo', 'YHD', None, None, None)
        db.session.add(company)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Company \'Yahoo\'>', str(Company.query.first()))

    def test_company_relations(self):
        currency = Currency('us dollar', 'us dol', 9)
        location = Location('USA', 'Washington D.C', 20, currency)
        exchange = Exchange('nasdaq', 200, -.04, location, currency)
        company = Company('Yahoo', 'YHD', location, exchange, currency)
        db.session.add(exchange)
        db.session.add(currency)
        db.session.add(location)
        db.session.add(company)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Location \'USA\'>', str(Company.query.first().location))

        self.assertEqual('<Exchange \'nasdaq\'>', str(Company.query.first().exchange))

        self.assertEqual('<Currency \'us dollar\'>', str(Company.query.first().currency))

if __name__ == "__main__" :
    unittest.main()
