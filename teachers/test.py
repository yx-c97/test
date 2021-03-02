import requests
import unittest

class LoginTest(unittest.TestCase):
      def testlogin(self):
          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet"
          data = {
              "method":"login",
              "loginname":"root11",
              "password":"1111111"
          }
          expect = "菜单"
          response = requests.get(url=url,data = data)
          response.encoding = "utf-8"
          data = response.text

          self.assertIn(expect,data)

      def testfindAllTeacher(self):
          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllTeacher"
          data = {

          }
          #期望数据
          expect = 200
          #调用测试接口
          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"

          #取出状态码和响应数据
          code = response.status_code
          txt = response.text

          #断言
          print(txt)
          self.assertEqual(expect,code)

      def testfindAllMenu(self):
          url = "http://www.jasonisoft.cn:8080/HKR/MenuServlet?method=findAllMenu"
          data = {

          }
          expect = 200

          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"
          code1 = response.status_code
          txt1 = response.text

          print(txt1)
          self.assertEqual(expect, code1)

      def testfindAllStudent(self):
          url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent"
          data = {

          }
          expect = 200

          response = requests.get(url=url, data=data)
          response.encoding = "utf-8"
          code2 = response.status_code
          txt2 = response.text

          print(txt2)
          self.assertEqual(expect, code2)

      def testfindAllPicture(self):
          url="http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllPicture"
          data={

          }
#期望数据
          expect= 200
#调用接口
          response=requests.post(url=url,data=data)
          response.encoding="utf-8"
#取出状态码和相应数据
          code3=response.status_code
          txt3=response.text
#断言
          print(txt3)
          self.assertEqual(expect,code3)


      def testloginOut(self):
          url="http://www.jasonisoft.cn:8080/HKR/UserServlet?method=loginOut"
          data={

          }
          expect=200

          response=requests.post(url=url,data=data)
          response.encoding="utf-8"

          code4=response.status_code
          txt4=response.text


          print(txt4)
          self.assertEquals(expect,code4)









