from itty import *

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
PORT = int(os.environ.get("PORT")) if os.environ.get("PORT") else 9393
INDEX = 'index.html'

def serve_media(request, filename):
    output = static_file(filename, root=STATIC_ROOT)
    return Response(output, content_type=content_type(filename))

@get('/')
def index(request):
    return serve_media(request, INDEX)

@get('/'+INDEX)
def index_redirect(request):
    raise Redirect('/')

@get('/(?P<filename>.+)')
def my_media(request, filename):
    return serve_media(request, filename)

run_itty(port=PORT,host='0.0.0.0')

# itty info: https://github.com/toastdriven/itty
