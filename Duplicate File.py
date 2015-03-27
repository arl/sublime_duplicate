import sublime
import io
import sublime_plugin
import shutil
import os.path

class DuplicateFileCommand(sublime_plugin.TextCommand):
    def run(self, edit, paths):
        split = os.path.splitext(paths[0])
        (key, value) = split
        dstfilename = key + " (Copy)" + value
        print("Duplicating \'" + paths[0] + "\' to \'" + dstfilename + "\'")
        shutil.copy(paths[0], dstfilename)
