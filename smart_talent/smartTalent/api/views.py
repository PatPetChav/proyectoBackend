from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):

    def get(self,request):
        context = {
            'ok':True,
            'message':'el servidor de SmartTalent esta activo aqui!'
        }
        return Response(context)