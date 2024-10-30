from datetime import datetime, timedelta
from gestion.models import Member, Loan


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.check_status_member(request)
        return response

    def check_status_member(self, request):
        members = Member.objects.all()
        for member in members:
            if Loan.objects.filter(member=member).exists():
                if Loan.objects.filter(member=member).count() >= 3:
                    member.blocked = True
                    member.save()
                    return self.get_response(request)
                else:
                    loans = Loan.objects.filter(member=member)
                    for loan in loans:
                        if loan.date <= datetime.today().date() - timedelta(days=7):
                            member.blocked = True
                            member.save()
                            return self.get_response(request)
                        else:
                            member.blocked = False
                            member.save()
                            return self.get_response(request)
            else:
                member.blocked = False
                member.save()
                return self.get_response(request)