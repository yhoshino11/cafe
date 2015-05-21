import unittest
from django.test import TestCase as DjangoTest

from menu.models import Tea
from menu.forms import TeaSearchForm


row = lambda L: (dict(zip(L[0], x)) for x in L[1:])


class TeaManagerTest(DjangoTest):
    def setUp(self):
        datas = (
            ("name", "kind"),
            ("darjeeling", "english"),
            ("suryalanka", "english"),
            ("oolong", "chinese"),
            ("tei-kuan-yin", "chinese"),
            ("pu-erh", "chinese"),
            ("shizuoka", "japanese")
            )

        for data in row(datas):
            Tea.objects.create(price=100, **data)


    def test_count_each_kind(self):
        result = Tea.objects.count_each_kind()

        self.assertEqual(result, dict(english=2, chinese=3, japanese=1))


class TeaSearchFormTest(unittest.TestCase):
    def test_valid(self):
        """Validate not to raise error when input was correct."""
        params = dict(name="foo", kind=["english"])
        form = TeaSearchForm(params)

        self.assertEqual(form.is_valid(), True, form.errors.as_text())


    def test_either1(self):
        """Validate to raise error when name and kind were not received either."""
        params = dict()
        form = TeaSearchForm(params)

        self.assertEqual(form.is_valid(), False, form.errors.as_text())


    def test_either2(self):
        """Validate not to raise error when name was received."""
        params = dict(name="foo")
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())


    def test_either3(self):
        """Validate not to raise error when kind was received."""
        params = dict(kind=["english", "chinese"])
        form = TeaSearchForm(params)
        self.assertEqual(form.is_valid(), True, form.errors.as_text())
