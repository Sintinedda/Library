from sqlite3 import IntegrityError
from datetime import datetime, timedelta
from gestion.models import *
import pytest


@pytest.mark.django_db
class TestItem:

    def check_status_member(self):
        if Loan.objects.filter(member=self.member).exists():
            if Loan.objects.filter(member=self.member).count() >= 3:
                self.member.blocked = True
                self.member.save()
            else:
                loans = Loan.objects.filter(member=self.member)
                for loan in loans:
                    datelimit = loan.date <= datetime.today().date() - timedelta(days=7)
                    if datelimit:
                        self.member.blocked = True
                        self.member.save()
                    else:
                        self.member.blocked = False
                        self.member.save()
        else:
            self.member.blocked = False
            self.member.save()

    def setup_method(self, method):
        self.item = Item.objects.create(name='item1', category='Livre', parution='2000-01-01')
        self.member = Member.objects.create(firstname='memberfn1', lastname='memberln1')
        self.loan = Loan.objects.create(item=self.item, member=self.member, date=datetime.today().date())

    def teardown_method(self, method):
        pass

    def test_same_item_name_and_same_category(self):
        i = Item()
        i.name = 'item1'
        i.category = 'Livre'
        i.parution = '2000-01-01'
        with pytest.raises(Exception) as raised:
            i.save()
            print('Item avec le meme nom et la meme categorie existe deja')
            self.assertEqual(IntegrityError, type(raised.exception))

    def test_same_item_name_and_different_category(self):
        i = Item()
        i.name = 'item1'
        i.category = 'Cd'
        i.parution = '2000-01-01'
        i.save()
        assert Item.objects.count() == 2
        assert Item.objects.filter(category='Livre').count() == 1
        assert Item.objects.filter(category='Cd').count() == 1
        print('plusieurs items avec le meme nom mais une categorie differente')

    def test_member_blocked_by_time_limit(self):
        self.loan.date = datetime.today().date() - timedelta(days=8)
        self.loan.save()
        self.check_status_member()
        assert self.member.blocked == True
        print('le membre est bloque a cause du temps de pret depasse')

    def test_member_not_blocked_by_time_limit(self):
        self.loan.date = datetime.today().date() - timedelta(days=6)
        self.loan.save()
        self.check_status_member()
        assert self.member.blocked == False
        print("le membre n'a pas encore depasse le temps, pas bloque")

    def test_member_blocked_by_items_limit(self):
        item2 = Item.objects.create(name='item2', category='Livre', parution='2000-01-01')
        item3 = Item.objects.create(name='item3', category='Cd', parution='2000-01-01')
        Loan.objects.create(item=item2, member=self.member, date=datetime.today().date())
        Loan.objects.create(item=item3, member=self.member, date=datetime.today().date())
        self.check_status_member()
        assert self.member.blocked == True
        print('le membre est bloque car il a deja 3 items')

    def test_member_not_blocked_by_items_limit(self):
        item2 = Item.objects.create(name='item2', category='Livre', parution='2000-01-01')
        Loan.objects.create(item=item2, member=self.member, date=datetime.today().date())
        self.check_status_member()
        assert self.member.blocked == False
        print("le membre n'a pas encore depasse la limite d'items")