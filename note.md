<i>프로젝트 진행시 발생했던 이슈, 새롭게 알게 된 내용들 간단히 정리, 내용이 길어지면 블로그에 따로 정리하고 링크  </i>   
   
</hr>
   
### Django Generic View     
    
[장고 제네릭뷰 정리](https://eunhyejung.github.io/python/2018/09/18/django-generic-view.html)   
     
- - -   
  
### reverse(), reverse_lazy()  
    
django 2.0 이후로 <b>django.core.urlresolvers</b>는 없어지고 <b>django.urls</b>로 대체됨.  

 `reverse()` 함수는 URL 패턴을 만들어주는 장고의 내장 함수
URL 패턴명을 인식하기 위해서는 urls.py 모듈이 메모리에 로딩되어야 하는데, views.py 모듈이 로딩되고 처리되는 시점에 urls.py 모듈이 로딩되지 않을 수 있다. 이를 방지하기 위해 reverse()함수 대신 `reverse_lazy()` 함수를 사용한다.    
  
자세한 사항은 [장고 공식 문서 :  django.urls](https://docs.djangoproject.com/ko/2.1/ref/urlresolvers/#reverse)을 참고.    
  
- - -   
