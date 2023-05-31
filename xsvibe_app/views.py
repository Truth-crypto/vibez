from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Music, Ads, FreeBeat, Video
from django.db.models import Q
# Create your views here.

# function for the xsvibez view
def index(request):
    true_ads = True
    true_video = True

    # getvideo = Video.objects.all().order_by('-created')[:5]

    try:
        true_ads = True
        true_video = True
        ads = Ads.objects.all()
        getvideo = Video.objects.all().order_by('-created')[:5]
        beatfilt = FreeBeat.objects.all().order_by('-created')[:5]

        q = request.GET.get('q')
        print(request.GET)
        if q != None:
            getmusic = Music.objects.filter(
                Q(musicname__icontains=q)|
                Q(artistname__icontains=q)).order_by('-created')
        else:
            ads = Ads.objects.all()
            q = ''
            getmusic = Music.objects.all().order_by('-created')[:5]
            getvideo = Video.objects.all().order_by('-created')[:5]
            beatfilt = FreeBeat.objects.all().order_by('-created')[:5]

    except Exception:
        true_ads = False
        true_video = False

        getmusic = Music.objects.all().order_by('-created')[:7]
        getvideo = Video.objects.all().order_by('-created')[:5]
        beatfilt = FreeBeat.objects.all().order_by('-created')[:5]

        return render(request, 'xsvibe_app/xsvibez.html', {
        'musicsfilt':getmusic,
        'ads':None,
        'getvideo':None,
        'true_ads':true_ads,
        'true_video':true_video,
        'beatfilt':beatfilt



    })

    return render(request, 'xsvibe_app/xsvibez.html', {
        'musicsfilt':getmusic,
        'ads':ads,
        'getvideo':getvideo,
        'true_ads':true_ads,
        'true_video':true_video,
        'beatfilt':beatfilt

    })

# function for the download music
def download_music(request, id):
    true_ads = True

    try:
        true_ads = True
        
        ads = Ads.objects.all()

        idget = Music.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = Music.objects.get(id=id)
        

        return render(request, 'xsvibe_app/Download music.html', {
        'musics':idget,
        'ads':None,
        'true_ads':true_ads


    })

    return render(request, 'xsvibe_app/Download music.html', {
        'musics':idget,
        'ads':ads,
        'true_ads':true_ads

        })

# listen music functions
def listen(request, id):
    true_ads = True

    try:
        true_ads = True
        
        ads = Ads.objects.all()

        idget = Music.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = Music.objects.get(id=id)
        

        return render(request, 'xsvibe_app/listen.html', {
        'musics':idget,
        'ads':None,
        'true_ads':true_ads


    })

    return render(request, 'xsvibe_app/listen.html', {
        'musics':idget,
        'ads':ads,
        'true_ads':true_ads

        })

# free beat listen function
def free_listen(request, id):
    true_ads = True

    try:
        true_ads = True
        
        ads = Ads.objects.all()

        idget = FreeBeat.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = FreeBeat.objects.get(id=id)
        

        return render(request, 'xsvibe_app/free_listen.html', {
        'musics':idget,
        'ads':None,
        'true_ads':true_ads


    })

    return render(request, 'xsvibe_app/free_listen.html', {
        'musics':idget,
        'ads':ads,
        'true_ads':true_ads

        })

# function for the listen and download 
def listen_download(request, id):
    true_ads = True

    try:
        true_ads = True
        
        ads = Ads.objects.all()

        idget = Music.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = Music.objects.get(id=id)
        

        return render(request, 'xsvibe_app/listen_download.html', {
        'musics':idget,
        'ads':None,
        'true_ads':true_ads


    })

    return render(request, 'xsvibe_app/listen_download.html', {
        'musics':idget,
        'ads':ads,
        'true_ads':true_ads

        })

# free beat listen and download
def free_listen_download(request, id):
    true_ads = True

    try:
        true_ads = True
        
        ads = Ads.objects.all()

        idget = FreeBeat.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = FreeBeat.objects.get(id=id)
        

        return render(request, 'xsvibe_app/free_listen_download.html', {
        'musics':idget,
        'ads':None,
        'true_ads':true_ads


    })

    return render(request, 'xsvibe_app/free_listen_download.html', {
        'musics':idget,
        'ads':ads,
        'true_ads':true_ads

        })


# function for the download video
def download_video(request, id):
    true_ads = True

    try:
        true_ads = True
        
        ads = Ads.objects.all()

        idget = Video.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = Video.objects.get(id=id)
        

        return render(request, 'xsvibe_app/download video.html', {
        'video':idget,
        'ads':None,
        'true_ads':true_ads


    })

    return render(request, 'xsvibe_app/download video.html', {
        'video':idget,
        'ads':ads,
        'true_ads':true_ads

        })

# function for the free beat
def free_beat(request):
    true_ads = True

    try:
        true_ads = True

        ads = Ads.objects.all()
        q = request.GET.get('q')
        print(request.GET)
        if q != None:
            getmusic = FreeBeat.objects.filter(
                Q(beatname__icontains=q)).order_by('created')
        else:
            ads = Ads.objects.all()
            q = ''
            getmusic = FreeBeat.objects.filter(
                Q(beatname__icontains=q)).order_by('created') 
    except Exception:
        true_ads = False
        getmusic = FreeBeat.objects.all()
        return render(request, 'xsvibe_app/free_beat.html', {
        'musicsfilt':getmusic,
        'ads':None,
        'true_ads':true_ads


    })
            
    return render(request, 'xsvibe_app/free_beat.html', {
        'musicsfilt':getmusic,
        'ads':ads,
        'true_ads':true_ads


    })

# function for the video
def video(request):
    true_ads = True

    try:
        true_ads = True

        ads = Ads.objects.all()
        q = request.GET.get('q')
        print(request.GET)
        if q != None:
            getvideo = Video.objects.filter(
                Q(videotitle__icontains=q)|

                Q(videoname__icontains=q)).order_by('-created')
        else:
            ads = Ads.objects.all()
            q = ''
            getvideo = Video.objects.filter(
                Q(videotitle__icontains=q)|
                Q(videoname__icontains=q)).order_by('-created') 
    except Exception:
        true_ads = False
        getvideo = Video.objects.all()
        return render(request, 'xsvibe_app/videos.html', {
        'getvideo':getvideo,
        'ads':None,
        'true_ads':true_ads


    })
            
    return render(request, 'xsvibe_app/videos.html', {
        'getvideo':getvideo,
        'ads':ads,
        'true_ads':true_ads


    })

# function for the free beat download
def free_beat_download(request, id):
    true_ads = True

    try:
        true_ads = True

        ads = Ads.objects.all()

        idget = FreeBeat.objects.get(id=id)
    except Exception:
        true_ads = False
        idget = FreeBeat.objects.get(id=id)

        return render(request, 'xsvibe_app/free_beat_download.html', {
        'musics':idget,
        'ads':None,
        'true_ads':true_ads


    })    
    return render(request, 'xsvibe_app/free_beat_download.html', {
        'musics':idget,
        'ads':ads,
        'true_ads':true_ads

        })


# function for the music
def music(request):
    true_ads = True

    try:
        true_ads = True


        ads = Ads.objects.all()

        seeallmusic = Music.objects.all().order_by('-created')
    except Exception:
        true_ads = False
        seeallmusic = Music.objects.all().order_by('-created')
        
        return render(request, 'xsvibe_app/music.html', {
        'musics':seeallmusic,

        'ads':None,
        'true_ads':true_ads


    })   
    return render(request, 'xsvibe_app/music.html', {
        'musics':seeallmusic,
        'ads':ads,
        'true_ads':true_ads

        })

