#__author: JuncWang
#date: 2018/6/5

import PhotoScan

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

# 更具 sPath 项目路径及 lPath(图片地址列表),将图片加入到项目中并保存
def AddPhotos(sPath,lPath):
    doc = PhotoScan.app.document
    doc.open(sPath)
    chunk = doc.chunk
    chunk.addPhotos(lPath)
    doc.save()
    return None




