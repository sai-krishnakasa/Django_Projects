from graphene_django import DjangoObjectType
import graphene
from .models import book

class BookType(DjangoObjectType):
    class Meta:
        model=book
        
        
class Query(graphene.ObjectType):
    all_books=graphene.List(BookType)
    def resolve_all_books(root,info):
        return book.objects.all()



class delete_book(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        
    Book=graphene.Field(BookType)

    @classmethod
    def mutate(cls,self,info,id):
        Book=book.objects.get(id=id)
        Book.delete()
        return delete_book(Book=Book)

class create_book(graphene.Mutation):
    class arguments:
        title=graphene.String(required=True)
        desc=graphene.String(required=True)

    cool=graphene.Field(BookType)
    
    @classmethod
    def mutate(cls,self,info,title,desc):
        cool=book.objects.create(title=title,desc=desc)
        cool.save()
        return create_book(cool=cool)

    # @graphene.resolve_only_args
    # def resolve_users(self):
    #     return book.objects.all()
class Mutation(graphene.ObjectType):
    delete_book=delete_book.Field()
    create_book=create_book.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)

