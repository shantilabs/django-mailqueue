from datetime import date

from django.core.exceptions import ValidationError
from base import BaseTestCase

from futubank.djutils.formfields import ExpireDateField, CurrencyCodeField


class TestFormFields(BaseTestCase):

    def test_expire_date_field(self):
        field = ExpireDateField()

        with self.assertRaises(ValidationError):
            field.clean('x1/12')

        with self.assertRaises(ValidationError):
            field.clean(r'11\12')

        with self.assertRaises(ValidationError):
            field.clean(r'11/2')

        with self.assertRaises(ValidationError):
            field.clean(r'13/13')

        with self.assertRaises(ValidationError):
            field.clean(r'-1/13')

        self.assertEqual(field.clean('1/17'), date(2017, 1, 1))
        self.assertEqual(field.clean('12/99'), date(2099, 12, 1))

    def test_currency_code_field(self):
        field = CurrencyCodeField()

        with self.assertRaises(ValidationError):
            field.clean('')

        with self.assertRaises(ValidationError):
            field.clean('123')

        with self.assertRaises(ValidationError):
            field.clean('RUBR')

        with self.assertRaises(ValidationError):
            field.clean('RU')

        with self.assertRaises(ValidationError):
            field.clean('ABC')

        self.assertEqual(field.clean('rub'), 'RUB')
        self.assertEqual(field.clean('USD'), 'USD')
