>>> from django.contrib.auth.models import User
>>> from News_Portal.models import *
>>> u1=User.objects.create_user('Мария')
>>> u2=User.objects.create_user('Николай')
>>> a1=Author.objects.create(user=u1)
>>> a2=Author.objects.create(user=u2)
>>> cat1=Category.objects.create(name='«Интернет»')
>>> cat2=Category.objects.create(name='«Культура»')
>>> cat3=Category.objects.create(name='«Наука и технологии»')
>>> cat4=Category.objects.create(name='«Общество»') 
>>> p1=Post.objects.create(title_of_post="Состоялся релиз Assassin's Creed Nexus VR",author=Author.objects.get(id=1),post_text="Состоялся релиз Assassin's Creed Nexus VR — приключений ассасинов на платформе виртуальной реальности Quest Pro, Quest 2 и Quest 3.")
>>> p2=Post.objects.create(title_of_post="В больницах Москвы появились роботы-помощники «робокошки»",author=Author.objects.get(id=2),post_text="«Они умеют доставлять еду и медицинские принадлежности, провожать пациентов, например, до лифта и в комнату отдыха, а по пути делиться полезными советами о поддержании своего здоровья. Роботы разгружают сотрудников и помогают им сосредоточиться на выполнении медицинских обязанностей», — отмечает заммэра Москвы")
>>> p3=Post.objects.create(title_of_post="В России появился фигурист-император. Его нужно показывать миру",author=Author.objects.get(id=1),post_text="На этапе Гран-при России по фигурному катанию в Самаре в соревнованиях мужчин 
победил 21-летний Петр Гуменник. Это было настолько убедительно, что творчество фанатов породило знаковое прозвище для фигуриста, которое тут же расползлось яркими буквами по самодельным плакатам на арене.",news_or_article="news")
>>> c1=Comment.objects.create(comment_text="text comment1",user=a1,post=p1) 
>>> c2=Comment.objects.create(comment_text="text comment2",user=a1,post=p2)
>>> c3=Comment.objects.create(comment_text="text comment3",user=a2,post=p3)
>>> c4=Comment.objects.create(comment_text="text comment1",user=a1,post=p3)
>>> p1.category.add(cat4)
>>> p1.category.add(cat1)
>>> p2.category.add(cat3)
>>> p2.category.add(cat1)
>>> p3.category.add(cat3)
>>> p3.category.add(cat1)
>>> c2.like()
>>> c1.like()
>>> p3.category.add(cat4) 
>>> c2.dislike()
>>> c3.dislike()
>>> c3.like() 
>>> c3.like() 
>>> c4.like()
>>> p1.like()
>>> p1.like()
>>> p1.dislike()
>>> p2.like() 
>>> p2.like()
>>> p2.like()
>>> p3.dislike()
>>> p3.like() 
>>> a1.update_rating()
>>> a2.update_rating()
>>> best_user=Author.objects.prefetch_related().all().order_by('-Author_rating').values('user__username', 'Author_rating',).first()
>>> print(best_user)
>>> best_post_id=Post.objects.all().order_by('-post_rating').values('id').first()
>>> print(str(Post.objects.all().order_by('-post_rating').values('date_of_post','author__user__username','post_rating','title_of_post').first()) + 'preview:' + Post.objects.get(id=best_post_id.get('id')).preview())
>>> print(Comment.objects.filter(post=Post.objects.get(id=best_post_id.get('id'))).values('date_of_comment','user__user__username','comment_rating','comment_text'))
