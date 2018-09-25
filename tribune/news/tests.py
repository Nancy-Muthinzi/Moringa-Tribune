from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class TestClassEditor(TestCase):
    #setup method
    def setUp(self):
        self.nancy= Editor(first_name = 'Nancy', last_name = 'Muthinzi', email = 'kathinimuthinzi@gmail.com')

    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nancy,Editor))   

    #save method
    def test_save_method(self):
        self.nancy.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    #delete method
    def test_delete_method(self):
        self.nancy.save_editor()
        self.nancy.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)    

    # retrieve all editors
    def test_can_retrieve_all_editors(self):
        self.nancy.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 1) 
        
    #test update method
    def test_can_update_editors(self):
        self.nancy.save_editor()
        edit = Editor.objects.filter(first_name='Nancy').update(first_name= 'NANCY')
        fetch_edit = Editor.objects.get(first_name='NANCY')
        self.assertEqual(fetch_edit.first_name,'NANCY')


class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.nancy= Editor(first_name = 'Nancy', last_name ='Muthinzi', email ='nanciekathini@gmail.com')
        self.nancy.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_can_get_news_by_date(self):
        test_date = '2017-01-05'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0 )
