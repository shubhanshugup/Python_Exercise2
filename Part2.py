from json2html import *
import json
i = open('format.json')
input = json.load(i)
htmlform =json2html.convert(json = input)
Demo = open("Report.html", "w")
text='''
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>
<h2>Test Case Status</h2>
</body>
</html>
'''
Demo.write(text)
Demo.write(htmlform)
Demo.close()
i.close()
print("Process Completed and Check HTML File")
