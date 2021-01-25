from django.db import models
from tagging.fields import TagField
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=100)
	blurb = MarkdownField(rendered_field='blurb_rendered', validator=VALIDATOR_STANDARD, max_length=250, default='Insert blurb here')
	blurb_rendered = RenderedMarkdownField()
	description = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
	text_rendered = RenderedMarkdownField()
	image = models.ImageField(upload_to='portfolio/images/')
	url = models.URLField(blank=True)
	tags = TagField()

	def __str__(self):
		return self.title