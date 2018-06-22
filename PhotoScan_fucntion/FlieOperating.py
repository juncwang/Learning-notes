#__author: JuncWang
#date: 2018/6/5

import PhotoScan
import os

# 根据 sPath 项目路径，计算出模型,贴图并保存回项目路劲中
def CalculationModel(sPath):
    doc = PhotoScan.app.document
    doc.open(sPath)
    chunk = doc.chunk
    chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True, reference_preselection=False)
    chunk.alignCameras()
    chunk.buildDepthMaps(quality=PhotoScan.MediumQuality, filter=PhotoScan.AggressiveFiltering)
    chunk.buildDenseCloud()
    chunk.buildModel(surface=PhotoScan.Arbitrary, interpolation=PhotoScan.EnabledInterpolation)
    chunk.buildUV(mapping=PhotoScan.GenericMapping)
    chunk.buildTexture(blending=PhotoScan.MosaicBlending, size=4096)
    doc.save()
    return None

# 根据 sInPath 项目路径,对项目内的模型及贴图按 sOutPath 路径进行输出
def ExportModel(sInPath, sOutPath):
    doc = PhotoScan.app.document
    doc.open(sPath)
    chunk = doc.chunk
    chunk.exportModel(sOutPath,True,6,PhotoScan.ImageFormat.ImageFormatJPEG,True,True,True,True,False,True,False)
    return None

# 根据 sPath 项目路径及 lPath(图片地址列表),将图片加入到项目中并保存
def AddPhotos(sPath,lPath):
    doc = PhotoScan.app.document
    doc.open(sPath)
    chunk = PhotoScan.app.document.addChunk()
    chunk.addPhotos(lPath)
    doc.save()
    return None

# 根据 sPath 项目路径 创建一个空工程
def CreatePSX(sPath):
    doc = PhotoScan.app.document
    try:
        doc.save(sPath)
    except RuntimeError:
        PhotoScan.app.messageBox("Can't save project")
    return None

# 根据 lPath(图片路径列表) 计算出模型及贴图,并输出到 sOutModePath(模型贴图路径) 下
def PhotoCanProcess(lPath,sOutModePath):
    doc = PhotoScan.app.document
    chunk = PhotoScan.app.document.addChunk()
    chunk.addPhotos(lPath)
    chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True, reference_preselection=False)
    chunk.alignCameras()
    chunk.buildDepthMaps(quality=PhotoScan.MediumQuality, filter=PhotoScan.AggressiveFiltering)
    chunk.buildDenseCloud()
    chunk.buildModel(surface=PhotoScan.Arbitrary, interpolation=PhotoScan.EnabledInterpolation)
    chunk.buildUV(mapping=PhotoScan.GenericMapping)
    chunk.buildTexture(blending=PhotoScan.MosaicBlending, size=4096)
    chunk = doc.chunk
    chunk.exportModel(sOutModePath, True, 6, PhotoScan.ImageFormat.ImageFormatJPEG, True, True, True, True, False, True,
                      False)

# 获得图片路径列表 sImagePath(文件路径)
def GetlPathForImagePackage(sImagePath):
    filename = os.listdir(sImagePath)
    lPath = []

    for file in filename:
        lPath.append('%s%s'%(sImagePath,file))

    return lPath



sImagePath = r'C:/Users/JuncWang/Desktop/oooo/'

lPath = GetlPathForImagePackage( sImagePath )

sOutImagePath = r'C:/Users/JuncWang/Desktop/abc.obj'

PhotoCanProcess(lPath, sOutImagePath)









