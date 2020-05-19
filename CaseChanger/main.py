#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# To use Alfred 3+ feedback mechanism:
from workflow import Workflow3, ICON_WEB
from case_changer import case_changer

def main(wf):
    args = wf.args

    original_text = " ".join(args) if len(args) > 0 and len(sys.argv[1].strip()) else sys.stdin.read()
    
    results = {
        "lowercase": case_changer.CaseChanger(original_text).to_lower(),
        "uppercase": case_changer.CaseChanger(original_text).to_upper(),
        "titlecase": case_changer.CaseChanger(original_text).to_title(),
        "lowercamel": case_changer.CaseChanger(original_text).to_lower_camel(),
        "uppercamel": case_changer.CaseChanger(original_text).to_upper_camel()
    }

    for (type_change, result) in results.items():
        wf.add_item(title = result, subtitle = "Convert to " + type_change, valid=True, icon = "icons/icon_" + type_change + ".png", arg=result)

    wf.send_feedback()

# def add_item(self, title, subtitle='', modifier_subtitles=None, arg=None,
#                  autocomplete=None, valid=False, uid=None, icon=None,
#                  icontype=None, type=None, largetext=None, copytext=None,
#                  quicklookurl=None):

if __name__ == u"__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))