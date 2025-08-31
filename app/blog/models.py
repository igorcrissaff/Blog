from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class BlogIndexPage(Page):
    pass

class PostPageTag(TaggedItemBase):
    content_object = ParentalKey('PostPage', on_delete=models.CASCADE, related_name='tagged_items')

class PostPage(Page):
    date = models.DateField("Data de publicação", auto_now=True)
    intro = models.CharField(max_length=1000)
    body = RichTextField(verbose_name="Conteúdo")
    tags = ClusterTaggableManager(through=PostPageTag, blank=True)
    

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='Imagem',
    )

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('tags'),
    ]