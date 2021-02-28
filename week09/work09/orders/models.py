from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    amount = models.PositiveIntegerField()
    is_cancel = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<order_id:{self.order_id};amount:{self.amount}>'
    class Meta:
      db_table = "orders"
