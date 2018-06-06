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
    chunk.exportModel(sOutPath, True, 6, PhotoScan.ImageFormat.ImageFormatJPEG, True, True, True, True, False, True,
                      False)

# 获得图片路径列表 sImagePath(文件路径到非变值文件名) sMinNum(最小变值) sMaxNum(最大变值) sType(图片类型)
def GetlPathForImagePackage(sImagePath,sMinNum,sMaxNum,sType):
    Num = sMinNum
    lPath = []
    while True:
        pathStr = ''.join([sImagePath, str(Num), '.', sType])
        lPath.append(pathStr)
        Num += 1
        if pathNum > sMaxNum:
            return lPath
            pass
        pass








