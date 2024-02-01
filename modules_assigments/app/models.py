from django.db import models 
import random
import datetime


class Profile(models.Model): 
  slug = models.SlugField()
  username = models.CharField(max_length = 200 ,null =True , blank = True) 
  email = models.EmailField()
  phone = models.IntegerField()
  address = models.CharField(max_length = 150)
#  Write functions to generate random data and do a bulk insert to fill these models. It should have 50000 rows for each model.
  @classmethod
  def random_Profile(self): 
    
    name_list= [ "thor" , "ironman" , " batman" , "naruto" , "saturo" , "luffy","Toji"]
    email_list = "@gmail.com"
    combinations = ['a','b','c','d','e','f','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    no = ["1","2","3","4","5","6","7","8","9","0"]
    obj_profile_list  = []
  
    for i in range(50000):
      num =   random.randint(4,7)
      for_slug  = "".join(random.sample(combinations, k=num))
      name = random.sample(name_list, k= 1)[0]
      email = name+email_list
      phone = int("".join(random.sample(no,k =10)))
      address ="house.no "+ str(num)+","+ for_slug +" "+ "area" + "," + "".join(random.sample(combinations, k=12)) 
      obj = Profile(slug = for_slug , username = name , email = email , phone = phone , address = address)
      obj_profile_list.append(obj)

    Profile.objects.bulk_create(obj_profile_list)




class Author(models.Model) : 
  slug = models.SlugField()
  name = models.CharField(max_length = 200 ,null =True , blank = True)
  profile = models.OneToOneField(Profile , on_delete = models.CASCADE)

  def author_name(self) : 
    # Return the list containing the names of the authors.
    name = Author.objects.filter(name != None)
    print(name)
    return name

  def random_Author():
    name_list = ["hill" , "green" , "shake" , "lok" , "carnegi" , "kunal" ]
    combinations = ['a','b','c','d','e','f','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   
    profiles = list(Profile.objects.all())
    author_list = []
  
    for i  in range(50000):
      num =   random.randint(4,7)
      name = random.sample(name_list, k= 1)[0]
      for_slug  = "".join(random.sample(combinations,k=num))
      obj_Author = Author(slug = for_slug , name = name , profile = profiles[i])
      author_list.append(obj_Author)
 
    Author.objects.bulk_create(author_list)

  


  # class Meta:
  #       verbose_name = "profile"
  


class Publisher(models.Model) : 
  slug = models.SlugField()
  name = models.CharField(max_length = 200 ,null =True , blank = True) 
  website = models.URLField()
  email = models.EmailField()
  address = models.CharField(max_length = 150)


  def random_Publisher():
    name_list = ["Penguin" , "Harper" ,"Simon","Macmillan","Hatchette" ]
    combinations = ['a','b','c','d','e','f','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   
    publisher_list = []
    
    for i  in range(50000):
      num =   random.randint(4,7)
      name = random.sample(name_list, k= 1)[0]
      for_slug  = "".join(random.sample(combinations,k=num))
      website = "www."+ name + ".com"
      email = name+ "@gmail.com"
      address ="office.no "+ str(num)+","+ for_slug +" "+ "street" + "," + "".join(random.sample(combinations, k=12)) 

      obj_publisher = Publisher(slug = for_slug , name = name ,website = website ,email = email ,address = address)  
      publisher_list.append(obj_publisher)

    Publisher.objects.bulk_create(publisher_list)
 


    
class Book(models.Model):
  slug = models.SlugField()
  author = models.ForeignKey(Author,on_delete = models.CASCADE)
  title = models.CharField(max_length = 100) 
  publisher = models.ForeignKey(Publisher,on_delete = models.CASCADE)
  date_of_pub =  models.DateTimeField()

  def random_Book():
    combinations = ['a','b','c','d','e','f','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   
    author = list(Author.objects.all())
    publisher = list(Publisher.objects.all())
    book_list= []

    for i  in range(50000):
      num =   random.randint(4,7)
      day = random.randint(1,27)
      month = random.randint(1,12)
      sub_year = str("20"+str(random.randint(20,24)))
    
      date_of_pub = datetime.date(int(sub_year),int(month),int(day))
      title = "".join(random.sample(combinations,k=num))

      for_slug  = "".join(random.sample(combinations,k=num))
      obj_Book = Book(slug = for_slug ,date_of_pub = date_of_pub ,
                       publisher = publisher[i], author =author[i] ,title = title)
      book_list.append(obj_Book)

    Book.objects.bulk_create(book_list)


class Collection(models.Model) : 
    slug = models.SlugField()
    name = models.CharField(max_length = 200 ,null =True , blank = True) 
    book = models.ManyToManyField(Book) 
    
    def random_Collection() : 
      combinations = ['a','b','c','d','e','f','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   
      book =  Book.objects.all()
      collection_list = []
       
      for i in range(50000) :
        num =   random.randint(4,7)
        name = "".join(random.sample(combinations,k=num))
        slug =  "".join(random.sample(combinations,k=num))

        obj_Collection =  Collection(name = name , slug = slug)
        obj_Collection.save()
        obj_Collection.book.add(random.choice(book))

        collection_list.append(obj_Collection)

      Collection.objects.bulk_create(collection_list)




      
      




  