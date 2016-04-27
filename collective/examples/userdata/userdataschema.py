import datetime

from DateTime.DateTime import DateTime
from zope.interface import Interface
from zope.component import adapts
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from z3c.form import field
from z3c.form.browser.radio import RadioFieldWidget

from plone.supermodel import model
from plone.formwidget.datetime.z3cform.widget import DateFieldWidget
from plone.app.users.browser.account import AccountPanelSchemaAdapter
from plone.app.users.browser.userdatapanel import UserDataPanel
from plone.app.users.browser.register import RegistrationForm, AddUserForm
from plone.z3cform.fieldsets import extensible

from collective.examples.userdata.interfaces import IUserDataExamplesLayer
from collective.examples.userdata import _

from artistic.content.config import CITY


gender_options = SimpleVocabulary([
    SimpleTerm(value='Male', title=_(u'Male')),
    SimpleTerm(value='Female', title=_(u'Female')),
    ])


def validateAccept(value):
    if value is not True:
        return False
    return True


class IEnhancedUserDataSchema(model.Schema):

    city = schema.Choice(
        title=_(u'City'),
        vocabulary=CITY,
        required=False,
    )

    schoolName = schema.TextLine(
        title=_(u'School Name'),
        required=False,
    )


class EnhancedUserDataSchemaAdapter(AccountPanelSchemaAdapter):
    schema = IEnhancedUserDataSchema


class UserDataPanelExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, UserDataPanel)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        self.add(fields)


class RegistrationPanelExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, RegistrationForm)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        self.add(fields)


class AddUserFormExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, AddUserForm)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        self.add(fields)

