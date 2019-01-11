from calibre.gui2.actions import InterfaceAction
from subprocess import Popen

import win32com.client


class Main(InterfaceAction):

    name = 'Send to Kindle'
    action_spec = ('Send to Kindle', None,
                   'Send ebook to Kindle', 'Ctrl+k')

    def genesis(self):
        icon = get_icons('send.png')
        self.qaction.setIcon(icon)
        self.qaction.triggered.connect(self.updateThenSend)

    def updateThenSend(self):
        self.updateMetadata()
        self.sendToKindle()

    def updateMetadata(self):
        from calibre.library import db
        from calibre.ebooks.metadata.meta import set_metadata
        from calibre.gui2 import error_dialog, info_dialog

        rows = self.gui.library_view.selectionModel().selectedRows()
        if not rows or len(rows) == 0:
            return error_dialog(self.gui, 'Cannot update metadata',
                                'No books selected', show=True)
        ids = list(map(self.gui.library_view.model().id, rows))
        db = self.gui.current_db.new_api
        for book_id in ids:
            mi = db.get_metadata(book_id, get_cover=True, cover_as_data=True)
            fmts = db.formats(book_id)
            if not fmts:
                continue
            for fmt in fmts:
                fmt = fmt.lower()
                ffile = db.format(book_id, fmt, as_file=True)
                ffile.seek(0)
                set_metadata(ffile, mi, fmt)
                ffile.seek(0)
                db.add_format(book_id, fmt, ffile, run_hooks=False)
        print('Updated')

    def sendToKindle(self):
        print('sending')
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys("^+k")
