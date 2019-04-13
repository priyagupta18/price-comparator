from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
# Create your views here.
import re
from django.http import HttpResponse
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
def urls(url):
    page=requests.get(url)    
    soup=BeautifulSoup(page.text,'html.parser')
    return soup

def test(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box',None)   
        #search_query="Lava GEM"
      
        for k in range(1,11):
            url =f'https://www.amazon.in/s?rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031&page=3&qid=1554742933&ref=lp_1389432031_pg_{k}'
            page=requests.get(url, headers=headers)
            soup=BeautifulSoup(page.text,'html.parser')
#            soup=BeautifulSoup(page.text,'html.parser')
            w=soup.find_all(attrs={"class" : "a-size-base-plus a-color-base a-text-normal"})
            for i in range(len(w)):
                f=re.findall(f'^{search_query}',w[i].text)
                if (f):
                    a_name=w[i].text
                    ccost=soup.find_all(attrs={"class":"a-price-whole"})
                    a_cost=ccost[i].text
                    sitee=soup.find_all('a',{'class':'a-link-normal a-text-normal'})
                    par_site=sitee[i]['href']
                    a_fullsite="https://www.amazon.in"+par_site
                    sstar=soup.find_all(attrs={"class":"a-icon-alt"})
                    a_star=sstar[i].text
                    rrview=soup.find_all(attrs={"class":"a-size-base"})
                    a_review=rrview[i].text
                    context={
                        'a_star':a_name,
                        'a_cost':a_cost,
                        'a_site':a_fullsite,
                    }
                    #return render(request,'compare/search.html',context)
                    
                    ama=1
                    break
                else:
                    a_name="not"
                    a_cost="null"
                    a_star="zero"
                    context={
                        'a_star':a_name,
                        'a_cost':a_cost,
                    }
                    ama=0
                    continue
            break
   # return render(request,'compare/index.html')       





        for j in range(1,11):
            url=f'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&otracker=product_breadCrumbs_Mobiles&page={j}'
            flip=urls(url)
            jati=flip.find_all('div',{'class':'_3wU53n'})
            #priya=flip.find_all('div',{'class':'_1vC4OE _2rQ-NK'})
            for i in range(len(jati)):
                f=re.findall(f'^{search_query}',jati[i].text)
                    #return HttpResponse("hey")
                if (f):
                    p_name= jati[i].text
                    cost=flip.find_all('div',{'class':'_1vC4OE _2rQ-NK'})
                    p_cost=cost[i].text
                    site=flip.find_all('a',{'class':'_31qSD5'})
                    partial_site=site[i]['href']
                    p_fullsite="https://www.flipkart.com"+partial_site
                    det=flip.find_all('div',{'class':'_1UoZlX'})
                    p_det=det[i]
                    for a in flip.findAll('a'):
                        del a['href']
                    test=flip.find_all('div',{'class':'hGSR34'}) 
                    p_test=test[i].text
                    t=flip.find_all('span',{'class':'_38sUEc'})
                    ty=t[i].text
                    pic=flip.find_all('img',{'class':'_1Nyybr  _30XEf0'})
                        #p_pic=pic[i]
                        #x=p_pic['src']
                    context.update({
                      #  'a_star':a_name,
                       # 'a_cost':a_cost,
                        'f_name':p_name,
                        'f_site':p_fullsite,
                        'f_cost':p_cost,
                        'f_det':p_det,
                        'f_ty':ty,
                        'f_test':p_test,
                     #   'p':x,
                       # 'a_cost':a_cost,
                       # 'a_star':a_star,
                           }) 
                   ##test=flip.find_all('div',{'class':'MOBF54P4G66ZBJ9K'})
                    #return HttpResponse(p_det)
                    #return render(request,'compare/search.html',context)
                    flip=1
                    break
                else:
                    
                    p_name="no"
                    p_fullsite="no"
                    p_cost="no"
                    p_det="no"
                    ty="no"
                    p_test="no"
                    context.update({
                        'a_star':a_name,
                        'a_cost':a_cost,
                        'f_name':p_name,
                        'f_site':p_fullsite,
                        'f_cost':p_cost,
                        'f_det':p_det,
                        'f_ty':ty,
                        'f_test':p_test,})
                    flip=0
                    continue
            break 
                       #return HttpResponse("no")
        return render(request,'compare/search.html',context)
        
            #return HttpResponse("try again")         
                        
        #return render(request,'compare/search.html',context)
    else:
        return HttpResponse("dfgd")                

    return render(request,'compare/index.html')       




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
def test(request):
    #if request.method == 'GET': # If the form is submitted

    #   search_query = request.GET.get('search_box', None)
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box')
        #return HttpResponse(search_query)
        if search_query:
            y=requests.get(url)
            x=BeautifulSoup(y.text,'html.parser')
    #print(x.prettify())
            z=x.find_all('div',{'class':'_3wU53n'})
            pr=x.find_all('div',{'class':'_1vC4OE _2rQ-NK'})

            for i in range(0,len(z)):
                if(z[i].text.strip()==r'I Kall K8 NEW (Blue, 16 GB)  (2 GB RAM)'):
                    return render(request,'compare/search.html') 
                    
            #return HttpResponse(z)
    #test = x.find_all('ul', {'class': 'vFw0gD'})
    #print(test[1].text)
            #s=1
            #if search_query in z:
            #    return render(request,'compare/search.html') 


            

            for i in range(len(z)):
        #print(z[i].text, end =" ")
        #print(pr[i].text)
        # print("\n")

                if(z[i].text.strip()==search_query):
                    return HttpResponse(search_query)
                    return render(request,'compare/search.html')
                    break
                else :
                    continue
                    #return HttpResponse("notfound")
                    #break    


            

#crawl(site)
            #return HttpResponse(search_query)
            #return render(request,'compare/search.html')
            

    return render(request,'compare/index.html')
'''
def your_view(request):
   
    # Your code
    #if request.method == 'GET': # If the form is submitted
     #   search_query = request.GET.get('search_box', None)
    #return HttpResponse("hgg")
    return redirect(request,'compare/search.html')
        # Do whatever you need with the word the user looked for

    # Your code    
