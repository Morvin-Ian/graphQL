import graphene
from graphene_django import DjangoObjectType

from .models import Student

class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = "__all__"

        # Add extra field
        extra_field = graphene.String()


class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    students_by_id = graphene.Field(StudentType)

    def resolve_all_students(root, info, **kwargs):
        return Student.objects.all()

    def resolve_students_by_id(root, info, id):
        return Student.objects.get(pk=id)

    def resolve_extra_field(self, info):
        return "Coded by Morvin"

schema = graphene.Schema(query=Query)