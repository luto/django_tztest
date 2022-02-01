from django.core.management.base import BaseCommand
from ...models import Post
from datetime import datetime
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        posted = timezone.now()
        p1 = Post.objects.create(posted=posted)
        p2 = Post.objects.get(pk=p1.pk)
        print(repr(p1.posted))
        print(repr(p1.posted.tzinfo))
        print(repr(p2.posted))
        print(repr(p2.posted.tzinfo))
        print("equal", p1.posted == p2.posted)
