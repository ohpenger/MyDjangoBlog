from django.contrib.syndication.views import Feed
from.models import Post,Category
class ALLPostsRssFeed(Feed):
    title = 'Django博客'
    link ='www.slightwhisper.top'
    description ='Django blog'
    def items(self):
        return Post.objects.all()
    def item_title(self,item):
        return '[%s]%s'% (item.category,item.title)
    def item_description(self, item):
        return item.body
