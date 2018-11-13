from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication
from main_window import Ui_mainWindow
import sys

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.fn_init_event()

    def fn_init_event(self):
        self.btnOpenFile.clicked.connect(self.parse)
        
    def fn_get_file_name(self, path):
        pass

    def parse(self):
        path = QFileDialog.getOpenFileName(self, '打开文件', '../', ('PDF文件 (*.pdf)'))[0]
        print(path)
        # 以二进制读模式打开
        fp = open(path, 'rb') 
        # 用文件对象来创建一个pdf文档分析器
        praser = PDFParser(fp)
        # 创建一个PDF文档
        doc = PDFDocument()
        # 连接分析器 与文档对象
        praser.set_document(doc)
        doc.set_parser(praser)

        # 提供初始化密码
        # 如果没有密码 就创建一个空的字符串
        doc.initialize()

        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            QMessageBox.information(self, '提示', '解析 PDF 失败！', QMessageBox.Yes)
            #raise PDFTextExtractionNotAllowed
        else:
            try:
                QMessageBox.information(self, '提示', '解析 PDF 中，请稍后！', QMessageBox.Yes)
                # 创建PDf 资源管理器 来管理共享资源
                rsrcmgr = PDFResourceManager()
                # 创建一个PDF设备对象
                laparams = LAParams()
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                # 创建一个PDF解释器对象
                interpreter = PDFPageInterpreter(rsrcmgr, device)
            
                text = ''
                # 循环遍历列表，每次处理一个page的内容
                for index, page in enumerate(doc.get_pages()): # doc.get_pages() 获取page列表
                    interpreter.process_page(page)
                    # 接受该页面的LTPage对象
                    layout = device.get_result()
                    # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                    for x in layout:
                        if (isinstance(x, LTTextBoxHorizontal)):
                            text += x.get_text()
                with open(path[:-3] + 'txt', 'w', encoding='utf-8') as f:
                    f.write(text)
                    QMessageBox.information(self, '提示', '解析 PDF 成功，TXT 在 PDF 对应目录下！', QMessageBox.Yes)
            except:
                QMessageBox.information(self, '提示', '解析 PDF 失败！', QMessageBox.Yes)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())



