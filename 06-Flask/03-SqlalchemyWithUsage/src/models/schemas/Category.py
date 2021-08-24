from manage import ma
from src.models.Category import Category
from marshmallow import fields


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_fk = True
        ordered = True
        # dump_only = ("created_at", "updated_at")


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
