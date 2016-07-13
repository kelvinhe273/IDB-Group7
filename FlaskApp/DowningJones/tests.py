import unittest
from flask_testing import TestCase
from __init__ import app, db
from models import Currency, Exchange, Location, Company

class MyTest(TestCase):

    def create_app(self):
        # pass in test configuration
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        app.config['TESTING'] = True
        db.create_all()
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_currency_commits(self):
        currency = Currency('US Dollar', 'USD', "USA", "NMS", 1)
        db.session.add(currency)
        db.session.commit()

        # assert currency is in db
        self.assertIn(currency, db.session)

    def test_currency_returns(self):
        currency = Currency('US Dollar', 'USD', "USA", "NMS", 1)
        db.session.add(currency)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Currency \'us dollar\'>', str(currency.query.first()))

    def test_currency_relations(self):
        currency = Currency('US Dollar', 'USD', "USA", "NMS", 1)
        exchange = exchange = Exchange('nasdaq', 200, -.04, None, currency)
        location = location = Location('USA', 'Washington DC', '16.77 trillion USD', 'USD', 'National Market System')
        db.session.add(currency)
        db.session.add(exchange)
        db.session.add(location)
        db.session.commit()

        #assert currency is on other models
        self.assertEqual('<Exchange \'nasdaq\'>', str(currency.query.first().exchanges.first()))

        self.assertEqual('<Location \'USA\'>', str(currency.query.first().locations.first()))

    def test_location_commits(self):
        location = Location('USA', 'Washington DC', '16.77 trillion USD', 'USD', 'National Market System')
        db.session.add(location)
        db.session.commit()

        # assert location is in db
        self.assertIn(location, db.session)

    def test_location_returns(self):
        location = Location('USA', 'Washington DC', '16.77 trillion USD', 'USD', 'National Market System')
        db.session.add(location)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Location \'USA\'>', str(location.query.first()))

    def test_location_relations(self):
        currency = Currency('US Dollar', 'USD', "USA", "NMS", 1)
        location = Location('USA', 'Washington DC', '16.77 trillion USD', 'USD', 'National Market System')
        exchange = Exchange('nasdaq', 200, -.04, location, currency)
        db.session.add(location)
        db.session.add(currency)
        db.session.add(exchange)
        db.session.commit()

        #assert it returns correct data
        self.assertEqual('<Currency \'us dollar\'>', str(location.query.first().currency))

        self.assertEqual('<Exchange \'nasdaq\'>', str(location.query.first().exchanges.first()))

    def test_exchange_commits(self):
        exchange = Exchange('nasdaq', 200, -.04, None, None)
        db.session.add(exchange)
        db.session.commit()

        # assert exchange is in db
        self.assertIn(exchange, db.session)

    def test_exchange_returns(self):
        exchange = Exchange('nasdaq', 200, -.04, None, None)
        db.session.add(exchange)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Exchange \'nasdaq\'>', str(exchange.query.first()))

    def test_exchange_relations(self):
        currency = Currency('US Dollar', 'USD', "USA", "NMS", 1)
        location = Location('USA', 'Washington DC', '16.77 trillion USD', 'USD', 'National Market System')
        exchange = Exchange('nasdaq', 200, -.04, location, currency)
        db.session.add(exchange)
        db.session.add(currency)
        db.session.add(location)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Currency \'us dollar\'>', str(exchange.query.first().currency))

        self.assertEqual('<Location \'USA\'>', str(exchange.query.first().location))

    def test_company_commits(self):
        company = Company('Yahoo', 'YHD', None, None, None)
        db.session.add(company)
        db.session.commit()

        # assert company is in db
        self.assertIn(company, db.session)

    def test_company_returns(self):
        company = Company('Yahoo', 'YHD', None, None, None)
        db.session.add(company)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Company \'Yahoo\'>', str(company.query.first()))

    def test_company_relations(self):
        currency = Currency('US Dollar', 'USD', "USA", "NMS", 1)
        location = Location('USA', 'Washington DC', '16.77 trillion USD', 'USD', 'National Market System')
        exchange = Exchange('nasdaq', 200, -.04, location, currency)
        company = Company('Yahoo', 'YHD', location, exchange, currency)
        db.session.add(exchange)
        db.session.add(currency)
        db.session.add(location)
        db.session.add(company)
        db.session.commit()

        #assert it retuns correct data
        self.assertEqual('<Location \'USA\'>', str(company.query.first().location))

        self.assertEqual('<Exchange \'nasdaq\'>', str(company.query.first().exchange))

        self.assertEqual('<Currency \'us dollar\'>', str(company.query.first().currency))

if __name__ == "__main__" :
    unittest.main()
