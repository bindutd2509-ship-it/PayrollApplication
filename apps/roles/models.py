import uuid
from django.db import models


class Company(models.Model):
    """
    Minimal company model reference from ER diagram.
    Only required fields added for Role connection.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    Role table based exactly on ER diagram
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Many roles belong to one company
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="roles"
    )

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    is_system_role = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "roles"
        unique_together = ("company", "name")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.company.name})"
