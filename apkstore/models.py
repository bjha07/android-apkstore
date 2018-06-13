from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 25)
    category_id = models.CharField(default = 0,max_length = 50)
    category_our_name = models.CharField(default = 0,max_length = 50)
    meta = models.CharField(default = 0,max_length = 50)
    status = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length = 25)
    category_id = models.CharField(default = 0,max_length = 50)
    category_our_name = models.CharField(default = 0,max_length = 50)
    meta = models.CharField(default = 0,max_length = 50)
    status = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.name

class APKDetails(models.Model):
    app_id = models.CharField(default = 0,max_length = 200)
    title_name = models.CharField(max_length = 50)
    title_shortcode = models.CharField(max_length = 30)
    devloper = models.CharField(max_length = 50,null=True, blank=True)
    ratting = models.FloatField(null=True, blank=True)
    offers_in_app = models.CharField(max_length = 30,null=True, blank=True)  #purchase (Y/N)
    play_store_download_link = models.CharField(max_length = 500,null=True, blank=True)
    apkpure_download_link = models.CharField(max_length = 500,null=True, blank=True)
    apk_version = models.FloatField(null=True, blank=True)
    description_1 = models.CharField(max_length = 2000,null=True, blank=True)
    description_2 = models.CharField(max_length = 2000,null=True, blank=True)
    description_3 = models.CharField(max_length = 2000,null=True, blank=True)
    description_4 = models.CharField(max_length = 2000,null=True, blank=True)
    image = models.FileField(upload_to='apkimage', null=True,blank=True)
    image1 = models.FileField(upload_to='apkimage', null=True,blank=True)
    image2 = models.FileField(upload_to='apkimage', null=True,blank=True)
    image3 = models.FileField(upload_to='apkimage', null=True,blank=True)
    image4 =  models.FileField(upload_to='apkimage', null=True,blank=True)
    image5 = models.FileField(upload_to='apkimage', null=True,blank=True)
    app_upload_file = models.FileField(upload_to='apkfile', null=True,blank=True)
    img_url_1 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_2 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_3 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_4 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_5 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_6 = models.CharField(max_length = 500,default = 0,null=True, blank=True)
    apk_url = models.CharField(max_length = 500,null=True, blank=True)
    size = models.CharField(max_length = 100,null=True, blank=True)
    added_on = models.DateField(null=True, blank=True,auto_now_add=True)
    updated_on = models.DateField(null=True, blank=True)
    number_of_install = models.IntegerField(default=0, null=True, blank=True) # as per play store
    required_version = models.CharField(default = 0 , max_length = 50)
    current_version = models.CharField(default = 0,max_length = 50)
    status = models.IntegerField(default=0, null=True, blank=True)
    page_title = models.CharField(default = 0 , max_length = 1000)
    meta_keyword = models.CharField(default = 0,max_length = 1000)
    meta_description = models.CharField(default = 0,max_length = 1000)
    app_url_show = models.CharField(default = 0 , max_length = 1000)
    category = models.ForeignKey(Category,default="",blank=True,null=True)
    subcategory = models.ForeignKey(SubCategory,default="",blank=True,null=True)
    def __str__(self):
        return self.title_name

class APKSubDetails(models.Model):
    app_id = models.CharField(default = 0,max_length = 200)
    title_name = models.CharField(max_length = 50)
    title_shortcode = models.CharField(max_length = 30)
    devloper = models.CharField(max_length = 50,null=True, blank=True)
    ratting = models.FloatField(null=True, blank=True)
    offers_in_app = models.CharField(max_length = 30,null=True, blank=True)  #purchase (Y/N)
    play_store_download_link = models.CharField(max_length = 500,null=True, blank=True)
    apkpure_download_link = models.CharField(max_length = 500,null=True, blank=True)
    apk_version = models.FloatField(null=True, blank=True)
    description_1 = models.CharField(max_length = 2000,null=True, blank=True)
    description_2 = models.CharField(max_length = 2000,null=True, blank=True)
    description_3 = models.CharField(max_length = 2000,null=True, blank=True)
    description_4 = models.CharField(max_length = 2000,null=True, blank=True)
    image = models.FileField(upload_to='apkimage', null=True,blank=True)
    image1 = models.FileField(upload_to='apkimage', null=True,blank=True)
    image2 = models.FileField(upload_to='apkimage', null=True,blank=True)
    image3 = models.FileField(upload_to='apkimage', null=True,blank=True)
    image4 = models.FileField(upload_to='apkimage', null=True,blank=True)
    image5 = models.FileField(upload_to='apkimage', null=True,blank=True)
    img_url_6 = models.CharField(max_length = 500,default = 0,null=True, blank=True)
    app_upload_file = models.FileField(upload_to='apkfile', null=True,blank=True)
    img_url_1 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_2 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_3 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_4 = models.CharField(max_length = 500,null=True, blank=True)
    img_url_5 = models.CharField(max_length = 500,null=True, blank=True)
    apk_url = models.CharField(max_length = 500,null=True, blank=True)
    size = models.CharField(max_length = 100,null=True, blank=True)
    added_on = models.DateField(null=True, blank=True,auto_now_add=True)
    updated_on = models.DateField(null=True, blank=True)
    number_of_install = models.IntegerField(default=0, null=True, blank=True) # as per play store
    required_version = models.CharField(default = 0,max_length = 50)
    current_version = models.CharField(default = 0,max_length = 50)
    status = models.IntegerField(default=0, null=True, blank=True)
    page_title = models.CharField(default = 0 , max_length = 1000)
    meta_keyword = models.CharField(default = 0,max_length = 1000)
    meta_description = models.CharField(default = 0,max_length = 1000)
    app_url_show = models.CharField(default = 0 , max_length = 1000)
    category = models.ForeignKey(Category,default="",blank=True,null=True)
    subcategory = models.ForeignKey(SubCategory,default="",blank=True,null=True)
    apkdetails = models.ForeignKey(APKDetails,default="",blank=True,null=True) 
    def __str__(self):
        return self.title_name

class Additional_info(models.Model):
    updated_on = models.DateField(null=True, blank=True)
    install_num_from_own_website = models.IntegerField(default=0, null=True, blank=True)
    status = models.IntegerField(default=0, null=True, blank=True)
    #current_version = models.CharField(default = 0,max_length = 50)
    additional_info1 = models.CharField(max_length = 500,null=True, blank=True)
    additional_info2 = models.CharField(max_length = 500,null=True, blank=True)
    apkdetails = models.ForeignKey(APKDetails,default="",blank=True,null=True)
    apksubdetails = models.ForeignKey(APKSubDetails,default="",blank=True,null=True)


class Comments(models.Model):
    added_on = models.DateField(null=True, blank=True,auto_now_add=True)
    comments = models.CharField(max_length = 1000,null=True, blank=True)
    status = models.IntegerField(default=0, null=True, blank=True)
    apkdetails = models.ForeignKey(APKDetails,default="",blank=True,null=True)

class ArticleBlog(models.Model):
    added_on = models.DateField(null=True, blank=True,auto_now_add=True)
    short_code = models.CharField(max_length = 50,default = 0,null=True, blank=True)
    image_link = models.CharField(max_length = 500,default = 0,null=True, blank=True)
    title = models.CharField(max_length = 1000,null=True, blank=True)
    desc_short =  models.CharField(max_length = 200,default = 0,null=True, blank=True)
    description_1 = models.CharField(max_length = 2000,null=True, blank=True)
    description_2 = models.CharField(max_length = 2000,null=True, blank=True)
    meta_desc = models.CharField(max_length = 2000,null=True, blank=True)
    meta_keyword = models.CharField(max_length = 2000,null=True, blank=True)
    page_title = models.CharField(max_length = 500,default = 0,null=True, blank=True)
    blog_url = models.CharField(max_length = 500,default = 0,null=True, blank=True)
    status = models.IntegerField(default=1, null=True, blank=True)
    div_id = models.CharField(max_length = 20,default = 0,null=True, blank=True)




