Talk Application
I created an endpoint for each of the methods:
    GetTalks() -returns list of talks
    GetTalk(int ID) - return one talk with ID
    Insert(Talk) - POST/CREATE, add a single talk
    Update(Talk,ID) - PUT/UPDATE, update a single talk
    Delete(ID) - DELETE/DELETE, Delete a single talk


to get the endpoints: localhost/api/
    path( 'gettalks', views.GetTalks, name='GetTalks'),
    path( 'gettalks/<int:pk>', views.GetTalk, name='GetTalk'),
    path( 'insert', views.Insert, name='Insert'),
    path( 'update', views.Update, name='Update'),
    path( 'delete/<int:pk>', views.Delete, name='Delete'),