from django.db import models
from django.forms import ValidationError

class Employee(models.Model):
    full_name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    hire_date = models.DateField()
    email = models.EmailField()
    head = models.ForeignKey('self', 
                             on_delete = models.SET_NULL, 
                             null = True,
                             blank = True)
    
    def clean(self):
        if self.head:
            current_head = self.head
            while current_head:
                if current_head == self:
                    raise ValidationError('Cyclic dependence is not allowed.')
                current_head = current_head.head

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        childs = Employee.objects.filter(head = self)
        older_child = childs.order_by('hire_date').first()
        older_child.head = self.head
        new_parent = older_child 

        for child in childs:
            if child != new_parent:
                child.head = new_parent
                child.save()

        super().delete(*args, **kwargs)