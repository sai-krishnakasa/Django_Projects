import graphene
from graphene_django import DjangoObjectType
from .models import Product,Category


class ProductType(DjangoObjectType):
    class Meta:
        model=Product

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category


class Query(graphene.ObjectType):
    all_products=graphene.List(ProductType)
    product=graphene.Field(ProductType,id=graphene.ID())

    all_categories=graphene.List(CategoryType)

    category=graphene.Field(CategoryType,id=graphene.ID())

    def resolve_all_products(self,info,**kwargs):
        return Product.objects.all()

    def resolve_all_categories(self,info,**kwargs):
        return Category.objects.all()

    def resolve_product(self,info,id):
        return Product.objects.get(id=id)

    def resolve_category(self,info,id):
        return Category.objects.get(id=id)



class createProduct(graphene.Mutation):
    class Arguments:
        name=graphene.String()
        price=graphene.Float()
        category=graphene.List(graphene.ID)
        in_stock=graphene.Boolean()
        date_created=graphene.types.datetime.DateTime()

    product=graphene.Field(ProductType)

    def mutate(self,info,name,price=None,category=None,in_stock=True,date_created=None):
        product=Product.objects.create(
            name=name,
            price=price,
            in_stock=in_stock,
            date_created=date_created
        )

        # This is how we deal with ManyToMany
        # Loop through and add categories for our product. Simple right? 😉
        if category is not None:
            category_set = []
            for category_id in category:
                category_object = Category.objects.get(pk=category_id)
                category_set.append(category_object)
            product.category.set(category_set)

        product.save()
        return createProduct(
        product=product
        )

class Mutation(graphene.ObjectType):
    createProduct=createProduct.Field()
    
schema=graphene.Schema(query=Query,mutation=Mutation)