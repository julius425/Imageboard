from django.db import models


class PostTemplate(models.Model):
    """
    Parent template for post-like models.
    """
    # attributes
    text = models.TextField()
    image = models.ImageField(
        blank=True, upload_to='uploads'
    )

    # methods
    def __str__(self):
        return str(self.id)

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    # meta
    class Meta:
        ordering = ['id']


class ThreadModel(PostTemplate):
    """
    Thread. Contains numerous Posts.
    """
    # relations
    parent = models.OneToOneField(PostTemplate, parent_link=True,
                                  related_name='+', on_delete=models.CASCADE)

    # methods
    def __str__(self):
        return str(self.id)


class PostModel(PostTemplate):
    """
    Post model.
    """
    parent = models.OneToOneField(PostTemplate, parent_link=True,
                                  related_name='+', on_delete=models.CASCADE)
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE)

    # methods
    def __str__(self):
        return str(self.id)
