from django.forms.utils import ErrorList
from django import forms


class FormUserNeededMixin(object):
    def form_valid(self,form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(["User Must be logged in to post a tweet"])
            return self.form_invalid(form)


class UserOwnerMixin(FormUserNeededMixin, object):
            def form_valid(self,form):
                if form.instance.user == self.request.user:
                    return super(UserOwnerMixin, self).form_valid(form)
                else:
                    form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This user is not allowed to update this tweet"])
                    return self.form_invalid(form)


# class UserOwnerDeletetionMixin(FormUserNeededMixin,object):
#     def form_valid(self, form):
#         if form.instance.user == self.request.user:
#             return super(UserOwnerDeletetionMixin, self).form_valid(form)
#         else:
#             form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This User is not allowed to delete this tweet"])
#             return self.form_invalid(form)
