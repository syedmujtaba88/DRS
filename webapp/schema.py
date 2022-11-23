import graphene
from django.db import models
from graphene_django import DjangoObjectType, DjangoListField
from django.db.models import Count, Case, When, Sum
from .models import NumberSync, DeviceSync, FixedNumberSync, Jobs


class SystemSummaryType(graphene.ObjectType):
    system_name = graphene.String()
    completed_jobs = graphene.Int()
    pending_jobs = graphene.Int()


class JobSummaryBySystemType(DjangoObjectType):
    class Meta:
        model = Jobs
        fields = "__all__"


class JobDetailsType(DjangoObjectType):
    class Meta:
        model = NumberSync
        fields = '__all__'


class Query(graphene.ObjectType):

    system_summary = graphene.List(SystemSummaryType)
    job_summary_by_system = graphene.List(
        JobSummaryBySystemType, system=graphene.String(), pending=graphene.Int())
    job_details = DjangoListField(JobDetailsType)

    def resolve_system_summary(self, info):
        #system | completed | pending
        result = (Jobs.objects.values('target_system').annotate(Completed_Jobs=Sum(Case(When(pending_records=0, then=1), default=0), output_field=models.IntegerField(
        )), Pending_Jobs=Sum(Case(When(pending_records=1, then=1), default=0), output_field=models.IntegerField())).values_list('target_system', 'Completed_Jobs', 'Pending_Jobs'))
        return [SystemSummaryType(system_name=i[0], completed_jobs=i[1], pending_jobs=i[2]) for i in result]

    def resolve_job_summary_by_system(self, info, system, pending):
        return Jobs.objects.filter(target_system=system, pending_records=pending)


schema = graphene.Schema(query=Query)
