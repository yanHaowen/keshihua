#coding=utf-8
from kmean import KM
from GuanJianCi import GJC
from pca_m import PCA_
from Guss import GUSS
from corr import Corr
from China import China
from mst import MST
import pca_m
import datetime,time
import os
#choice :算法选择
#dataname:数据名称，后续可能根据此值寻找以前数据图片
#param:是一个list，存放数组
#data:数据
#other:某算法的细分算法，默认为none
#return :回馈信息
#关于生成的html文件：backup文件为后备文件，展示文件夹为show_tu
#关于返回的数据文件：save_show为展示的数据文件，save_backup为后备文件夹
class Holder(object):

    def __init__(self):
        self.kmeans = KM()
        self.pca = PCA_()
        self.guss = GUSS()
        self.corr = Corr()
        self.china = China()
        self.mst = MST()
        self.gjc = GJC()

    def holder(self,choice,dataname,param,data,other=None):
        message = None
        if choice == 1:
            self.kmeans.tu_kmeans(v=data,n_c=param["n_c"],dataname="dataname")
        if choice == 2:
            func_name=["tu_pca","tu_spca"]
            func = getattr(self.pca,func_name[other])
            if other == 0:
                message = func(dataname=dataname,components_ratio=param["components_ratio"],components_n=param["components_n"],data=data)
            else:
                message = func(dataname=dataname,components_n=param["components_n"],data=data)
        if choice == 3:
            self.guss.tu_Gussian(dataname=dataname,X=data[:,0:-1],TrainData=data[:,-1],choice=param["guss_choice"])
        if choice == 4:
            message = self.corr.corr_m(dataname=dataname,data_place=param["data_place"])
        if choice == 5:
            self.china.china_city(dataname=dataname,data=data)
        if choice == 6:
            self.mst.mst(data=data[0],dataN=data[1],dataname=dataname,choice=param["mst_choice"])
        if choice == 7:
            self.gjc.GuanJianCi(data_name=dataname,num=param["num"],text=data)
        return message

    def history(self,dataname):
        data = self.date_create()
        path_txt = "save_backup/"+data+"/"+dataname
        path_tu = "save_backup_tu/"+data+"/"+dataname
        path = []
        if os.path.exists(path_tu):
            path.append(path_tu)
        if os.path.exists(path_txt):
            path.append(path_txt)
        return path

    def date_create(self):
        now_time=datetime.datetime.now().strftime('%Y-%m-%d')
        return now_time

    def clear_holder(self):
        dir_list = ["save_backup","save_backup_tu","save_show","save_show_tu"]
        for dir in dir_list:
            self.clear_helper(dir)

    def clear_helper(self,name):
        now = self.date_create()
        old = os.listdir(name)

        def rmdir(dir):
            for roots,dirs,files in os.walk(dir):
                for name in files:
                    os.remove(roots+"/"+name)
            os.rmdir(dir)

        for itme in old:
            if itme[5:7] != now[5:7] or itme[0:5] != now[0:5]:
                rmdir(name+"/"+itme)
