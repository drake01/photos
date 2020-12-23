# photos

google photos
django project

```
class Album:

    name = models.CharField
    user = models.ForeignKey(User
    created = models.DateTimeField(auto_now_add=True)
```

```
class Image
    url
    user
    title
    created
    albums = models.ManyToManyField('Album')
 ```

# Task List:
* show my images only (show images for a user)

* create album for me

* show my albums

* add only my photos to albums (make sure api prevents adding to some other user's photos)


api path: http://127.0.0.1:8000/api/v1/

APIs:

```
/image/
```

```
/album/
```

```
/user/
```

INSTALLATION:
===============
```
git clone https://github.com/drake01/photos
cd photos
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python ./manage.py migrate
python ./manage.py runserver

```



using "httpie":
===============

* create users: abc and xyz:
```
http POST http://127.0.0.1:8000/api/v1/user/ email=abc@abc.com username=abc password=abc

http POST http://127.0.0.1:8000/api/v1/user/ email=xyz@xyz.com username=xyz password=xyz
```
* create some images
```
http -a abc:abc POST http://127.0.0.1:8000/api/v1/image/ title="abc image" url="abc url"
http -a abc:abc POST http://127.0.0.1:8000/api/v1/image/ title="abc image2" url="abc url2"
```

* create some images for user: xyz
```
http -a xyz:xyz POST http://127.0.0.1:8000/api/v1/image/ title="xyz image" url="xyz url"
http -a xyz:xyz POST http://127.0.0.1:8000/api/v1/image/ title="xyz image2" url="xyz url2"
```

* create albums:
```
http -a abc:abc POST http://127.0.0.1:8000/api/v1/album/ name="abc album"
http -a abc:abc POST http://127.0.0.1:8000/api/v1/album/ name="abc album2"
```
```
http -a xyz:xyz POST http://127.0.0.1:8000/api/v1/album/ name="xyz album"
```

* add image to some albums using:
```
http -a user:password PUT http://127.0.0.1:8000/api/v1/image/<image_id>/ albums:='[list of album ids]' title='new image title'
```

For example,image 2 should be added to 3 albums  with ids 1,2,3  and change title="new image title"
Client request:
```
http -a abc:abc PUT http://127.0.0.1:8000/api/v1/image/2/ albums:='[1,2,3]' title='new image title'
```

GET requests:

```
http -a abc:abc GET http://127.0.0.1:8000/api/v1/image/

http -a xyz:xyz GET http://127.0.0.1:8000/api/v1/image/
```


returns 403 without -a user:password
```
http GET http://127.0.0.1:8000/api/v1/image/ 
```

```
http -a abc:abc GET http://127.0.0.1:8000/api/v1/album/

http -a xyz:xyz GET http://127.0.0.1:8000/api/v1/album/
```

