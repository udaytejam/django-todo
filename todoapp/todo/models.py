from django.db import models


# class Group(models.Model):
#     group_name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.group_name


class TodoItem(models.Model):
    check = models.BooleanField(default=False)
    name = models.CharField(max_length=150)
    # group = models.ForeignKey(Group, on_delete=models.CASCASE)

    def __str__(self):
        return self.name


