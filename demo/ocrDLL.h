#ifndef OCRDLL_H_INCLUDED
#define OCRDLL_H_INCLUDED


#ifdef  __cplusplus
#define EXPORT extern "C" __declspec(dllexport)
#else
#define EXPORT __declspec(dllexport)
#endif

/*
输入参数
  1、param：
  格式：xml 
  例如"<root><elem imgPath=\"C:\\Users\\liu\\Desktop\\中国工商\\2015_12_22\\3\\IMG_0004.jpg\" imagetype=\"1\" bankName=\"1030200232060000\" accountType=\"2\"  accountNumber=\"06010120060001236\" userName=\"李四\" fromDate=\"20140201\" toDate=\"20151010\" rejectHeadRatio=\"0\" rejectMoneyRatio=\"0\" checkAccount=\"0\" /></root>";
输出结果
  格式：xml 
  例如： 
   <?xml version="1.0" ?>
  	<stateResult state="0" />
  	<userInfo name="张三" account="012345678" />
  	<ticketInfo>
  	     <record inCome="1000" pay="101" />
  	     <record inCome="1000" pay="101" />
  	</ticketInfo>
	其中stateResult一项  0：正常 
	                    -1：输入参数错误 
						-2：不能打开给定图像
						-3: 模板匹配拒识
						-4：表头识别拒识
						-5：金额拒识
*/
EXPORT int ocr(char *param,const char *storePath);
//加载模板
EXPORT int initLibrary();
//释放识别结果空间
EXPORT void freeOCR(char *result);
//释放模板
EXPORT void destroyLibrary();
#endif

initLibrary();
ocr("<root><elem imgPath=\"C:\\Users\\\\IMG_0004.jpg\" imagetype=\"1\" bankName=\"1030200232060000\" accountType=\"2\"  accountNumber=\"06010120060001236\" userName=\"李四\" fromDate=\"20140201\" toDate=\"20151010\" rejectHeadRatio=\"0\" rejectMoneyRatio=\"0\" checkAccount=\"0\" /></root>","");