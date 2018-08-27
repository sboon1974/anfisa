# import sys
import json
from StringIO import StringIO
from .anf_data import AnfisaData
from view.gen_html import formTopPage, emptyPage

#===============================================
class HTML_Setup:

    START = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">'

    META_UTF = \
        '<meta http-equiv="content-type" content="text/html; charset=UTF-8">'

    STYLE_SHEET_REF = \
        '  <link rel="stylesheet" href="%s" type="text/css" media="all"/>'

    JS_REF = \
        '  <script type="text/javascript" src="%s">\n </script>'

#===============================================
class AnfisaService:
    sMain = None

    @classmethod
    def start(cls, config, in_container):
        assert cls.sMain is None
        cls.sMain = cls(config, in_container)

    @classmethod
    def request(cls, serv_h, rq_path, rq_args):
        if rq_path == "/":
            return serv_h.makeResponse(
                content = cls.sMain.formTop(rq_args))
        if rq_path == "/rec":
            return serv_h.makeResponse(
                content = cls.sMain.formRec(rq_args))
        if rq_path == "/norecords":
            return serv_h.makeResponse(
                content = cls.sMain.formNoRec(rq_args))
        if rq_path == "/list":
            return serv_h.makeResponse(mode = "json",
                content = cls.sMain.formList(rq_args))
        if rq_path == "/hot_eval_data":
            return serv_h.makeResponse(mode = "json",
                content = cls.sMain.formHotEvalData(rq_args))
        if rq_path == "/hot_eval_modify":
            return serv_h.makeResponse(mode = "json",
                content = cls.sMain.formHotEvalModify(rq_args))

        return serv_h.makeResponse(error = 404)

    #===============================================
    def __init__(self, config, in_container):
        self.mConfig = config
        self.mInContainer = in_container
        AnfisaData.setup(config)
        self.mHtmlTitle = self.mConfig["html-title"]
        self.mHtmlBase = (self.mConfig["html-base"]
            if self.mInContainer else None)
        if self.mHtmlBase and not self.mHtmlBase.endswith('/'):
            self.mHtmlBase += '/'

    #===============================================
    def _formHtmlHead(self, output, title = None,
            css_files = None, js_files = None):
        print >> output, '<head>'
        print >> output, HTML_Setup.META_UTF
        if self.mHtmlBase:
            print >> output, ' <base href="%s" />' % self.mHtmlBase
        if css_files:
            for fname in css_files:
                print >> output, HTML_Setup.STYLE_SHEET_REF % fname
        if title:
            print >> output, ' <title>%s</title>' % title
        if js_files:
            for fname in js_files:
                print >> output, HTML_Setup.JS_REF % fname
        print >> output, '</head>'

    #===============================================
    def formTop(self, rq_args):
        data_set = AnfisaData.getSet(rq_args.get("data"))
        modes = rq_args.get("m", "")
        output = StringIO()
        formTopPage(output, self.mHtmlTitle, self.mHtmlBase,
            data_set.getName(), AnfisaData.getSetNames(), modes)
        return output.getvalue()

    #===============================================
    def formRec(self, rq_args):
        output = StringIO()
        data_set = AnfisaData.getSet(rq_args.get("data"))
        modes = rq_args.get("m", "")
        rec_no = int(rq_args.get("rec"))
        record = data_set.getRecord(rec_no)
        print >> output, HTML_Setup.START
        print >> output, '<html>'
        self._formHtmlHead(output,
            css_files = ["a_rec.css"], js_files = ["a_rec.js"])
        print >> output, ('<body onload="init_r(\'%s\');">' %
            data_set.getFirstAspectID())
        record.reportIt(output, AnfisaData.getRecHotData(
            data_set.getName(), rec_no, 'X' in modes), "X" in modes)
        print >> output, '</body>'
        print >> output, '</html>'
        return output.getvalue()

    #===============================================
    def formNoRec(self, rq_args):
        output = StringIO()
        emptyPage(output)
        return output.getvalue()

    #===============================================
    def formList(self, rq_args):
        output = StringIO()
        data_index = AnfisaData.getIndex(rq_args.get("data"))
        modes = rq_args.get("m", "")
        filter = json.loads(rq_args.get("filter"))
        output.write(json.dumps(data_index.makeJSonReport(filter,
            'R' in modes, 'X' in modes)))
        return output.getvalue()

    #===============================================
    def formHotEvalData(self, rq_args):
        output = StringIO()
        workspace = rq_args.get("ws")
        modes = rq_args.get("m", "")
        output.write(json.dumps(AnfisaData.getHotEvalData(
            workspace, 'X' in modes)))
        return output.getvalue()

    #===============================================
    def formHotEvalModify(self, rq_args):
        output = StringIO()
        workspace = rq_args.get("ws")
        modes = rq_args.get("m", "")
        item = rq_args.get("it")
        content = rq_args.get("cnt")
        output.write(json.dumps(AnfisaData.modifyHotEvalData(
            workspace, 'X' in modes, item, content)))
        return output.getvalue()

