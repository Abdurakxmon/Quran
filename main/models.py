from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Surai(models.Model):
	number=models.CharField(max_length=50, null=True)
	name_ar = models.CharField(max_length=50)
	name_en = models.CharField(max_length=50)
	slug = models.SlugField(unique=True, null=True)
	translation_en = models.CharField(max_length=50)
	number_of_Ayah = models.CharField(max_length=50)
	audio = models.CharField(max_length=200)
	desc = RichTextField()

	class Meta:
		verbose_name = 'Surai'
		verbose_name_plural = 'Surai'

	def __str__(self):
		return f"Surai - {self.name_en}"
	
	def get_surai(self):
		return reverse('main:surai_detail', kwargs={'surai_slug':self.slug})

class Ayah(models.Model):
	experiences = models.ForeignKey(Surai, on_delete=models.CASCADE)
	text_ar = RichTextField()
	text_uz = RichTextField()
	audio = models.CharField(max_length=200, null=True)
	chapter = models.CharField(max_length=50, null=True)
	verse = models.CharField(max_length=50, null=True)
	verse_ar = models.CharField(max_length=50, null=True)
	

	class Meta:
		verbose_name = 'Ayah'
		verbose_name_plural = 'Ayah'