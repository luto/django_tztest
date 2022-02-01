from django.core.management.base import BaseCommand
from ...models import Post
from datetime import datetime
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        posted = datetime(2022, 1, 1, 10)
        posted = timezone.make_aware(posted)
        p1 = Post.objects.create(posted=posted)
        p2 = Post.objects.get(pk=p1.pk)
        print(p1.posted)
        print(p2.posted)
