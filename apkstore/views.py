import re
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import APKDetails ,APKSubDetails, Category , SubCategory ,ArticleBlog
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
from django.contrib.auth import logout,login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import csv
import unicodedata
from django.db.models import Q
# Create your views here.

def index(request):
    return HttpResponse("working fine")
    if request.method == 'POST':
        apps_name = request.POST['apps_name']
	q = Q()
	q = q & Q(title_name__icontains = apps_name) | Q(category__meta = apps_name)| Q(category__name__icontains = apps_name)
        apkdetails_search = APKDetails.objects.filter(q)
	return render(request,"apkstore/search_table.html",{'apkdetails_search':apkdetails_search})
    #return render(request,"apkstore/search_table.html",{'apkdetails_search':apkdetails_search})

def robots(request):
    apkdetails = APKDetails.objects.filter(id=6)
    return render(request,"apkstore/robots.txt")
def search_apps(request): 
    return HttpResponse("its working")
    apkdetails = APKDetails.objects.filter(id=6)
    return render(request,"apkstore/home_working_time.html",{'apk':apkdetails})

def addapkdetails(request):
    if request.method == 'POST':
        title_name = request.POST['title_name']
	title_shortcode = request.POST['title_shortcode']
        developer = request.POST['developer']
        ratting = request.POST['ratting']
        offer_in_app = request.POST['offer_in_app']
        play_st_down_link = request.POST['play_st_down_link']
        apkpure_down_link = request.POST['apk_down_link']
        apk_version = request.POST['apk_version']
        desc1 = request.POST['desc1']
        fs = FileSystemStorage(location="django_project/media/apkimage")
        desc2 = request.POST['desc2']
        image = request.FILES.get('main_image')
	#return HttpResponse("%s" %image)
	if image:
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
	    #return HttpResponse(filename)
	    url = "apkimage/"+str(filename)
	    image_url = url
	else:
	    image_url = None
        image1 = request.FILES.get('image1')
	if image1:
            filename = fs.save(image1.name, image1)
            uploaded_file_url = fs.url(filename)
	    url = "apkimage/"+str(filename)
	    image1_url = url
	else:
	    image1_url = None
        image2 = request.FILES.get('image2')
	if image2:
            filename = fs.save(image2.name, image2)
            uploaded_file_url = fs.url(filename)
	    url = "apkimage/"+str(filename)
	    image2_url = url
	else:
	    image2_url = None
        image3 = request.FILES.get('image3')
	if image3:
            filename = fs.save(image3.name, image3)
            uploaded_file_url = fs.url(filename)
	    url = "apkimage/"+str(filename)
	    image3_url = url
	else:
	    image3_url = None
        image4 = request.FILES.get('image4')
	if image4:
            filename = fs.save(image4.name, image4)
            uploaded_file_url = fs.url(filename)
	    url = "apkimage/"+str(filename)
	    image4_url = url
	else:
	    image4_url = None
        image5 = request.FILES.get('image5')
	if image5:
            filename = fs.save(image5.name, image5)
            uploaded_file_url = fs.url(filename)
	    url = "apkimage/"+str(filename)
	    image5_url = url
	else:
	    image5_url = None
        app_upload = request.FILES.get('app_upload')
	if app_upload:
            fs_file = FileSystemStorage(location="django_project/media/apkfile")
            filename = fs_new.save(app_upload.name, app_upload)
            uploaded_file_url = fs_new.url(filename)
	    url = "apkfile/"+str(filename)
	    app_upload_url = url
	else:
	    app_upload_url = None
        no_of_install = request.POST['no_of_install']
        req_android_vsn = request.POST['req_android_vsn']
	status = request.POST['status']
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
	if category != "0":
	    category_obj = Category.objects.filter(id=int(category))
	    category_obj = category_obj[0]
        if category == "0":
	    category_obj = None
	if subcategory != "0":
	    subcategory_obj = SubCategory.objects.filter(id=int(subcategory))
	    subcategory_obj = subcategory_obj[0]
	if subcategory == "0":
	    subcategory_obj = None
	APKDetails.objects.create(title_name=title_name,title_shortcode=title_shortcode,devloper=developer,ratting=ratting,offers_in_app=offer_in_app,play_store_download_link=play_st_down_link,apkpure_download_link=apkpure_down_link,apk_version=apk_version,description_1=desc1,description_2=desc2,image=image_url,image1=image1_url,image2=image2_url,image3=image3_url,image4=image4_url,image5=image5_url,app_upload_file=app_upload_url,number_of_install=no_of_install,required_android_version=req_android_vsn,status=status,category=category_obj,subcategory=subcategory_obj)

	return render(request,"apkstore/addapkdetails.html",{'msg':"Successfull Update"})
    

    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    return render(request,"apkstore/addapkdetails.html",{'category':category,'subcategory':subcategory})

def addapksubdetails(request):
    if request.method == 'POST':
        title_name = request.POST['title_name']
       # title_shortcode = request.POST['title_shortcode']
        developer = request.POST['developer']
        ratting = request.POST['ratting']
        offer_in_app = request.POST['offer_in_app']
        play_st_down_link = request.POST['play_st_down_link']
        apkpure_down_link = request.POST['apk_down_link']
        apk_version = request.POST['apk_version']
        desc1 = request.POST['desc1']
        fs = FileSystemStorage(location="django_project/media/apkimage")
        desc2 = request.POST['desc2']
        image = request.FILES.get('main_image')
        #return HttpResponse("%s" %image)
        '''
        if image:
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
            #return HttpResponse(filename)
            url = "apkimage/"+str(filename)
            image_url = url
        else:
            image_url = None
        image1 = request.FILES.get('image1')
        if image1:
            filename = fs.save(image1.name, image1)
            uploaded_file_url = fs.url(filename)
            url = "apkimage/"+str(filename)
            image1_url = url
        else:
            image1_url = None
        image2 = request.FILES.get('image2')
        if image2:
            filename = fs.save(image2.name, image2)
            uploaded_file_url = fs.url(filename)
            url = "apkimage/"+str(filename)
            image2_url = url
        else:
            image2_url = None
        image3 = request.FILES.get('image3')
        if image3:
            filename = fs.save(image3.name, image3)
            uploaded_file_url = fs.url(filename)
            url = "apkimage/"+str(filename)
            image3_url = url
        else:
            image3_url = None
        image4 = request.FILES.get('image4')
        if image4:
            filename = fs.save(image4.name, image4)
            uploaded_file_url = fs.url(filename)
            url = "apkimage/"+str(filename)
            image4_url = url
        else:
            image4_url = None
        image5 = request.FILES.get('image5')
        if image5:
            filename = fs.save(image5.name, image5)
            uploaded_file_url = fs.url(filename)
            url = "apkimage/"+str(filename)
            image5_url = url
        else:
            image5_url = None
	'''
        app_upload = request.FILES.get('app_upload')
        if app_upload:
            fs_new = FileSystemStorage(location="django_project/media/apkfile")
            filename = fs_new.save(app_upload.name, app_upload)
            uploaded_file_url = fs_new.url(filename)
            url = "apkfile/"+str(filename)
            app_upload_url = url
        else:
            app_upload_url = None
        no_of_install = request.POST['no_of_install']
        req_android_vsn = request.POST['req_android_vsn']
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
	apk_details_fk = request.POST.get('apkdetails')
        if category != "0":
            category_obj = Category.objects.filter(id=int(category))
	    category_obj_update = category_obj[0]
        if category == "0":
            category_obj = None
	    category_obj_update = None
        if subcategory != "0":
            subcategory_obj = SubCategory.objects.filter(id=int(subcategory))
	    subcategory_obj_update = subcategory_obj[0]
        if subcategory == "0":
            subcategory_obj = None
	    subcategory_obj_update = None
        if apk_details_fk != "0":
            apk_details_obj = APKDetails.objects.filter(id=int(apk_details_fk))
        else:
	    apk_details_obj = None
            return HttpResponse("Please fill this fileld (required)")

	if apk_details_obj:
	    details_obj = apk_details_obj[0]
            APKSubDetails.objects.create(title_name=details_obj.title_name,devloper=details_obj.devloper,ratting=details_obj.ratting,offers_in_app=details_obj.offers_in_app,play_store_download_link=details_obj.play_store_download_link,apkpure_download_link=details_obj.apkpure_download_link,apk_version=details_obj.apk_version,description_1=details_obj.description_1,description_2=details_obj.description_2,image=details_obj.image,image1=details_obj.image1,image2=details_obj.image2,image3=details_obj.image3,image4=details_obj.image4,image5=details_obj.image5,app_upload_file=details_obj.app_upload_file,number_of_install=details_obj.number_of_install,required_android_version=details_obj.required_android_version,category=details_obj.category,subcategory=details_obj.subcategory,apkdetails=details_obj)
          
            apk_details_id = int(apk_details_fk)
            apkdetils_update(apk_details_id,title_name,developer,ratting,offer_in_app,play_st_down_link,apkpure_down_link,apk_version,desc1,desc2,app_upload_url,no_of_install,req_android_vsn,category_obj_update,subcategory_obj_update)


        return render(request,"apkstore/addapksubdetails.html",{"msg":"Successfull Updated"})


    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    apkdetails = APKDetails.objects.all()
    return render(request,"apkstore/addapksubdetails.html",{'category':category,'subcategory':subcategory,'apkdetails':apkdetails})

def apkdetils_update(apk_details_id,title_name,devloper,ratting,offers_in_app,play_store_download_link,apkpure_download_link,apk_version,description_1,description_2,app_upload_url,number_of_install,required_android_version,category,subcategory):
    apk_details = APKDetails.objects.filter(id=apk_details_id)
    if apk_details:
        apk_details.update(title_name=title_name,devloper=devloper,ratting=ratting,offers_in_app=offers_in_app,play_store_download_link=play_store_download_link,apkpure_download_link=apkpure_download_link,apk_version=apk_version,description_1=description_1,description_2=description_2,app_upload_file=app_upload_url,number_of_install=number_of_install,required_android_version=required_android_version,category=category,subcategory=subcategory)
	return True


def whatsappmessenger(request):
    whatsapp_obj = APKDetails.objects.filter(title_shortcode="whatsapp101")
    if whatsapp_obj:
	whats_sub_obj = whatsapp_obj[0]
	whats_app_sub_obj =  whats_sub_obj.apksubdetails_set.all()

    #file_url = "http://android-apkstore.com.cp-in-7.webhostbox.net/cartoon"
    #return HttpResponseRedirect(file_url)	
    return render(request,"apkstore/whatsappmessenger.html",{'whatsapp_obj':whatsapp_obj,'whatsapp_sub_obj':whats_app_sub_obj})


def previous_version(request):
    if request.method == "GET":
	version_id = request.GET.get('version_id')
	version_obj = APKSubDetails.objects.filter(id = int(version_id))
	return render(request,"apkstore/previous_version.html",{'version_obj':version_obj})

@csrf_exempt
def teamworklogin(request):
    user = request.user
    if request.method == "POST":
	username = request.POST['email']
        password = request.POST['psw']
        newuser = auth.authenticate(username=username, password=password)
        if newuser:
            login(request, newuser)
	if newuser:
	    return render(request,"apkstore/teamworkpanel.html",{'user':user})
	else:
	    return render(request,"apkstore/teamworklogin.html",{"msg":"Email or Password dones not match please try again.."})
    else:
	return render(request,"apkstore/teamworklogin.html")

@login_required(login_url="/teamworklogin/")
@csrf_exempt
def teamworkhome(request):
    return render(request,"apkstore/teamworkpanel.html")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/teamworklogin/")
    #return render(request,"/teamworklogin.html",{"msg":"thanks for visite"})

@login_required(login_url="/teamworklogin/")
@csrf_exempt
def teamworkpanel(request):
    return render(request,"apkstore/teamworkpanel.html",{})
@login_required(login_url="/teamworklogin/")
@csrf_exempt
def addcategory(request):
    if request.method == 'POST':
        name = request.POST['name']
	category_id = request.POST['category_id']
	category_our_name = request.POST['category_our_name']
	category_meta = request.POST['meta']
        name = str(name)
	category_id = str(category_id)
	category_our_name = str(category_our_name)
	category_meta = str(category_meta)
	check = Category.objects.filter(category_id = category_id)
	if check:
	    return render(request,"apkstore/addcategory.html",{"msg":"Already Exist customer id Please try other"})
        Category.objects.create(name=name,category_id=category_id,category_our_name=category_our_name,meta=category_meta)
        return render(request,"apkstore/addcategory.html",{"msg":"successfull saved"})
	pass
    else:
        return render(request,"apkstore/addcategory.html",{})

@login_required(login_url="/teamworklogin/")
@csrf_exempt
def addblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        image_link = request.POST['image_link']
        desc = request.POST['desc']
        meta_desc = request.POST['meta_desc']
        meta_keyword = request.POST['meta_key_desc']

        title = str(title)
        image_link = str(image_link)
        desc = str(desc)
	desc1 = ''
	desc2 = ''
	if len(desc)>2000:
	    desc1 = desc[:1999]
	    desc2 = desc[2000:3999]
	else:
	    desc1 = desc

        meta_desc = str(meta_desc)
	meta_keyword = str(meta_keyword)
        ArticalBlog.objects.create(title=title,image_link=image_link,description_1 = desc1,description_2 = desc2,meta_desc=meta_desc,meta_keyword = meta_keyword)
        return render(request,"apkstore/addblog.html",{"msg":"successfull saved"})
        pass
    else:
        return render(request,"apkstore/addblog.html",{})

@login_required(login_url="/teamworklogin/")
@csrf_exempt
def addblog_bulk(request):
    if request.FILES:
	upload_file = request.FILES['upload_file']
        file_contents = csv.reader(upload_file)
	row_check = 1
        if file_contents :
            i = 0
            row_count = 1
            for val in file_contents:
                if i == 0:
                    i = i + 1
                    continue
		short_code = val[0]
                short_code = unicode(short_code, "ISO-8859-1")#order_number
                short_code = unicodedata.normalize('NFKD', short_code).encode('ascii','ignore')

                title = val[1]
                title = unicode(title, "ISO-8859-1")#order_number
                title = unicodedata.normalize('NFKD', title).encode('ascii','ignore')

                image_link = val[2]
                image_link = unicode(image_link, "ISO-8859-1")#order_number
                image_link = unicodedata.normalize('NFKD', image_link).encode('ascii','ignore')

                desc = val[3]
                desc = unicode(desc, "ISO-8859-1")#order_number
                desc = unicodedata.normalize('NFKD', desc).encode('ascii','ignore')

                meta_desc = val[4]
                meta_desc = unicode(meta_desc, "ISO-8859-1")#order_number
                meta_desc = unicodedata.normalize('NFKD', meta_desc).encode('ascii','ignore')

                meta_keyword = val[5]
                meta_keyword = unicode(meta_keyword, "ISO-8859-1")#order_number
                meta_keyword = unicodedata.normalize('NFKD',meta_keyword).encode('ascii','ignore')

		page_title = val[6]
                page_title = unicode(page_title, "ISO-8859-1")#order_number
                page_title = unicodedata.normalize('NFKD',page_title).encode('ascii','ignore')

		blog_url = val[7]
                blog_url = unicode(blog_url, "ISO-8859-1")#order_number
                blog_url = unicodedata.normalize('NFKD',blog_url).encode('ascii','ignore')

		short_code = str(short_code)
		if ArticleBlog.objects.filter(short_code=short_code):
		    error_msg = "Code : "+short_code + "Already Exist in row"+row_check
		    return render(request,"apkstore/addblog_bulk.html",{"msg":error_msg})

       	        title = str(title)
        	image_link = str(image_link)
        	desc = str(desc)
        	meta_desc = str(meta_desc)
        	meta_keyword = str(meta_keyword)
        	desc1 = ''
        	desc2 = ''
		page_title = str(page_title)
		blog_url = str(blog_url)
		if len(desc)<=190:
		    desc_short = desc[185]
        	elif len(desc)>2000:
		    desc_short = desc[:185]
            	    desc1 = desc[185:2150]
            	    desc2 = desc[2150:]
        	else:
                    pass
		article = ArticleBlog.objects.latest('id')
		div_id = str(article.div_id)
		size_div = len(div_id)
		div_id = div_id[size_div-1]
		next_div_id = "ts" + str(int(div_id+1))
		#return HttpResponse(image_link)
		row_check = row_check + 1
        	ArticleBlog.objects.create(short_code=short_code,title=title,image_link=image_link,description_1 = desc1,description_2 = desc2,desc_short=desc_short,meta_desc=meta_desc,meta_keyword = meta_keyword,page_title=page_title,blog_url=blog_url,div_id=next_div_id)
            return render(request,"apkstore/addblog_bulk.html",{"msg":"successfull saved"})
    else:
        return render(request,"apkstore/addblog_bulk.html",{})

@login_required(login_url="/teamworklogin/")
@csrf_exempt
def addcategory_bulk(request):
    if request.FILES:
        upload_file = request.FILES['upload_file']
        file_contents = csv.reader(upload_file)
        if file_contents :
            i = 0
            row_count = 1
            for val in file_contents:
                if i == 0:
                    i = i + 1
                    continue
                name = val[1]
                name = unicode(name, "ISO-8859-1")#order_number
                name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')

                category_id = val[0]
                category_id = unicode(category_id, "ISO-8859-1")#order_number
                category_id = unicodedata.normalize('NFKD', category_id).encode('ascii','ignore')

                category_our_name = val[2]
                category_our_name = unicode(category_our_name, "ISO-8859-1")#order_number
                category_our_name = unicodedata.normalize('NFKD', category_our_name).encode('ascii','ignore')

                category_meta = val[3]
                category_meta = unicode(category_meta, "ISO-8859-1")#order_number
                category_meta = unicodedata.normalize('NFKD', category_meta).encode('ascii','ignore')
                
                if name:
                    name = str(name)
                else:
            	    name = None
                if category_id:
                    category_id = str(category_id)
                else:
            	    category_id = None
                if category_our_name:
                    category_our_name = str(category_our_name)
                else:
            	    category_our_name = None
                if category_meta:
                    category_meta = str(category_meta)
                else:
            	    category_meta = None
          	if category_id == None:
                    return render(request,"apkstore/addcategory_bulk.html",{"msg":"Category id is empty please fill"})

                check = Category.objects.filter(category_id = category_id)
                if check:
                    return render(request,"apkstore/addcategory_bulk.html",{"msg":"Already Exist customer id Please try other"})
                Category.objects.create(name=name,category_id=category_id,category_our_name=category_our_name,meta=category_meta)
            return render(request,"apkstore/addcategory_bulk.html",{"msg":"successfull saved"})
	else:
	    return render(request,"apkstore/addcategory_bulk.html",{'msg':"File Empty"})
    else:
        return render(request,"apkstore/addcategory_bulk.html",{})

@login_required(login_url="/teamworklogin/")
@csrf_exempt
def addsubcategory(request):
    if request.method == 'POST':
	name = request.POST['name']
	subcategory_id = request.POST['subcategory_id']
	subcategory_our_name = request.POST['subcategory_our_name']
	meta = request.POST['meta']
	name = str(name)
	subcategory_id = str(subcategory_id)
	subcategory_our_name = str(subcategory_our_name)
	meta = str(meta)
	SubCategory.objects.create(name=name,category_id=subcategory_id,category_our_name=subcategory_our_name,meta=meta)
	return render(request,"apkstore/addsubcategory.html",{"msg":"successfull saved"})
    else:
        return render(request,"apkstore/addsubcategory.html",{})
@csrf_exempt
def userregister(request):
    if request.method == "POST":
	email = request.POST['email']
	password = request.POST['password']
        if isValidEmail(email) == False:
	    return HttpResponse("Invailid Email")
	email_match = User.objects.filter(email=email)
	if email_match:
	    return HttpResponse("Already Exist Please try other")
	user = User.objects.create(username=email,email=email)
	user.set_password(password)
	user.save()
	return HttpResponse("Successfully Registerd")

 
def isValidEmail(email):
	if len(email) > 7:
		if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) != None:
			return True
	return False 
    
def check_reting(value):
    reting = value
    splt = str(reting)
    x = list(splt)
    if "." in x:
        new_split = splt.split(".")
        n1 = new_split[0]
        n2 = new_split[1]
        if n2 < 5:
            ret_after = "less_reting"
        elif n2 > 5:
            ret_after = "more_retting"
        else:
            ret_after = "avg"
        ret_before = int(n1)
	return [ret_before , ret_after]
    else:
        return [value]
 
def main_show(request):
    whatsapp_obj = APKDetails.objects.filter(title_shortcode="hotstar111")
    if whatsapp_obj:
        whats_sub_obj = whatsapp_obj[0]
        whats_app_sub_obj =  whats_sub_obj.apksubdetails_set.all()
	reting =check_reting(whats_sub_obj.ratting)
        if len(reting)>1:
	    ret_before = int(reting[0])
	    ret_after = reting[1]
        else:
	    ret_before = int(reting[0])
    #file_url = "http://android-apkstore.com.cp-in-7.webhostbox.net/cartoon"
    #return HttpResponseRedirect(file_url)      
    return render(request,"apkstore/adp1.html",{'whatsapp_obj':whatsapp_obj,'whatsapp_sub_obj':whats_app_sub_obj,"ret_before":ret_before,"ret_after":ret_after})

def main_show_new(request):
    get_article_id = request.GET.get('get_id')
    get_article_id = ArticleBlog.objects.filter(blog_url=get_article_id)
    apkdetails_apps = APKDetails.objects.filter(category__meta = "Apps")[:12]
    apkdetails_apps_1 = APKDetails.objects.filter(category__meta = "Apps")[:4]
    apkdetails_apps_2 = APKDetails.objects.filter(category__meta = "Apps")[4:8]
    apkdetails_apps_3 = APKDetails.objects.filter(category__meta = "Apps")[8:12]
    apkdetails_games = APKDetails.objects.filter(category__meta = "Games")[:12]
    if apkdetails_apps:
        whats_sub_obj = apkdetails_apps[0]
        whats_app_sub_obj =  whats_sub_obj.apksubdetails_set.all()
        reting =check_reting(whats_sub_obj.ratting)
        if len(reting)>1:
            ret_before = int(reting[0])
            ret_after = reting[1]
        else:
            ret_before = int(reting[0])
    #file_url = "http://android-apkstore.com.cp-in-7.webhostbox.net/cartoon"
    #return HttpResponseRedirect(file_url)      
    return render(request,"apkstore/adp2.html",{'apkdetails_games':apkdetails_games,'apkdetails_apps':apkdetails_apps,'apkdetails_apps_1':apkdetails_apps_1,'apkdetails_apps_2':apkdetails_apps_2,'apkdetails_apps_3':apkdetails_apps_3 , "ret_before":ret_before,"ret_after":ret_after , 'get_article_id':get_article_id})

def alp_new_apps(request):
    apkdetails_apps = APKDetails.objects.filter(category__meta = "Apps")[:12]
    apkdetails_apps_1 = APKDetails.objects.filter(category__meta = "Apps")[:4]
    apkdetails_apps_2 = APKDetails.objects.filter(category__meta = "Apps")[4:8]
    apkdetails_apps_3 = APKDetails.objects.filter(category__meta = "Apps")[8:12]
    apkdetails_games = APKDetails.objects.filter(category__meta = "Games")[:12]
    apkdetails = APKDetails.objects.filter(category__meta = "Apps").exclude(id__in=[1,2,3,4,5,6,8])
    if apkdetails_apps:
        whats_sub_obj = apkdetails_apps[0]
        whats_app_sub_obj =  whats_sub_obj.apksubdetails_set.all()
        reting =check_reting(whats_sub_obj.ratting)
        if len(reting)>1:
            ret_before = int(reting[0])
            ret_after = reting[1]
        else:
            ret_before = int(reting[0])
    #file_url = "http://android-apkstore.com.cp-in-7.webhostbox.net/cartoon"
    #return HttpResponseRedirect(file_url)      
    return render(request,"apkstore/alp1_new_apps.html",{'apkdetails':apkdetails,'apkdetails_games':apkdetails_games,'apkdetails_apps':apkdetails_apps,'apkdetails_apps_1':apkdetails_apps_1,'apkdetails_apps_2':apkdetails_apps_2,'apkdetails_apps_3':apkdetails_apps_3 , "ret_before":ret_before,"ret_after":ret_after})

def alp_new_games(request):
    apkdetails_apps = APKDetails.objects.filter(category__meta = "Apps")[:12]
    apkdetails_apps_1 = APKDetails.objects.filter(category__meta = "Apps")[:4]
    apkdetails_apps_2 = APKDetails.objects.filter(category__meta = "Apps")[4:8]
    apkdetails_apps_3 = APKDetails.objects.filter(category__meta = "Apps")[8:12]
    apkdetails_games = APKDetails.objects.filter(category__meta = "Games")[:12]
    apkdetails = APKDetails.objects.filter(category__meta = "Games").exclude(id__in=[1,2,3,4,5,6,8])
    if apkdetails_apps:
        whats_sub_obj = apkdetails_apps[0]
        whats_app_sub_obj =  whats_sub_obj.apksubdetails_set.all()
        reting =check_reting(whats_sub_obj.ratting)
        if len(reting)>1:
            ret_before = int(reting[0])
            ret_after = reting[1]
        else:
            ret_before = int(reting[0])
    #file_url = "http://android-apkstore.com.cp-in-7.webhostbox.net/cartoon"
    #return HttpResponseRedirect(file_url)      
    return render(request,"apkstore/alp1_new_games.html",{'apkdetails':apkdetails,'apkdetails_games':apkdetails_games,'apkdetails_apps':apkdetails_apps,'apkdetails_apps_1':apkdetails_apps_1,'apkdetails_apps_2':apkdetails_apps_2,'apkdetails_apps_3':apkdetails_apps_3 , "ret_before":ret_before,"ret_after":ret_after})


def alp2_blog(request):
    apkdetails_apps = APKDetails.objects.filter(category__meta = "Apps")[:12]
    apkdetails_apps_1 = APKDetails.objects.filter(category__meta = "Apps")[:4]
    apkdetails_apps_2 = APKDetails.objects.filter(category__meta = "Apps")[4:8]
    apkdetails_apps_3 = APKDetails.objects.filter(category__meta = "Apps")[8:12]
    apkdetails_games = APKDetails.objects.filter(category__meta = "Games")[:12]
    article = ArticleBlog.objects.all().exclude(status=0)
    if apkdetails_apps:
        whats_sub_obj = apkdetails_apps[0]
        whats_app_sub_obj =  whats_sub_obj.apksubdetails_set.all()
        reting =check_reting(whats_sub_obj.ratting)
        if len(reting)>1:
            ret_before = int(reting[0])
            ret_after = reting[1]
        else:
            ret_before = int(reting[0])
    return render(request,"apkstore/alp2.html",{'apkdetails_games':apkdetails_games,'apkdetails_apps':apkdetails_apps,'apkdetails_apps_1':apkdetails_apps_1,'apkdetails_apps_2':apkdetails_apps_2,'apkdetails_apps_3':apkdetails_apps_3 , "ret_before":ret_before,"ret_after":ret_after,'article':article})


def main_page(request):
    apkdetails_action = APKDetails.objects.filter(category__name__icontains = "action")
    apkdetails_arcade = APKDetails.objects.filter(category__name__icontains = "Arcade")
    apkdetails_adventure = APKDetails.objects.filter(category__name__icontains = "Adventure")
    apkdetails_board = APKDetails.objects.filter(category__name__icontains = "Board")
    apkdetails_card = APKDetails.objects.filter(category__name__icontains = "Card")
    apkdetails_casino = APKDetails.objects.filter(category__name__icontains = "Casino")
    apkdetails_Casual = APKDetails.objects.filter(category__name__icontains = "Casual")
    apkdetails_educational = APKDetails.objects.filter(category__name__icontains = "Educational")
    apkdetails_music = APKDetails.objects.filter(category__name__icontains = "Music")
    apkdetails_puzzle = APKDetails.objects.filter(category__name__icontains = "Puzzle")
    apkdetails_racing = APKDetails.objects.filter(category__name__icontains = "Racing")
    apkdetails_role_playing = APKDetails.objects.filter(category__name__icontains = "Role Playing")
    apkdetails_simulation = APKDetails.objects.filter(category__name__icontains = "Simulation")
    apkdetails_sports = APKDetails.objects.filter(category__name__icontains = "Sports")
    apkdetails_strategy = APKDetails.objects.filter(category__name__icontains = "Strategy")
    apkdetails_trivia = APKDetails.objects.filter(category__name__icontains = "Trivia")
    apkdetails_word = APKDetails.objects.filter(category__name__icontains = "Word")
    apkdetails_daydream = APKDetails.objects.filter(category__name__icontains = "Daydream")
    apkdetails_art_and_design = APKDetails.objects.filter(category__name__icontains = "Art & Design")
    apkdetails_auto_vehicles = APKDetails.objects.filter(category__name__icontains = "Auto & Vehicles")
    apkdetails_beauty = APKDetails.objects.filter(category__name__icontains = "Beauty")
    apkdetails_books_reference = APKDetails.objects.filter(category__name__icontains = "Books & Reference")
    apkdetails_business = APKDetails.objects.filter(category__name__icontains = "Business")
    apkdetails_comics = APKDetails.objects.filter(category__name__icontains = "Comics")
    apkdetails_communication = APKDetails.objects.filter(category__name__icontains = "Communication")
    apkdetails_dating = APKDetails.objects.filter(category__name__icontains = "Dating")
    apkdetails_education = APKDetails.objects.filter(category__name__icontains = "Education")
    apkdetails_entertainment = APKDetails.objects.filter(category__name__icontains = "Entertainment")
    apkdetails_event = APKDetails.objects.filter(category__name__icontains = "Event")
    apkdetails_finance = APKDetails.objects.filter(category__name__icontains = "Finance")
    apkdetails_food_and_drink = APKDetails.objects.filter(category__name__icontains = "Food & Drink")
    apkdetails_health_and_fitness = APKDetails.objects.filter(category__name__icontains = "Health & Fitness")
    apkdetails_house_and_home = APKDetails.objects.filter(category__name__icontains = "House & Home")
    apkdetails_libraries_and_demo = APKDetails.objects.filter(category__name__icontains = "Libraries & Demo")
    apkdetails_lifestyle = APKDetails.objects.filter(category__name__icontains = "Lifestyle")
    apkdetails_maps_and_navigation = APKDetails.objects.filter(category__name__icontains = "Maps & Navigation")
    apkdetails_medical = APKDetails.objects.filter(category__name__icontains = "Medical")
    apkdetails_music_and_audio = APKDetails.objects.filter(category__name__icontains = "Music & Audio")
    apkdetails_news_and_magazines = APKDetails.objects.filter(category__name__icontains = "News & Magazines")
    apkdetails_parenting = APKDetails.objects.filter(category__name__icontains = "Parenting")
    apkdetails_personalization = APKDetails.objects.filter(category__name__icontains = "Personalization")
    apkdetails_photography = APKDetails.objects.filter(category__name__icontains = "Photography")
    apkdetails_productivity = APKDetails.objects.filter(category__name__icontains = "Productivity")
    apkdetails_shopping = APKDetails.objects.filter(category__name__icontains = "Shopping")
    apkdetails_social = APKDetails.objects.filter(category__name__icontains = "Social")
    apkdetails_sports = APKDetails.objects.filter(category__name__icontains = "Sports")
    apkdetails_tools = APKDetails.objects.filter(category__name__icontains = "Tools")
    apkdetails_travel_and_local = APKDetails.objects.filter(category__name__icontains = "Travel & Local")
    apkdetails_videoplayers_and_editors = APKDetails.objects.filter(category__name__icontains = "Video Players & Editors")
    apkdetails_weather = APKDetails.objects.filter(category__name__icontains = "Weather")
    apkdetails_wear_os_by_google = APKDetails.objects.filter(category__name__icontains = "Wear OS by Google")

    apkdetails_games = APKDetails.objects.filter(category__meta = "Games")[:12]
    apkdetails_games_2 = APKDetails.objects.filter(category__meta = "Games")[12:18]
    apkdetails_games_3 = APKDetails.objects.filter(category__meta = "Games")[18:24]
    apkdetails_games_4 = APKDetails.objects.filter(category__meta = "Games")[24:30]
    apkdetails_games_5 = APKDetails.objects.filter(category__meta = "Games")[30:36]
    apkdetails_games_6 = APKDetails.objects.filter(category__meta = "Games")[36:42]
    apkdetails_apps = APKDetails.objects.filter(category__meta = "Apps")[:12]
    apkdetails_apps_2 = APKDetails.objects.filter(category__meta = "Apps")[12:18]
    apkdetails_apps_3 = APKDetails.objects.filter(category__meta = "Apps")[18:24]
    apkdetails_apps_4 = APKDetails.objects.filter(category__meta = "Apps")[24:30]
    apkdetails_apps_5 = APKDetails.objects.filter(category__meta = "Apps")[30:36]
    if apkdetails_action:
        apkdetails_obj = apkdetails_action[0]
        reting =check_reting(apkdetails_obj.ratting)
        if len(reting)>1:
            ret_before = int(reting[0])
            ret_after = reting[1]
        else:
            ret_before = int(reting[0])
    #file_url = "http://android-apkstore.com.cp-in-7.webhostbox.net/cartoon"
    #return HttpResponseRedirect(file_url)
    article = ArticleBlog.objects.all().exclude(status=0)      
    return render(request,"apkstore/home.html",{'apkdetails_games':apkdetails_games,'apkdetails_apps':apkdetails_apps,'apkdetails_games_2':apkdetails_games_2,'apkdetails_games_3':apkdetails_games_3,'apkdetails_games_4':apkdetails_games_4,'apkdetails_games_5':apkdetails_games_5,'apkdetails_games_6':apkdetails_games_6,'apkdetails_apps_2':apkdetails_apps_2,'apkdetails_apps_3':apkdetails_apps_3,'apkdetails_apps_4':apkdetails_apps_4,'apkdetails_apps_5':apkdetails_apps_5,"ret_before":ret_before,"ret_after":ret_after , 'article':article})


def home(request):
    return render(request,"apkstore/home.html")


def softdata_upload(request):
    if request.FILES:
        upload_file = request.FILES['upload_file']
        file_contents = csv.reader(upload_file)
        if file_contents :
	    i = 0
	    row_count = 1 
            for val in file_contents:
		if i == 0:
		    i = i + 1
		    continue
	        app_id = val[0]
                app_id = unicode(app_id, "ISO-8859-1")#order_number
                app_id = unicodedata.normalize('NFKD', app_id).encode('ascii','ignore')

                short_key = val[1]
                short_key = unicode(short_key, "ISO-8859-1")#order_number
                short_key = unicodedata.normalize('NFKD', short_key).encode('ascii','ignore')

                title_name = val[2]
                title_name = unicode(title_name, "ISO-8859-1")#order_number
                title_name = unicodedata.normalize('NFKD', title_name).encode('ascii','ignore')

                app_url = val[3]
                app_url = unicode(app_url, "ISO-8859-1")#order_number
                app_url = unicodedata.normalize('NFKD', app_url).encode('ascii','ignore')

                updated_on = val[4]
                updated_on = unicode(updated_on, "ISO-8859-1")#order_number
                updated_on = unicodedata.normalize('NFKD', updated_on).encode('ascii','ignore')

                category = val[5]
                category = unicode(category, "ISO-8859-1")#order_number
                category = unicodedata.normalize('NFKD', category).encode('ascii','ignore')

                sub_category = val[6]
                sub_category = unicode(short_key, "ISO-8859-1")#order_number
                sub_category = unicodedata.normalize('NFKD', sub_category).encode('ascii','ignore')

                size = val[7]
                size = unicode(size, "ISO-8859-1")#order_number
                size = unicodedata.normalize('NFKD', size).encode('ascii','ignore')

                developer = val[8]
                developer = unicode(developer, "ISO-8859-1")#order_number
                developer = unicodedata.normalize('NFKD', developer).encode('ascii','ignore')

                required_android = val[9]
                required_android = unicode(required_android, "ISO-8859-1")#order_number
                required_android = unicodedata.normalize('NFKD', required_android).encode('ascii','ignore')

                current_version = val[10]
                current_version = unicode(current_version, "ISO-8859-1")#order_number
                current_version = unicodedata.normalize('NFKD', current_version).encode('ascii','ignore')

                desc = val[11]
                desc = unicode(desc, "ISO-8859-1")#order_number
                desc = unicodedata.normalize('NFKD', desc).encode('ascii','ignore')

                rating = val[12]
                rating = unicode(rating, "ISO-8859-1")#order_number
                rating = unicodedata.normalize('NFKD', rating).encode('ascii','ignore')

                img_src_1 = val[13]
                img_src_1 = unicode(img_src_1, "ISO-8859-1")#order_number
                img_src_1 = unicodedata.normalize('NFKD', img_src_1).encode('ascii','ignore')

                img_src_2 = val[14]
                img_src_2 = unicode(img_src_2, "ISO-8859-1")#order_number
                img_src_2 = unicodedata.normalize('NFKD', img_src_2).encode('ascii','ignore')

                img_src_3 = val[15]
                img_src_3 = unicode(img_src_3, "ISO-8859-1")#order_number
                img_src_3 = unicodedata.normalize('NFKD', img_src_3).encode('ascii','ignore')

                img_src_4 = val[16]
                img_src_4 = unicode(img_src_4, "ISO-8859-1")#order_number
                img_src_4 = unicodedata.normalize('NFKD', img_src_4).encode('ascii','ignore')

                img_src_5 = val[17]
                img_src_5 = unicode(img_src_5, "ISO-8859-1")#order_number
                img_src_5 = unicodedata.normalize('NFKD', img_src_5).encode('ascii','ignore')

                img_src_6 = val[18]
                img_src_6 = unicode(img_src_6, "ISO-8859-1")#order_number
                img_src_6 = unicodedata.normalize('NFKD', img_src_6).encode('ascii','ignore')


                page_title = val[19]
                page_title = unicode(page_title, "ISO-8859-1")#order_number
                page_title = unicodedata.normalize('NFKD', page_title).encode('ascii','ignore')

                meta_keyword = val[20]
                meta_keyword = unicode(meta_keyword, "ISO-8859-1")#order_number
                meta_keyword = unicodedata.normalize('NFKD', meta_keyword).encode('ascii','ignore')

                meta_description = val[21]
                meta_description = unicode(meta_description, "ISO-8859-1")#order_number
                meta_description = unicodedata.normalize('NFKD', meta_description).encode('ascii','ignore')

                app_url_show = val[22]
                app_url_show = unicode(app_url_show, "ISO-8859-1")#order_number
                app_url_show = unicodedata.normalize('NFKD', app_url_show).encode('ascii','ignore')


		if app_id:
		    app_id = str(app_id)
		else:
		    app_id = None

		if app_id == None:
		    msg = "Please fill App Id in row " + row_count
		    return render(request,"apkstore/softdata_upload.html",{'msg':msg})

		check_app_id = APKDetails.objects.filter(app_id=app_id)
		if check_app_id:
		    msg = "Already Exist " + app_id + "in Row no " + row_count
		    return render(request,"apkstore/softdata_upload.html",{'msg':msg})

		if short_key:
		    short_key = str(short_key)
		else:
		    short_key = None

		if short_key == None:
                    msg = "Please fill short key in row " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})

                check_short_key = APKDetails.objects.filter(title_shortcode=short_key)
                if check_short_key:
                    msg = "Already Exist " + short_key + "in Row no " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})


		if title_name:
		   title_name = str(title_name)
		else:
		    title_name = None

                if app_url:
		    apk_url = str(app_url)
		else:
		    apk_url = None

		if updated_on:
		    updated_on = str(updated_on)
		else:
		    updatd_on = None

		if category:
		    category = str(category)
		else:
		    category = None

		if sub_category:
		    sub_category = str(sub_category)
		else:
		    sub_category = None

		if size:
		    size = str(size)
		else:
		    size = None

		if developer:
		    developer = str(developer)
		else:
		    developer = None

		if required_android:
		    required_version = (required_android)
		else:
		    required_version = None

		if current_version:
		    current_version = (current_version)
		else:
		    current_version = None

		if page_title:
		    page_title = str(page_title)
		else:
		    page_title = None

		if meta_keyword:
		    meta_keyword = str(meta_keyword)
		else:
		    meta_keyword = None

		if meta_description:
		    meta_description = str(meta_description)
		else:
		    meta_description = None 
		
		if app_url_show:
	            app_url_show = str(app_url_show)
		else:
		    app_url_show = None

		desc1 = ""
		desc2 = ""
		desc3 = ""
		desc4 = ""

		if desc:
		    desc = str(desc)
		    if len(desc)>999:
		        desc1 = desc[:999]
		    if len(desc)>1999:
		        desc2 = desc[999:1999]
		    if len(desc)>2999:
			desc3 = desc[1999:2999]
		    if len(desc4)>3999:
			desc4 = desc[3999:]
		else:
		    desc = None

		if rating:
		    rating = float(rating)
		else:
		    rating = None

		if img_src_1:
		    img_src_1 = str(img_src_1)
		else:
		    img_src_1 = None

		if img_src_2:
		    img_src_2 = str(img_src_2)
		else:
		    img_src_2 = None

                if img_src_3:
		    img_src_3 = str(img_src_3)
		else:
		    img_src_3 = None

                if img_src_4:
		    img_src_4 = str(img_src_4)
		else:
		    img_src_4 = None

                if img_src_5:
		    img_src_5 = str(img_src_5)
		else:
		    img_src_5 = None

                if img_src_6:
                    img_src_6 = str(img_src_6)
                else:
                    img_src_6 = None


		#return HttpResponse(updated_on)
		category_obj = Category.objects.filter(name=category)
		if not category_obj:
		    msg = "Category not match please check and try again  " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})
		else:
		    category_obj = category_obj[0]
		subcategory_obj = SubCategory.objects.latest('id')
		subcategory_obj = None


		APKDetails.objects.create(app_id=app_id,title_name=title_name,title_shortcode=short_key,devloper=developer,ratting=rating,required_version=required_version,current_version=current_version,description_1=desc1,description_2=desc2,description_3=desc3,description_4=desc4,img_url_1=img_src_1,img_url_2=img_src_2,img_url_3=img_src_3,img_url_4=img_src_4,img_url_5=img_src_5,img_url_6=img_src_6,apk_url=apk_url,size=size,updated_on=updated_on,app_url_show=app_url_show,page_title=page_title,meta_keyword=meta_keyword,meta_description=meta_description,category=category_obj,subcategory=subcategory_obj)

        return render(request,"apkstore/softdata_upload.html",{'msg':"Successfull Uploaded"})



    return render(request,"apkstore/softdata_upload.html")


def prev_version_softdata_upload(request):
    if request.FILES:
        upload_file = request.FILES['upload_file']
        file_contents = csv.reader(upload_file)
        if file_contents :
            i = 0
            row_count = 1
            for val in file_contents:
                if i == 0:
                    i = i + 1
                    continue
                app_id = val[0]
                app_id = unicode(app_id, "ISO-8859-1")#order_number
                app_id = unicodedata.normalize('NFKD', app_id).encode('ascii','ignore')

                short_key = val[1]
                short_key = unicode(short_key, "ISO-8859-1")#order_number
                short_key = unicodedata.normalize('NFKD', short_key).encode('ascii','ignore')

                title_name = val[2]
                title_name = unicode(title_name, "ISO-8859-1")#order_number
                title_name = unicodedata.normalize('NFKD', title_name).encode('ascii','ignore')

                app_url = val[3]
                app_url = unicode(app_url, "ISO-8859-1")#order_number
                app_url = unicodedata.normalize('NFKD', app_url).encode('ascii','ignore')

                updated_on = val[4]
                updated_on = unicode(updated_on, "ISO-8859-1")#order_number
                updated_on = unicodedata.normalize('NFKD', updated_on).encode('ascii','ignore')

                category = val[5]
                category = unicode(category, "ISO-8859-1")#order_number
                category = unicodedata.normalize('NFKD', category).encode('ascii','ignore')

                sub_category = val[6]
                sub_category = unicode(short_key, "ISO-8859-1")#order_number
                sub_category = unicodedata.normalize('NFKD', sub_category).encode('ascii','ignore')

                size = val[7]
                size = unicode(size, "ISO-8859-1")#order_number
                size = unicodedata.normalize('NFKD', size).encode('ascii','ignore')
                developer = val[8]
                developer = unicode(developer, "ISO-8859-1")#order_number
                developer = unicodedata.normalize('NFKD', developer).encode('ascii','ignore')

                required_android = val[9]
                required_android = unicode(required_android, "ISO-8859-1")#order_number
                required_android = unicodedata.normalize('NFKD', required_android).encode('ascii','ignore')

                current_version = val[10]
                current_version = unicode(current_version, "ISO-8859-1")#order_number
                current_version = unicodedata.normalize('NFKD', current_version).encode('ascii','ignore')

                desc = val[11]
                desc = unicode(desc, "ISO-8859-1")#order_number
                desc = unicodedata.normalize('NFKD', desc).encode('ascii','ignore')

                rating = val[12]
                rating = unicode(rating, "ISO-8859-1")#order_number
                rating = unicodedata.normalize('NFKD', rating).encode('ascii','ignore')

                img_src_1 = val[13]
                img_src_1 = unicode(img_src_1, "ISO-8859-1")#order_number
                img_src_1 = unicodedata.normalize('NFKD', img_src_1).encode('ascii','ignore')

                img_src_2 = val[14]
                img_src_2 = unicode(img_src_2, "ISO-8859-1")#order_number
                img_src_2 = unicodedata.normalize('NFKD', img_src_2).encode('ascii','ignore')

                img_src_3 = val[15]
                img_src_3 = unicode(img_src_3, "ISO-8859-1")#order_number
                img_src_3 = unicodedata.normalize('NFKD', img_src_3).encode('ascii','ignore')

                img_src_4 = val[16]
                img_src_4 = unicode(img_src_4, "ISO-8859-1")#order_number
                img_src_4 = unicodedata.normalize('NFKD', img_src_4).encode('ascii','ignore')

                img_src_5 = val[17]
                img_src_5 = unicode(img_src_5, "ISO-8859-1")#order_number
                img_src_5 = unicodedata.normalize('NFKD', img_src_5).encode('ascii','ignore')
                page_title = val[18]
                page_title = unicode(page_title, "ISO-8859-1")#order_number
                page_title = unicodedata.normalize('NFKD', page_title).encode('ascii','ignore')

                meta_keyword = val[19]
                meta_keyword = unicode(meta_keyword, "ISO-8859-1")#order_number
                meta_keyword = unicodedata.normalize('NFKD', meta_keyword).encode('ascii','ignore')

                meta_description = val[20]
                meta_description = unicode(meta_description, "ISO-8859-1")#order_number
                meta_description = unicodedata.normalize('NFKD', meta_description).encode('ascii','ignore')

                if app_id:
                    app_id = str(app_id)
                else:
                    app_id = None

                if app_id == None:
                    msg = "Please fill App Id in row " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})

                check_app_id = APKDetails.objects.filter(app_id=app_id)
                if check_app_id:
                    msg = "Already Exist " + app_id + "in Row no " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})

                if short_key:
                    short_key = str(short_key)
                else:
                    short_key = None

		if short_key == None:
                    msg = "Please fill short key in row " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})

		check_short_key = APKDetails.objects.filter(title_shortcode=short_key)
	        if check_short_key:
		    msg = "Already Exist " + short_key + "in Row no " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})
                if title_name:
                   title_name = str(title_name)
                else:
                    title_name = None

                if app_url:
                    apk_url = str(app_url)
                else:
                    apk_url = None
                if updated_on:
                    updated_on = str(updated_on)
                else:
                    updatd_on = None

                if category:
                    category = str(category)
                else:
                    category = None

                if sub_category:
                    sub_category = str(sub_category)
                else:
                    sub_category = None

                if size:
                    size = str(size)
                else:
                    size = None

                if developer:
                    developer = str(developer)
                else:
                    developer = None

                if required_android:
                    required_version = (required_android)
                else:
                    required_version = None

                if current_version:
                    current_version = (current_version)
                else:
                    current_version = None

                if page_title:
                    page_title = str(page_title)
                else:
                    page_title = None

                if meta_keyword:
                    meta_keyword = str(meta_keyword)
                else:
                    meta_keyword = None
                if meta_description:
                    meta_description = str(meta_description)
                else:
                   meta_description = None

                desc1 = ""
                desc2 = ""
                desc3 = ""
                desc4 = ""

                if desc:
                    desc = str(desc)
                    if len(desc)>999:
                        desc1 = desc[:999]
                    if len(desc)>1999:
                        desc2 = desc[999:1999]
                    if len(desc)>2999:
                        desc3 = desc[1999:2999]
                    if len(desc4)>3999:
                        desc4 = desc[3999:]
                else:
                    desc = None

                if rating:
                    rating = float(rating)
                else:
                    rating = None

                if img_src_1:
                    img_src_1 = str(img_src_1)
                else:
                    img_src_1 = None

                if img_src_2:
                    img_src_2 = str(img_src_2)
                else:
                    img_src_2 = None

                if img_src_3:
                    img_src_3 = str(img_src_3)
                else:
                    img_src_3 = None
                if img_src_4:
                    img_src_4 = str(img_src_4)
                else:
                    img_src_4 = None

                if img_src_5:
                    img_src_5 = str(img_src_5)
                else:
                    img_src_5 = None

                #return HttpResponse(updated_on)
                category_obj = Category.objects.latest('id')
                subcategory_obj = SubCategory.objects.latest('id')


                APKDetails.objects.create(app_id=app_id,title_name=title_name,title_shortcode=short_key,devloper=developer,ratting=rating,required_version=required_version,current_version=current_version,description_1=desc1,description_2=desc2,description_3=desc3,description_4=desc4,img_url_1=img_src_1,img_url_2=img_src_2,img_url_3=img_src_3,img_url_4=img_src_4,img_url_5=img_src_5,apk_url=apk_url,size=size,updated_on=updated_oni,page_title=page_title,meta_keyword=meta_keyword,meta_description=meta_description,category=category_obj,subcategory=subcategory_obj)

            return render(request,"apkstore/softdata_upload.html",{'msg':"Successfull Uploaded"})



    return render(request,"apkstore/softdata_upload.html")

def softdata_upload_update(request):
    if request.FILES:
        upload_file = request.FILES['upload_file']
        file_contents = csv.reader(upload_file)
        if file_contents :
            i = 0
            row_count = 1
            for val in file_contents:
                if i == 0:
                    i = i + 1
                    continue
                app_id = val[0]
                app_id = unicode(app_id, "ISO-8859-1")#order_number
                app_id = unicodedata.normalize('NFKD', app_id).encode('ascii','ignore')

                short_key = val[1]
                short_key = unicode(short_key, "ISO-8859-1")#order_number
                short_key = unicodedata.normalize('NFKD', short_key).encode('ascii','ignore')

                title_name = val[2]
                title_name = unicode(title_name, "ISO-8859-1")#order_number
                title_name = unicodedata.normalize('NFKD', title_name).encode('ascii','ignore')

                app_url = val[3]
                app_url = unicode(app_url, "ISO-8859-1")#order_number
                app_url = unicodedata.normalize('NFKD', app_url).encode('ascii','ignore')

                updated_on = val[4]
                updated_on = unicode(updated_on, "ISO-8859-1")#order_number
                updated_on = unicodedata.normalize('NFKD', updated_on).encode('ascii','ignore')

                category = val[5]
                category = unicode(category, "ISO-8859-1")#order_number
                category = unicodedata.normalize('NFKD', category).encode('ascii','ignore')

                sub_category = val[6]
                sub_category = unicode(short_key, "ISO-8859-1")#order_number
                sub_category = unicodedata.normalize('NFKD', sub_category).encode('ascii','ignore')

                size = val[7]
                size = unicode(size, "ISO-8859-1")#order_number
                size = unicodedata.normalize('NFKD', size).encode('ascii','ignore')
                developer = val[8]
                developer = unicode(developer, "ISO-8859-1")#order_number
                developer = unicodedata.normalize('NFKD', developer).encode('ascii','ignore')

                required_android = val[9]
                required_android = unicode(required_android, "ISO-8859-1")#order_number
                required_android = unicodedata.normalize('NFKD', required_android).encode('ascii','ignore')

                current_version = val[10]
                current_version = unicode(current_version, "ISO-8859-1")#order_number
                current_version = unicodedata.normalize('NFKD', current_version).encode('ascii','ignore')

                desc = val[11]
                desc = unicode(desc, "ISO-8859-1")#order_number
                desc = unicodedata.normalize('NFKD', desc).encode('ascii','ignore')

                rating = val[12]
                rating = unicode(rating, "ISO-8859-1")#order_number
                rating = unicodedata.normalize('NFKD', rating).encode('ascii','ignore')

                img_src_1 = val[13]
                img_src_1 = unicode(img_src_1, "ISO-8859-1")#order_number
                img_src_1 = unicodedata.normalize('NFKD', img_src_1).encode('ascii','ignore')

                img_src_2 = val[14]
                img_src_2 = unicode(img_src_2, "ISO-8859-1")#order_number
                img_src_2 = unicodedata.normalize('NFKD', img_src_2).encode('ascii','ignore')

                img_src_3 = val[15]
                img_src_3 = unicode(img_src_3, "ISO-8859-1")#order_number
                img_src_3 = unicodedata.normalize('NFKD', img_src_3).encode('ascii','ignore')

                img_src_4 = val[16]
                img_src_4 = unicode(img_src_4, "ISO-8859-1")#order_number
                img_src_4 = unicodedata.normalize('NFKD', img_src_4).encode('ascii','ignore')

                img_src_5 = val[17]
                img_src_5 = unicode(img_src_5, "ISO-8859-1")#order_number
                img_src_5 = unicodedata.normalize('NFKD', img_src_5).encode('ascii','ignore')
                page_title = val[18]
                page_title = unicode(page_title, "ISO-8859-1")#order_number
                page_title = unicodedata.normalize('NFKD', page_title).encode('ascii','ignore')

                meta_keyword = val[19]
                meta_keyword = unicode(meta_keyword, "ISO-8859-1")#order_number
                meta_keyword = unicodedata.normalize('NFKD', meta_keyword).encode('ascii','ignore')

                meta_description = val[20]
                meta_description = unicode(meta_description, "ISO-8859-1")#order_number
                meta_description = unicodedata.normalize('NFKD', meta_description).encode('ascii','ignore')

                if app_id:
                    app_id = str(app_id)
                else:
                    app_id = None

                if app_id == None:
                    msg = "Please fill App Id in row " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})

                if short_key:
                    short_key = str(short_key)
                else:
                    short_key = None

		if short_key == None:
                    msg = "Please fill short key in row " + row_count
                    return render(request,"apkstore/softdata_upload.html",{'msg':msg})
		#return HttpResponse(app_id)
	        apkdetails_update = APKDetails.objects.filter(title_shortcode=short_key)
                if title_name:
                   title_name = str(title_name)
                else:
                    title_name = None

                if app_url:
                    apk_url = str(app_url)
                else:
                    apk_url = None
                if updated_on:
                    updated_on = str(updated_on)
                else:
                    updatd_on = None

                if category:
                    category = str(category)
                else:
                    category = None

                if sub_category:
                    sub_category = str(sub_category)
                else:
                    sub_category = None

                if size:
                    size = str(size)
                else:
                    size = None

                if developer:
                    developer = str(developer)
                else:
                    developer = None

                if required_android:
                    required_version = (required_android)
                else:
                    required_version = None

                if current_version:
                    current_version = (current_version)
                else:
                    current_version = None

                if page_title:
                    page_title = str(page_title)
                else:
                    page_title = None

                if meta_keyword:
                    meta_keyword = str(meta_keyword)
                else:
                    meta_keyword = None
                if meta_description:
                    meta_description = str(meta_description)
                else:
                   meta_description = None

                desc1 = ""
                desc2 = ""
                desc3 = ""
                desc4 = ""

                if desc:
                    desc = str(desc)
                    if len(desc)>999:
                        desc1 = desc[:999]
                    if len(desc)>1999:
                        desc2 = desc[999:1999]
                    if len(desc)>2999:
                        desc3 = desc[1999:2999]
                    if len(desc4)>3999:
                        desc4 = desc[3999:]
                else:
                    desc = None

                if rating:
                    rating = float(rating)
                else:
                    rating = None

                if img_src_1:
                    img_src_1 = str(img_src_1)
                else:
                    img_src_1 = None

                if img_src_2:
                    img_src_2 = str(img_src_2)
                else:
                    img_src_2 = None

                if img_src_3:
                    img_src_3 = str(img_src_3)
                else:
                    img_src_3 = None
                if img_src_4:
                    img_src_4 = str(img_src_4)
                else:
                    img_src_4 = None

                if img_src_5:
                    img_src_5 = str(img_src_5)
                else:
                    img_src_5 = None

                #return HttpResponse(updated_on)
		if apkdetails_update:
                    category_obj = Category.objects.latest('id')
                    subcategory_obj = SubCategory.objects.latest('id')
		    subcategory_obj = None
		    apkdetails_update.update(apk_url=apk_url)
		    #apkdetails_update.update(title_name=title_name,devloper=developer,ratting=rating,required_version=required_version,current_version=current_version,description_1=desc1,description_2=desc2,description_3=desc3,description_4=desc4,img_url_1=img_src_1,img_url_2=img_src_2,img_url_3=img_src_3,img_url_4=img_src_4,img_url_5=img_src_5,img_url_6=img_src_6,apk_url=apk_url,size=size,updated_on=updated_on,app_url_show=app_url_show,page_title=page_title,meta_keyword=meta_keyword,meta_description=meta_description,category=category_obj,subcategory=subcategory_obj)
	        else:
		    return render(request,"apkstore/softdata_upload_update.html",{'msg':"App id or short key did not match"})

            return render(request,"apkstore/softdata_upload_update.html",{'msg':"Successfull Uploaded"})



    return render(request,"apkstore/softdata_upload_update.html")


def open_with_id(request):
    ids = request.GET.get('get_id')
    get_code = APKDetails.objects.filter(app_url_show=str(ids))
    if not get_code:
        return HttpResponse("sorry this app not availeble")
    get_code = get_code[0]
    apkdetails = APKDetails.objects.filter(id=get_code.id)
    apkdetails_games = APKDetails.objects.filter(category__meta = "Games")[:12]
    apkdetails_apps = APKDetails.objects.filter(category__meta = "Apps")[:12]
    apkdetails_apps_1 = APKDetails.objects.filter(category__meta = "Apps")[:4]
    apkdetails_apps_2 = APKDetails.objects.filter(category__meta = "Apps")[4:8]
    apkdetails_apps_3 = APKDetails.objects.filter(category__meta = "Apps")[8:12]
    if apkdetails:
        apkdetails_obj = apkdetails[0]
        apkdetails_sub_obj =  apkdetails_obj.apksubdetails_set.all()
        reting =check_reting(apkdetails_obj.ratting)
        if len(reting)>1:
            ret_before = int(reting[0])
            ret_after = reting[1]
        else:
            ret_before = int(reting[0])
        desc1 = apkdetails_obj.description_1
        if len(desc1)>200:
            desc1 = apkdetails_obj.description_1[:20]
        desc2 = apkdetails_obj.description_1[20:]
        desc3 = apkdetails_obj.description_2
    #file_url = "http://android-apkstore.com.cp-in-7.webhostbox.net/cartoon"
    #return HttpResponseRedirect(file_url)      
    return render(request,"apkstore/adp1/BZDIIODBYN.html",{'apkdetails':apkdetails,'apkdetails_games':apkdetails_games,'apkdetails_apps':apkdetails_apps,'apkdetails_apps_1':apkdetails_apps_1,'apkdetails_apps_2':apkdetails_apps_2,'apkdetails_apps_3':apkdetails_apps_3,'apkdetails_sub_obj':apkdetails_sub_obj,"ret_before":ret_before,"ret_after":ret_after,"desc1":desc1,"desc2":desc2,"desc3":desc3})
    #url = "http://android-apkstore.com/"+ str(get_code.app_url_show)
    #return HttpResponse(url)
    #return redirect(url)
    #x = globals()[get_short_code](request)
    #return HttpResponse(x)

def BZDIIODBYN(request):
    apkdetails = APKDetails.objects.filter(title_shortcode="BZDIIODBYN")
    if apkdetails:
        apkdetails_obj = apkdetails[0]
        apkdetails_sub_obj =  apkdetails_obj.apksubdetails_set.all()
        reting =check_reting(apkdetails_obj.ratting)
        if len(reting)>1:
            ret_before = int(reting[0])
            ret_after = reting[1]
        else:
            ret_before = int(reting[0])
	desc1 = apkdetails_obj.description_1
	if len(desc1)>200:
	    desc1 = apkdetails_obj.description_1[1:200]
	desc2 = apkdetails_obj.description_1[200:]
	desc3 = apkdetails_obj.description_2
    #file_url = "http://android-apkstore.com.cp-in-7.webhostbox.net/cartoon"
    #return HttpResponseRedirect(file_url)      
    return render(request,"apkstore/adp1/BZDIIODBYN.html",{'apkdetails':apkdetails,'apkdetails_sub_obj':apkdetails_sub_obj,"ret_before":ret_before,"ret_after":ret_after,"desc1":desc1,"desc2":desc2,"desc3":desc3})
