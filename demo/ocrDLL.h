#ifndef OCRDLL_H_INCLUDED
#define OCRDLL_H_INCLUDED


#ifdef  __cplusplus
#define EXPORT extern "C" __declspec(dllexport)
#else
#define EXPORT __declspec(dllexport)
#endif

/*
�������
  1��param��
  ��ʽ��xml 
  ����"<root><elem imgPath=\"C:\\Users\\liu\\Desktop\\�й�����\\2015_12_22\\3\\IMG_0004.jpg\" imagetype=\"1\" bankName=\"1030200232060000\" accountType=\"2\"  accountNumber=\"06010120060001236\" userName=\"����\" fromDate=\"20140201\" toDate=\"20151010\" rejectHeadRatio=\"0\" rejectMoneyRatio=\"0\" checkAccount=\"0\" /></root>";
������
  ��ʽ��xml 
  ���磺 
   <?xml version="1.0" ?>
  	<stateResult state="0" />
  	<userInfo name="����" account="012345678" />
  	<ticketInfo>
  	     <record inCome="1000" pay="101" />
  	     <record inCome="1000" pay="101" />
  	</ticketInfo>
	����stateResultһ��  0������ 
	                    -1������������� 
						-2�����ܴ򿪸���ͼ��
						-3: ģ��ƥ���ʶ
						-4����ͷʶ���ʶ
						-5������ʶ
*/
EXPORT int ocr(char *param,const char *storePath);
//����ģ��
EXPORT int initLibrary();
//�ͷ�ʶ�����ռ�
EXPORT void freeOCR(char *result);
//�ͷ�ģ��
EXPORT void destroyLibrary();
#endif

initLibrary();
ocr("<root><elem imgPath=\"C:\\Users\\\\IMG_0004.jpg\" imagetype=\"1\" bankName=\"1030200232060000\" accountType=\"2\"  accountNumber=\"06010120060001236\" userName=\"����\" fromDate=\"20140201\" toDate=\"20151010\" rejectHeadRatio=\"0\" rejectMoneyRatio=\"0\" checkAccount=\"0\" /></root>","");