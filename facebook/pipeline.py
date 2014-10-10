from facebook.models import Profile


def custom_pipeline(strategy, user, response, details, *args, **kwargs):
    
    #profile = user.profile
    #print profile
    #print profile
    '''if profile is None:
        profile = FacebookUser(user_id=user.id)
        profile.gender = response.get('gender')
        profile.link = response.get('link')
        profile.timezone = response.get('timezone')
        profile.save() '''
    print user
    print user.first_name
    print response
    print details
    url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
    print url
    print user.social_auth.get(provider='facebook').extra_data['birthdate']
    
    user_id = response['id']
    name = response['name']
    link = response['link']
    access_token = response['access_token']
    email = response['email']
    
    email = response['email']
    
    if Profile.objects.filter(email=email).exists():
            print "exist"
    else:
        
        data = Profile(person=user,user_id=user_id, name=name, link=link, access_token=access_token, email=email)
        data.save()