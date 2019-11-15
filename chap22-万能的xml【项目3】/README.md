# 第22章 小结

在这个项目中，你将看到XML可用来表示各种类型的数据，以及如何使用Simple API for XML(SAX)来处理XML文件（读取和解析XML）。

这个项目的目的标是，根据描述各种网页和目录的单个XML文件生成完整的网站。

### 进一步探索

至此，你创建了一个基本程序，可对其做哪些扩展呢？下面是一些建议。

- [ ] 创建一个新的ContentHandler，用于创建由链接组成的网站目录或菜单

- [ ] 在网页中添加导航帮助，让用户知道自己身在何处（在哪个目录中）

- [ ] 创建一个WebSiteConstructor的子类，并在其中重写方法 writeHeader和writeFooter，以实现自定义设计。

- [ ] 再创建一个ContentHandler，使其根据XML文件创建单个网页。

- [ ] 创建一个以某种方式（如RSS）提供网站内容摘要的ContentHandler。

- [ ] 研究其他XML转换工具，尤其是XML转换（XSLT）

- [ ] 使用ReportLab中的Platypus( [http:www.reportlab.org](http:www.reportlab.org) )等工具更具XML文件创建一个或多个PDF文档。

