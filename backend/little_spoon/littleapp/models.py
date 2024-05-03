from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.



class RecipeCategory(models.Model):
    """
    Admin create Recipe categories
    """
    name = models.CharField(_('Category name'), max_length=100)

    class Meta:
        verbose_name = _('Recipe Category')
        verbose_name_plural = _('Recipe Categories')

    def __str__(self):
        return self.name
    
    
def get_default_recipe_category():
    """
    Returns a default recipe type.
    """
    return RecipeCategory.objects.get_or_create(name='Others')[0]


class Recipe(models.Model):
    """
    Recipe model
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="recipes", on_delete=models.CASCADE)
    category = models.ForeignKey(
        RecipeCategory, related_name="recipe_list", on_delete=models.SET(get_default_recipe_category))
    picture = models.ImageField(upload_to='uploads')
    title = models.CharField(max_length=200)
    desc = models.CharField(_('Short description'), max_length=200)
    cook_time = models.TimeField()
    ingredients = models.TextField()
    procedure = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL , verbose_name=_(""), null=True , blank=True)
    def __str__(self):
        return self.title

    

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bookmarks = models.ManyToManyField(Recipe, related_name='bookmarked_by' , blank=True)
    avatar = models.ImageField(upload_to='avatar', blank=True)
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
    





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_info(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user= instance)
