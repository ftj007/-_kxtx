import unittest
import HTMLTestRunner
import baidu, youdao, time

testunit = unittest.TestSuite()


testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))

#取前面时间
now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))

filename = 'E:\\fff\\自动化\\'+now+'_result.html'

fp = open(filename, 'wb')

runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='百度搜索测试报告',description=u'用例执行情况：')

runner.run(testunit)

