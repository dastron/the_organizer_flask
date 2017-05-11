from ..webapp import database as db
from ..models.mixins import AnObject
from sqlalchemy import Unicode, DateTime, Boolean, ForeignKey
from sqlalchemy_utils import UUIDType


class Container(AnObject, db.Model):
    """
    Underly class for all objects in the store
    """
    # __tablename__ = 'item_attributes'

    """
    title = Column(Unicode(100), nullable=False)
    headline = Column(UnicodeText, nullable=False)
    description = Column(UnicodeText, nullable=False)

    primary_key = db.Column(Unicode(256), nullable=False)
    url = db.Column(Unicode(2042), nullable=False)

    thumbnail = db.Column(Unicode(2042))

    active = Column(Boolean, default=False)
    """

    parent_id = db.Column(UUIDType, ForeignKey('containers.id'))
    children = db.relationship("Container")
    # group_maps = db.relationship("GroupMap")
    user_id = db.Column(UUIDType, ForeignKey('users.id'))
    # submitted_date_time = db.Column(DateTime(timezone=True), nullable=False)
    # updated_date_time = db.Column(DateTime(timezone=True), nullable=False)

    @staticmethod
    def add(user_id, title, headline, primary_key, active):
        primary_key = primary_key.lower()
        return Container(user_id=user_id, title=title, primary_key=primary_key, active=active)

    def insert(self):
        db.session.add(self)
        self.save()
        return self.id

    def save(self):
        db.session.commit()

    # def add_item_attr_save(item_id, attribute, value, active):
    #     item_attrs = ItemAttribute(item_id=item_id, attribute=attribute, value=value, active=active)
    #     db.session.add(item_attrs)
    #     item_attrs.save()
    #     return item_attrs.id
