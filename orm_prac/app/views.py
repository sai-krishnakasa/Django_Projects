from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import sys
from io import StringIO
from contextlib import redirect_stdout

@method_decorator(csrf_exempt,name='dispatch')
class runcode(View):
    def post(self,request):
        code=request.POST['codearea']
        f = StringIO()
        try:
            with redirect_stdout(f):
                exec(code)
                output=f.getvalue()
                length=len(output)
        except Exception as e:
            output=e
            length=3
            return render(request,'index.html',{"output": output,"code":code,"length":length})
        return render(request,'index.html',{"output": output,"code":code,"length":length})
    def get(self,request):
        return render(request,'index.html')
