#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Fulinke"
__pkuid__  = "1800011782"
__email__  = "1800011782@pku.edu.cn"
"""
import sys
from urllib.request import urlopen


def wcount(lines, topn):
	"""count words from lines of text string, then sort by their counts
	in reverse order, output the topn (word count), each in one line. """
	
	lines = lines.lower()
	changelst = [',','.','?','!',';',':','"','(',')','/','_','-','\\n','\\r',"'s","'ll,","'ve","'d"]
	for i in changelst:
		lines = lines.replace(i,' ')
		'''除去标点符号，换行，缩进等，将单词解放出来'''
	wordlist = lines.split()
	count = {}
	for word in wordlist:
		if word not in count:
			count[word] = 1
		else:
			count[word] += 1
	'''统计各个单词的数目，置于字典中'''
	cntresult = list(count.items()) #统计结果置入列表，方便排序#
	cntresult = sorted(cntresult, key = lambda x: x[1],reverse = True)#排序
	if topn <= len(cntresult): #单词数足够多，输出前topn
		ans = cntresult[:topn]
		for i in ans:
			print(i[0], i[1])
	else:  #单词数不足时，全部输出
		for j in cntresult:
			print(j[0], j[1])


def main():
	if len(sys.argv) == 1:
		print('Usage: {} url [topn]'.format(sys.argv[0]))
		print('  url: URL of the txt file to analyze ')
		print('  topn: how many (words count) to output. If not given, will output top 10 words')
		sys.exit(1)	    #对用户进行提示
	else:
		try:
			doc = urlopen(sys.argv[1])
		except Exception as er:
			er = str(er)
			if er == '<urlopen error [Errno 11001] getaddrinfo failed>':
				print('<urlopen error [Errno 11001] getaddrinfo failed>' \
					'网络连接错误')
			if er == 'HTTP Error 404: Not Found':
				print('404: Not Found 未找到URL')
			if 'unknown url type' in er:
				print('URL类型错误')
		docstr = doc.read()
		doc.close()
		docu = str(docstr)
		if len(sys.argv) == 2: #如果只输入网址则只统计前十#
			wcount(docu, 10)
		else:
			topn = int(sys.argv[2])
			wcount(docu, topn)

if __name__=='__main__':
	main()
