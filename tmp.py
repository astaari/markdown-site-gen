import re

imre = re.compile(r"([!]\[[^\] ]*\]){1}(\([\S]*\)){1}")
linkre = re.compile(r"([^!]\[[^\] ]*\]){1}(\([\S]*\)){1}")

st = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"

print(imre.findall(st))
print(linkre.findall(st))
